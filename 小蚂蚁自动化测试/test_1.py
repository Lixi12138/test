import unittest
from selenium import webdriver
from page_objects.login_page import login_page
from page_objects.info_page import info_page

# 登录测试及个人信息
class myTest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()
        cls.lp = login_page(cls.driver)
        cls.ip = info_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登陆用例
    def test_1_login(self):
        self.lp.login('admin', 'asd123')
        self.lp.wait(1)

    # 修改信息及修密码用例
    def test_2_info(self):
        self.ip.index('admin', 'asd123', 'asd123')
        self.lp.wait(1)