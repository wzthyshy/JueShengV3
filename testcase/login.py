from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin:
    def test_login(self):
        option = Options()
        option.debugger_address = "localhost:8081"

        driver = webdriver.Chrome(chrome_options=option)
        driver.get("https://ke.qq.com/")
