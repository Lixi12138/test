import unittest
from selenium import webdriver
from page_objects.login_page import login_page
from page_objects.user_page import page

# 用户管理
class myTest4(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()
        cls.lp = login_page(cls.driver)
        cls.sp = page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登陆用例
    def test_1_login(self):
        self.lp.login('admin', 'asd123')

    # 查询案例
    def test_2_user_query(self):
        self.sp.query_('admin')

    # 添加案例
    def test_3_user_add(self):
        self.sp.add_('123456789', '123456789', 'syh', '2855483989@qq.com', '15380930116')

    # 删除案例
    def test_4_user_del(self):
        self.sp.del_()

