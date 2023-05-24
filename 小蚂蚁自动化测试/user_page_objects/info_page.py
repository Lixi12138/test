from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# import login_page

class info_page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:8081/'
        # 公告列表
        self.my = (By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div[2]/div[1]/span[1]')
        self.myinfo = (By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div[2]/div[2]/div[1]/a')

        self.info = (By.XPATH, '//*[@id="user_index"]/div/div/div/div[1]/div/div/a[1]')
        self.change_password = (By.XPATH, '//*[@id="user_collect"]/div/div/div/div[1]/div/div/a[2]')
        self.collect = (By.XPATH, '//*[@id="user_info"]/div/div/div/div[1]/div/div/a[3]')

        self.old_pwd = (By.XPATH, '//*[@id="input-2"]')
        self.pwd1 = (By.XPATH, '//*[@id="input-2"]')
        self.pwd2 = (By.XPATH, '/html/body/div/div[3]/div/div/div/div[2]/div/form/div[3]/div/input')
        self.button = (By.XPATH, '//*[@id="user_password"]/div/div/div/div[2]/div/div[2]/div')


    # 访问
    def visit(self, url):
        print(url)
        self.driver.get(url)

    # 定位
    def location(self, loc):
        return self.driver.find_element(*loc)

    # 定位多个元素
    def locations(self, loc):
        return self.driver.find_elements(*loc)

    # 输入
    def input(self, loc, text):
        self.location(loc).send_keys(text)

    # 滑动
    def chain(self, loc, len):
        chain = self.location(loc)
        ActionChains(self.driver).click_and_hold(on_element=chain).perform()
        ActionChains(self.driver).move_by_offset(len, 0).perform()
        ActionChains(self.driver).release().perform()

    # 点击
    def click(self, loc):
        self.location(loc).click()

    # 等待
    def wait(self, time):
        sleep(time)

    # 动作界面测试用例
    def info_(self):
        # 访问登陆界面
        self.visit(self.url)
        js_up = "window.scrollTo(0,0)"
        self.driver.execute_script(js_up)
        self.click(self.my)
        self.click(self.myinfo)
        self.wait(2)
        self.click(self.info)
        self.wait(2)
        self.click(self.collect)
        self.wait(2)
        self.click(self.change_password)
        # self.input(self.old_pwd, '123456')
        # self.input(self.pwd1, '123456')
        # self.input(self.pwd2, '123456')
        # self.click(self.button)
        self.wait(2)
#
#
# if __name__ == '__main__':
#     driver = webdriver.Edge()
#     driver.maximize_window()
#     login_test = login_page.login_page(driver)
#     login_test.login('12345', '123456')
#     notice_test = info_page(driver)
#     notice_test.info_()