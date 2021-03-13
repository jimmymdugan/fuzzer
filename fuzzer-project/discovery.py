# Author: Jimmy Dugan | SWEN-331 | Fuzzer Project
import os
import re
"""
This class is responsible for discovery operations
"""


class Discovery():
    def __init__(self, path, browser, words, extensions):
        self.common_words_list = self.load_common_words(words)
        self.extensions_list = self.load_extensions(extensions)
        self.browser = browser
        self.path = path
        self.guessed_pages = [path]
        self.discovered_links = []
        self.page_form_inputs = {}
        self.page_url_inputs = {}
        self.cookies = []
        self.page_titles = {}

    """
    This function opens the common words file and stores the words in a list
    
    Args:
        file_path (string): the path of the words file to open
    
    Raises:
        ValueError: If the file does not exist
    
    Returns:
        words_list (list): the list of common words from the file
    """
    def load_common_words(self, file_path) -> list:
        words_list = []
        if not os.path.isfile(file_path):
            raise ValueError('{} does not exist'.format(file_path))
        for line in open(file_path):
            words_list.append(line.strip())
        return words_list

    """
    This function opens the extensions file and stores the words in a list

    Args:
        file_path (string): the path of the extensions file to open
    
    Raises:
        ValueError: If the file does not exist
    
    Returns:
        extensions (list): the list of extensions from the file
    """
    def load_extensions(self, file_path) -> list:
        extensions = []
        if not os.path.isfile(file_path):
            raise ValueError('{} does not exist'.format(file_path))
        for line in open(file_path):
            extensions.append(line.strip())
        return extensions

    """
    This function creates all combinations of URLs and tests if the URLs are valid
    """
    def guess_pages(self):
        for url in self.guessed_pages:
            if '.' not in url:
                for word in self.common_words_list:
                    current_url = "{}/{}".format(url, word.lower())
                    if (self.browser.open(current_url)):
                        self.guessed_pages.append(current_url)
                    for extension in self.extensions_list:
                        current_url = "{}/{}.{}".format(
                            url, word.lower(), extension.lower())
                        if 'logout' not in current_url:
                            if (self.browser.open(current_url)):
                                self.guessed_pages.append(current_url)

    """
    This function visits the guessed URLs and checks to see if there are unlinked URLs on the page
    """
    def discover_page(self):
        for url in self.guessed_pages:
            if 'logout' not in url and self.browser.open(url):
                html_content = self.browser.get_current_page()
                all_links_in_page = html_content.find_all('a')
                for link in all_links_in_page:
                    href_link = link.get('href')
                    if isinstance(href_link, str):
                        # ignore external sites and logout page
                        joined_link = '{}/{}'.format(
                            url, href_link
                        ) if '://' not in href_link and 'logout' not in href_link else None
                    if joined_link and joined_link not in self.discovered_links \
                            and '://localhost' in joined_link \
                            and self.browser.open(joined_link):
                        self.discovered_links.append(joined_link)

    """
    This function visits each page found and checks to see if there are inputs
    
    Valid cases for input:
        - In the URL: eg. ?input=value
        - html form input values
        - stored cookies
    """
    def find_page_inputs(self):
        for url in self.discovered_links:
            self.page_form_inputs[url] = []
            self.page_url_inputs[url] = []
            curr_form_input_key = self.page_form_inputs[url]
            curr_url_input_key = self.page_url_inputs[url]
            if self.browser.open(url):
                html_content = self.browser.get_current_page()
                # get page title form html content
                page_title = ''
                if html_content:
                    titles = html_content.find_all('h1')
                    for title in titles:
                        page_title += '{} '.format(title.text.strip())
                    page_title += '- {}'.format(
                        url) if page_title else '{}'.format(url)
                    self.page_titles[url] = page_title
                # check if the URL has a direct input value which can be manipulated
                url_input_value = re.search('\?(.*)=', url)
                if url_input_value:
                    input_value = url_input_value.group(1)
                    curr_url_input_key.append(input_value.strip())
                # check for input values in page form
                if html_content:
                    all_page_forms = html_content.find_all('input')
                    for input in all_page_forms:
                        input_name = input.get('name')
                        if isinstance(input_name, str):
                            curr_form_input_key.append(input_name)
                # check cookie values for inputs
                for cookie in self.browser.session.cookies:
                    if cookie not in self.cookies:
                        self.cookies.append(cookie)

    """
    This function prints and formats the final data
    """
    def print_output(self):
        underline = '________________________________'
        # print all valid links guessed
        print('VALID LINKS GUESSED:')
        print(underline)
        for url in self.guessed_pages:
            print(url)
        print(underline)
        # print all links found on the page
        print('LINKS DISCOVERED ON PAGE:')
        print(underline)
        for link in self.discovered_links:
            print(link)
        print(underline)
        # print all inputs found on the page
        print('INPUTS FOUND ON PAGES:')
        print(underline)
        print('Form inputs:')
        print(underline)
        for page in self.page_form_inputs:
            if self.page_form_inputs[page]:
                page_title = self.page_titles[page]
                print('\n{}'.format(page_title))
                for input in self.page_form_inputs[page]:
                    print('\t{}'.format(input))
        print(underline)
        print('URL inputs:')
        print(underline)
        for page in self.page_url_inputs:
            if self.page_url_inputs[page]:
                page_title = self.page_titles[page]
                print('\n{}'.format(page_title))
                for input in self.page_url_inputs[page]:
                    print('\t{}'.format(input))
        print(underline)
        # print the cookies stored on the page which can be manipulated
        print('COOKIES:')
        for cookie in self.cookies:
            print('\t{}'.format(cookie))
        print(underline)
