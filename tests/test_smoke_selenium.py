import os
import unittest
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPages(unittest.TestCase):
    def setUp(self):

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        try:
            # downloaed chromedriver from https://chromedriver.chromium.org/downloads. Python will automatically find it in your PATH.
            self.driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        except WebDriverException as e:
            self.fail(f'WebDriver setup failed, error is: {str(e)}')
        
        # Implicitly wait for a certain duration while trying to find any element or elements
        self.driver.implicitly_wait(10)  # seconds

    def tearDown(self):
        self.driver.quit()

    def generate_test_urls(self):
        """
        Generate a list of test URLs from HTML files in the templates directory,
        including only links starting with https://www.indieagi.org.
        """
        test_urls = []
        directory = "./templates/"

        for filename in os.listdir(directory):
            if filename.endswith(".html"):
                with open(directory + filename, 'r') as f:
                    contents = f.read()

                soup = BeautifulSoup(contents, 'html.parser')

                for link in soup.find_all('a'):
                    url = link.get('href')
                    if url.startswith("https://www.indieagi.org"):
                        test_urls.append(url)

        return test_urls

    def test_webpage_load(self):
        test_urls = self.generate_test_urls()

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
