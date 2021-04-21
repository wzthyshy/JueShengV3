# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture(scope='module')
# def driver():
#     global _driver
#     print('------------open browser------------')
#     _driver = webdriver.Chrome()
#     _driver.maximize_window()
#     yield _driver
#     print('------------close browser------------')
#     _driver.quit()