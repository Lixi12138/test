import unittest
from selenium import webdriver
from user_page_objects.login_page import login_page

class myTest5(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()
        cls.lp = login_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登陆用例 使用滑块验证
    def test_1_login(self):
        self.lp.login('12345', '123456')


