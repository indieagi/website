I have the following smoke test in my github repo. How can I configure it to run as a check automatically for any PR on this repo?

Abide by the following contraints:
- runs on Ubuntu latest
- installs selenium chrome webdriver
- installs any packages in requirements.txt
- runs on python 3.11

Include the following information in the instructions:
- the workflow yaml file
- any directories or files that need to be created

<smoke-test>
import subprocess
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def test_smoke_selenium():
  try:
    server = subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE)
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")

    assert "Weekly Lightning Talk Meetup" in driver.page_source, """Test Failed: 
    Text not found: Weekly Lightning Talk Meetup"""

  except WebDriverException as e:
    print(f"Test Failed: WebDriverException encountered. {str(e)}")

  finally:
    driver.quit()
    server.terminate()

test_smoke_selenium()
</smoke-test>