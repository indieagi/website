import os
import unittest
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class WebPageTest(unittest.TestCase):
    def setUp(self):
        self.initialize_web_driver()

    def tearDown(self):
        self.quit_web_driver()

    def test_web_pages(self):
        urls_to_test = self.urls_to_test()
        self.assert_urls_load_correctly(urls_to_test)

    def initialize_web_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        try:
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        except WebDriverException as e:
            self.fail(f'WebDriver setup failed: {str(e)}')

        self.driver.implicitly_wait(10)  # seconds

    def quit_web_driver(self):
        self.driver.quit()

    def urls_to_test(self):
        return self.get_urls_from_index_html() + ["https://www.indieagi.org"]

    def get_urls_from_index_html(self):
        urls = []
        index_html_path = "./templates/index.html"

        if os.path.exists(index_html_path):
            with open(index_html_path, 'r') as f:
                html_content = f.read()

            soup = BeautifulSoup(html_content, 'html.parser')

            for link in soup.find_all('a'):
                url = link.get('href')
                if url.startswith("https://www.indieagi.org"):
                    urls.append(url)
    
        return urls

    def assert_urls_load_correctly(self, urls):
        for url in urls:
            self.assert_url_loads_correctly(url)

    def assert_url_loads_correctly(self, url):
        self.assert_url_resolves(url)
        self.assert_url_returns_ok_status(url)

    def assert_url_resolves(self, url):
        try:
            requests.get(url)
        except requests.exceptions.RequestException as e:
            self.fail(f"DNS resolution failed for {url}: {str(e)}")

    def assert_url_returns_ok_status(self, url):
        try:
            self.driver.get(url)
            response = requests.get(url)
            self.assertEqual(response.status_code, 200, f"Expected status code 200, but got {response.status_code} for the URL {url}")
        except WebDriverException as e:
            self.fail(f"DNS resolution succeeded but failed to get 200 OK for {url}. Error: {str(e)}")

if __name__ == "__main__":
    unittest.main()