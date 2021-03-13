# Author: Jimmy Dugan | SWEN-331 | Fuzzer Project
import argparse
import mechanicalsoup
from auth import Auth
from discovery import Discovery
from test import Test
import os
"""
Main class responsible for handling input from the command line
"""


class Fuzzer:
    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.base_url = None
        self.extensions = os.path.abspath('text_files/extensions.txt')
        self.words = os.path.abspath('text_files/words.txt')
        self.sensitive = os.path.abspath('text_files/sensitive.txt')
        self.vectors = os.path.abspath('text_files/vectors.txt')
        self.sanitized_chars = os.path.abspath(
            'text_files/sanitized-chars.txt')
        self.status_codes = os.path.abspath('status_codes.json')
        self.form_inputs = {}
        self.url_inputs = {}

    """
    This function is responsible for defining and parsing program arguments
    """
    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("run_option",
                            help='Keyword to specify discovery command')
        parser.add_argument("discover_url",
                            help="Specify the base url to find DVWA")
        parser.add_argument("--custom-auth",
                            help="Specify the custom-auth, --custom-auth=dvwa")
        parser.add_argument(
            "--common-words",
            help="Specify the common words file, --common-words=file")
        parser.add_argument(
            "--extensions",
            help="Specify the extensions file, --extensions=file")
        parser.add_argument(
            "--sensitive", help="Specify the sensitive file, --sensitive=file")
        parser.add_argument("--vectors",
                            help="Specify the vectors file, --vectors=file")
        parser.add_argument(
            "--sanitized-chars",
            help="Specify the sanitized chars file, --sanitized-chars=file")
        parser.add_argument("--slow", help="Timeout delay value, --slow=10")
        args = parser.parse_args()
        parser.parse_args()

        if args.run_option and args.discover_url:
            self.base_url = args.discover_url

        if args.custom_auth == 'dvwa':
            auth = Auth(path=self.base_url, browser=self.browser)
            self.browser = auth.dvwa_setup()

        if args.run_option == 'discover' and args.common_words and args.extensions:
            discover = Discovery(path=self.base_url,
                                 browser=self.browser,
                                 words=self.words,
                                 extensions=self.extensions)
            discover.guess_pages()
            discover.discover_page()
            discover.find_page_inputs()
            discover.print_output()

        if args.run_option == 'test' and args.sensitive and args.vectors:
            timeout = int(args.slow) if args.slow else 0
            discover = Discovery(path=self.base_url,
                                 browser=self.browser,
                                 words=self.words,
                                 extensions=self.extensions)
            discover.discover_page()
            discover.find_page_inputs()
            titles = discover.page_titles
            url_params = discover.page_url_inputs
            sanitized_chars = self.sanitized_chars if args.sanitized_chars else [
                '<', '>'
            ]
            test = Test(browser=self.browser,
                        vectors=self.vectors,
                        sensitive=self.sensitive,
                        timeout=timeout,
                        status_codes=self.status_codes,
                        discovered_urls=discover.discovered_links,
                        sanitized_chars=sanitized_chars,
                        page_titles=titles,
                        url_params=url_params)
            test.test_page_forms()
            test.print_results()


if __name__ == '__main__':
    fuzz = Fuzzer()
    fuzz.parse_args()
