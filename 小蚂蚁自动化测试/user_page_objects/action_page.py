from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# import login_page

class action_page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:8081/fitness_action_library/list'
        # 公告列表
        self.action_list = (By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div[1]/ul/li[5]/a')

        self.query_1 = (By.XPATH, '/html/body/div/div[3]/div/div/div[2]/div/div/input[1]')
        self.query_2 = (By.XPATH, '/html/body/div/div[3]/div/div/div[2]/div/div/input[2]')
        self.button = (By.XPATH, '//*[@id="fitness_action_library_list"]/div/div/div[2]/div/div/button')

        self.one_action = (By.XPATH, '//*[@id="diy_fitness_action_library_list"]/div/a/div[1]/div/div[2]/img')

        self.like = (By.XPATH, '//*[@id="fitness_action_library_details"]/div[1]/div/div/div/div/div/div/div/div[2]/div[3]/button[1]')
        self.collect = (By.XPATH, '//*[@id="fitness_action_library_details"]/div[1]/div/div/div/div/div/div/div/div[2]/div[3]/button[2]')
        self.commend = (By.XPATH, '//*[@id="fitness_action_library_details"]/div[2]/div/div/div/div/div[4]/div[1]/div/div[2]/div[1]')
        self.submit = (By.XPATH, '//*[@id="fitness_action_library_details"]/div[2]/div/div/div/div/div[4]/div[2]/button')


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
    def action(self):
        # 访问登陆界面
        self.visit(self.url)
        self.click(self.action_list)
        self.wait(2)
        self.input(self.query_1, '1')
        self.input(self.query_2, '1')
        self.click(self.button)
        self.click(self.one_action)
        self.wait(2)
        self.click(self.like)
        self.click(self.collect)
        self.input(self.commend, '我喜欢这个课程')
        self.click(self.submit)
        self.wait(2)


# if __name__ == '__main__':
#     driver = webdriver.Edge()
#     driver.maximize_window()
#     login_test = login_page.login_page(driver)
#     login_test.login('12345', '123456')
#     notice_test = action_page(driver)
#     notice_test.action()