import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture()
def setup(request):
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    options = ["--headless", "--ignore-certificate-errors"]
    for option in options:
        chrome_options.add_argument(option)
    request.cls.driver = webdriver.Chrome(service=service,options=chrome_options)
    yield request.cls.driver
    request.cls.driver.close()

