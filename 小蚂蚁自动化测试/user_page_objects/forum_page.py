from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# import login_page

class forum_page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:8081/'
        # 公告列表
        self.forum_list = (By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div[1]/ul/li[2]/a')
        self.forum_1 = (By.XPATH, '//*[@id="forum_index"]/div/div/div[1]/div/div/div[2]/a[1]/div[1]/img')
        self.forum_2 = (By.XPATH, '//*[@id="forum_index"]/div/div/div[1]/div/div/div[2]/a[2]/div[1]/img')
        self.forum_3 = (By.XPATH, '//*[@id="forum_index"]/div/div/div[1]/div/div/div[2]/a[3]/div[1]/img')
        self.forum_4 = (By.XPATH, '//*[@id="forum_index"]/div/div/div[1]/div/div/div[2]/a[4]/div[1]/img')

        self.like = (By.XPATH, '//*[@id="forum_details"]/div[1]/div/div/div/div/div/div/div[4]/div[2]/div[1]/span')
        self.collect = (By.XPATH, '//*[@id="forum_details"]/div[1]/div/div/div/div/div/div/div[4]/div[2]/div[2]/span')

        self.to_commend = (By.XPATH, '//*[@id="forum_details"]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div[3]/button')
        self.commend = (By.XPATH, '//*[@id="forum_details"]/div[2]/div/div/div/div[3]/div[3]/div[1]/div/div[2]/div[1]')
        self.submit = (By.XPATH, '//*[@id="forum_details"]/div[2]/div/div/div/div[3]/div[3]/div[2]/button')

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

    # 点赞
    def likes(self):
        # 访问登陆界面
        self.visit(self.url)
        self.click(self.forum_list)
        self.wait(2)
        # js_up = "window.scrollTo(0,0)"
        # self.driver.execute_script(js_up)
        self.click(self.forum_1)
        self.wait(2)
        self.click(self.like)
        self.wait(2)
        js_up = "window.scrollTo(0,0)"
        self.driver.execute_script(js_up)
        self.click(self.forum_list)

    # 收藏
    def collects(self):
        # 访问登陆界面
        self.visit(self.url)
        self.click(self.forum_list)
        self.wait(2)
        # js_up = "window.scrollTo(0,0)"
        # self.driver.execute_script(js_up)
        self.click(self.forum_1)
        self.wait(2)
        self.click(self.collect)
        self.wait(2)
        js_up = "window.scrollTo(0,0)"
        self.driver.execute_script(js_up)
        self.click(self.forum_list)

    # 评论
    def commends(self, commend):
        # 访问登陆界面
        self.visit(self.url)
        self.click(self.forum_list)
        self.wait(2)
        self.click(self.forum_1)
        self.wait(2)
        self.input(self.commend, commend)
        self.wait(2)
        self.click(self.submit)
        self.wait(2)
        js_up = "window.scrollTo(0,0)"
        self.driver.execute_script(js_up)
        self.click(self.forum_list)

    # 回复某人
    def commend_tos(self, commend):
        # 访问登陆界面
        self.visit(self.url)
        self.click(self.forum_list)
        self.wait(2)
        self.click(self.forum_1)
        self.wait(2)
        self.click(self.to_commend)
        self.input(self.commend, commend)
        self.wait(2)
        self.click(self.submit)
        self.wait(2)
        js_up = "window.scrollTo(0,0)"
        self.driver.execute_script(js_up)
        self.click(self.forum_list)

#
# if __name__ == '__main__':
#     driver = webdriver.Edge()
#     login_test = login_page.login_page(driver)
#     login_test.login('12345', '123456')
#     forum_test = forum_page(driver)
#     forum_test.notice()