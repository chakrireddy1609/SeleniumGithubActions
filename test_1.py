import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Test_Sample1():
    def test_title(self):
        self.driver.get("https://accounts.staging.joveo.com/")
        assert self.driver.title == "Joveo Account"

    def test_text(self):
        self.driver.get("https://accounts.staging.joveo.com/")
        text_shown = self.driver.find_element(By.XPATH, "//h1[@class='mt-4']").text
        assert text_shown == "Log in to Joveo Account"


