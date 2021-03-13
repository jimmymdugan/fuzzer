# Author: Jimmy Dugan | SWEN-331 | Fuzzer Project
import os
import json
"""
This class is responsible for test operations
"""


class Test:
    def __init__(
            self,
            browser,
            vectors,
            sensitive,
            timeout,
            status_codes,
            discovered_urls,
            sanitized_chars,
            page_titles,
            url_params,
    ):
        self.browser = browser
        self.sensitive = self.load_sensitive(sensitive)
        self.vectors = self.load_vectors(vectors)
        self.timeout = timeout
        self.status_codes = self.load_status_codes(status_codes)
        self.discovered_urls = discovered_urls
        self.page_forms = {}
        self.num_unsanitized_inputs = 0
        self.num_sensitive_leak = 0
        self.num_doa = 0
        self.num_response_errors = 0
        self.sanitized_chars = (self.load_sanitized_chars(sanitized_chars)
                                if isinstance(sanitized_chars, str) else
                                sanitized_chars)
        self.page_forms_dict = self.get_page_forms()
        self.page_titles = page_titles
        self.url_params = url_params

    """
    This function opens the sensitive words file and stores the words in a list

    Args:
        file_path (string): the path of the words file to open

    Raises:
        ValueError: If the file does not exist

    Returns:
        sensitive_list (list): the list of sensitive words from the file
    """
    def load_sensitive(self, file_path) -> list:
        sensitive_list = []
        if not os.path.isfile(file_path):
            raise ValueError("{} does not exist".format(file_path))
        for line in open(file_path):
            sensitive_list.append(line.strip())
        return sensitive_list

    """
    This function opens the vectors file and stores the words in a list

    Args:
        file_path (string): the path of the words file to open

    Raises:
        ValueError: If the file does not exist

    Returns:
        vector_list (list): the list of vectors from the file
    """
    def load_vectors(self, file_path) -> list:
        vector_list = []
        if not os.path.isfile(file_path):
            raise ValueError("{} does not exist".format(file_path))
        for line in open(file_path):
            vector_list.append(line.strip())
        return vector_list

    """
    This function opens the sanitized chars file and stores the words in a list

    Args:
        file_path (string): the path of the words file to open

    Raises:
        ValueError: If the file does not exist

    Returns:
        char_list (list): the list of characters from the file
    """
    def load_sanitized_chars(self, file_path) -> list:
        char_list = []
        if not os.path.isfile(file_path):
            raise ValueError("{} does not exist".format(file_path))
        for line in open(file_path):
            char_list.append(line.strip())
        return char_list

    """
    This function opens the response codes file and stores the codes in a dict

    Args:
        file_path (string): the path of the words file to open

    Raises:
        ValueError: If the file does not exist

    Returns:
        response_codes (dict): a dict of response codes from the json file
    """
    def load_status_codes(self, file_path) -> dict:
        if os.path.isfile(file_path):
            with open(file_path) as json_file:
                response_codes = json.load(json_file)
                return response_codes
        else:
            raise ValueError("{} does not exist".format(file_path))

    """
    This function checks to make sure the input values have been sanitized from the page response

    Args:
        page_response (string): the page response after the request

    Returns:
        out_values (list): a list of unsanitized values in the page response
    """
    def check_page_special_chars(self, page_response, vector) -> list:
        out_values = []
        for char in self.sanitized_chars:
            if char in vector and vector in page_response.text:
                out_values.append(
                    'The character "{}" was not sanitized from input vector "{}"'
                    .format(char, vector))
        return out_values

    """
    This function checks to make sure the input values have been sanitized from the page response

    Args:
        page_response (string): the page response after the request

    Returns:
        out_values (list): a list of unsanitized values in the page response
    """
    def check_sensitive(self, page_response) -> list:
        out_values = []
        detected_lines = []
        for line in page_response.text.splitlines():
            for word in self.sensitive:
                if word in line and line not in detected_lines:
                    detected_lines.append(line)
                    out_values.append(
                        'Potential Sensitive Data Leak: The sensitive word "{}" was found in response.'
                        .format(word))
        return out_values

    """
    This function checks the response time of the page with a given vector to see if there is a possibility of DOS

    Args:
        page_response (string): the page response after the request
        vector (string): the page input vector to test

    Returns:
        message (string): response indicating if the time is greater than the specified timeout limit for the given vector
    """
    def check_response_time(self, page_response, vector) -> str:
        page_load_time_ms = round(page_response.elapsed.total_seconds() * 1000,
                                  2)
        if page_load_time_ms > self.timeout:
            message = 'Potential DOS Vulnerability: This page took {} ms to load with input vector: "{}".'.format(
                page_load_time_ms, vector)
            return message

    """
    This function checks the page status code to catch errors where pages are not found or a bad request

    Args:
        page_response (string): the page response after the request
        vector (string): the page input vector to test

    Returns:
        message (string): response indicating if there was a bad response from the request
    """
    def check_page_status_code(self, page_response, vector) -> str:
        # check if code is defined json file
        code = str(page_response.status_code)
        if code in self.status_codes.keys() and code != "200":
            code_values = self.status_codes[code]
            response_message = code_values["message"]
            response_desc = code_values["description"]
            message = 'HTTP Error {} ({}) with input vector "{}"'.format(
                code, response_message, vector)
            return message

    """
    This function gets all forms for all URLs

    Returns:
        page_forms_dict (dict): dictonary containing all page forms with the URL as the key and forms as values
    """
    def get_page_forms(self) -> dict:
        page_forms_dict = {}
        for url in self.discovered_urls:
            if self.browser.open(url):
                html_content = self.browser.get_current_page()
                if html_content:
                    forms = html_content.find_all("form")
                    if forms:
                        page_forms_dict[url] = forms
        return page_forms_dict

    """
    This function finds vulnerabilities against all inputs found in forms on all discovered links
    
    Sub-tasks:
        Check if a sensitive word is found in the page response
        Check if input vactors are sanitized from the page response
        Check if the response time of the page is greater than the specified timeout
        Check if there is a bad status code returned from the page response
    """
    def test_page_forms(self):
        form_urls = self.page_forms_dict.keys()
        for url in form_urls:
            sensitive_vulns = set()
            special_char_vulns = set()
            response_time_vulns = set()
            status_vulns = set()
            self.browser.open(url)
            underline = "________________________________"
            for form in self.page_forms_dict[url]:
                last1, last2, last3, last4 = (
                    len(response_time_vulns),
                    len(special_char_vulns),
                    len(status_vulns),
                    len(sensitive_vulns),
                )
                for vector in self.vectors:
                    page_inputs = form.find_all("input")
                    for page_input in page_inputs:
                        if page_input.get("type"):
                            type = page_input.get("type")
                            if type != "submit":
                                name = ""
                                if "name" in page_input.attrs:
                                    name = page_input.get("name")
                                try:
                                    self.browser.select_form(
                                        'form[action="#"]')
                                    self.browser[name] = vector
                                except:
                                    pass
                    try:
                        self.browser.select_form('form[action="#"]')
                        response = self.browser.submit_selected()
                    except:
                        pass
                    if self.check_sensitive(response):
                        for output in self.check_sensitive(response):
                            if output:
                                sensitive_vulns.add(output)
                    if self.check_page_special_chars(response, vector):
                        self.num_unsanitized_inputs += 1
                        for output in self.check_page_special_chars(
                                response, vector):
                            if output:
                                special_char_vulns.add(output)
                    if self.check_response_time(response, vector):
                        response_time_vulns.add(
                            self.check_response_time(response, vector))
                        self.num_doa += 1
                    if self.check_page_status_code(response, vector):
                        status_vulns.add(
                            self.check_page_status_code(response, vector))
                        self.num_response_errors += 1

                    if last1 != self.num_response_errors:
                        self.num_response_errors += 1
                if (len(sensitive_vulns) + len(special_char_vulns) +
                        len(response_time_vulns) + len(status_vulns)):
                    print("\n" + underline)
                    print("{}".format(self.page_titles[url]))
                    print(underline)
                for vuln in sensitive_vulns:
                    print(vuln)
                for vuln in special_char_vulns:
                    print(vuln)
                for vuln in response_time_vulns:
                    print(vuln)
                for vuln in status_vulns:
                    print(vuln)

    """
    This function prints the final numbers for the test output
    """
    def print_results(self):
        underline = "________________________________"
        print(underline)
        print("TEST RESULTS")
        print(underline)
        print("Number of unsanitized inputs: {}".format(
            self.num_unsanitized_inputs))
        print("Number of possible sensitive data leakages: {}".format(
            self.num_sensitive_leak))
        print("Number of possible DOS vulnerabilities: {}".format(
            self.num_doa))
        print("Number of HTTP/Response Code Errors: {}".format(
            self.num_response_errors))
