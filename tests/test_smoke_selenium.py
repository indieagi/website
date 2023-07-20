import os
import unittest
import requests
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

class TestWebPages(unittest.TestCase):
    def setUp(self):

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        try:
            # downloaed chromedriver from https://chromedriver.chromium.org/downloads. Python will automatically find it in your PATH.
            self.driver = webdriver.Chrome(options=chrome_options)
        except WebDriverException as e:
            self.fail(f'WebDriver setup failed, error is: {str(e)}')
        
        # Implicitly wait for a certain duration while trying to find any element or elements
        self.driver.implicitly_wait(10)  # seconds

    def tearDown(self):
        self.driver.quit()

    def test_webpage_load(self):
        test_urls = [
            'https://indieagi.org/events/intro-to-full-stack-llm',
            'https://indieagi.org',
            'https://indieagi.org/events/weekly-lightning-talk-meetup'
        ]

        for url in test_urls:
            try:
                response = requests.get(url)
            except requests.exceptions.RequestException as e:
                print(f'DNS resolution failed for {url}, error is: {str(e)}')
                continue

            try:
                self.driver.get(url)
                self.assertEqual(response.status_code, 200, f"Expected status code 200, but got {response.status_code} for the URL {url}")
            except WebDriverException as e:
                print(f'Page load failed for {url}, error is: {str(e)}')


if __name__ == "__main__":
    unittest.main()
