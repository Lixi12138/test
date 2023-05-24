import unittest
from selenium import webdriver
from user_page_objects.login_page import login_page
from user_page_objects.info_page import info_page


class myTest9(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()
        cls.lp = login_page(cls.driver)
        cls.ap = info_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登陆用例 使用滑块验证
    def test_1_login(self):
        self.lp.login('12345', '123456')

    # 公告界面
    def test_2_info(self):
        self.ap.info_()

