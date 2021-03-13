# Author: Jimmy Dugan | SWEN-331 | Fuzzer Project
from mechanicalsoup import StatefulBrowser
"""
This class is responsible for authentication
"""


class Auth:
    def __init__(self, path, browser):
        self.login = '/'
        self.setup = '/setup.php'
        self.security = '/security.php'
        self.username = 'admin'
        self.password = 'password'
        self.path = path
        self.browser = browser

    """
    This function handles the DVWA custom auth argument
    
    Function tasks:
        Browser lands on setup page and resets the database
        Browser lands on login page and logs in with the specified credentials
        Browser lands on security page and selects LOW   
    
    Raises:
        ValueError: if the path is not found 
    
    Returns:
        browser (StatefulBrowser): the authenticated browser
    """
    def dvwa_setup(self) -> StatefulBrowser:

        #setup - create/reset database
        if (self.browser.open(self.path + self.setup)):
            self.browser.select_form('form[action="#"]')
            self.browser.submit_selected()
        else:
            raise ValueError(
                'Invalid URL for DVWA setup. {} not found'.format(self.path +
                                                                  self.setup))

        #login
        if (self.browser.open(self.path + self.login)):
            self.browser.select_form('form[action="login.php"]')
            self.browser['username'] = self.username
            self.browser['password'] = self.password
            self.browser.submit_selected()
        else:
            raise ValueError(
                'Invalid URL for DVWA login. {} not found'.format(self.path +
                                                                  self.login))

        #security - select low
        if (self.browser.open(self.path + self.security)):
            self.browser.select_form('form[action="#"]')
            self.browser['security'] = 'low'
            self.browser.submit_selected()
        else:
            raise ValueError(
                'Invalid URL for DVWA security. {} not found'.format(
                    self.path + self.security))

        return self.browser
