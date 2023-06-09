from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# import login_page
class page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:8080/page/frime.jsp'
        # 点击健身课程
        self.user = (By.XPATH, '//*[@id="userManagement"]/a')
        self.admin = (By.XPATH, '//*[@id="user"]')
        self.easy_user = (By.XPATH, '//*[@id="registered_users"]/a')
        # 进入子界面
        self.frame1 = (By.XPATH, '//*[@id="demoAdmin"]')
        # 四个管理按钮,查询,重置,删除,添加
        self.b_query = (By.XPATH, '//*[@id="inquire"]')
        self.b_reset = (By.XPATH, '//*[@id="reset"]')
        self.b_delete = (By.XPATH, '//*[@id="delete"]')
        self.b_add = (By.XPATH, '//*[@id="add"]')
        # 信息按钮.查看详情
        self.b_detail1 = (By.XPATH, '/html/body/div/div[2]/div/div[2]/div[4]/div[2]/table/tbody/tr/td/div/button')

        # 查询表单的input
        self.input_title = (By.XPATH, '/html/body/div/div[1]/form/div/div/div/input')

        # 添加表单的input--管理员
        self.phone = (By.XPATH, '//*[@id="phone"]')
        self.user_id = (By.XPATH, '//*[@id="username"]')
        self.user_password = (By.XPATH, '//*[@id="password"]')
        self.nickname = (By.XPATH, '//*[@id="nickname"]')
        self.email = (By.XPATH, '//*[@id="email"]')
        self.b_sub = (By.XPATH, '//*[@id="submit"]')

        # 添加表单的input--注册用户
        self.nickname = (By.XPATH, '//*[@id="nickname"]')
        self.email = (By.XPATH, '//*[@id="email"]')
        self.b_sub = (By.XPATH, '//*[@id="submit"]')

        # 删除表单按钮
        self.del_yes = (By.CLASS_NAME, 'layui-layer-btn0')
        self.del_no = (By.CLASS_NAME, 'layui-layer-btn1')
        self.del_l_1 = (By.XPATH, '/html/body/div/div[3]/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td/div/div/i')
        self.del_l_2 = (By.XPATH, '/html/body/div/div[2]/div/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[1]/div/div/i')


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

    # 删除
    def delete(self, loc):
        self.location(loc).clear()

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
    def wait(self, time=1):
        sleep(time)

    # 查询信息
    def query_(self, input_title):
        self.click(self.user)
        self.click(self.admin)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.input(self.input_title, input_title)
        self.click(self.b_query)
        self.driver.switch_to.parent_frame()
        self.click(self.user)
        self.wait()

    # 添加信息
    def add_(self, user_id, user_password, nickname, email, phone):
        self.click(self.user)
        self.click(self.easy_user)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.click(self.b_add)
        self.input(self.phone, phone)
        self.input(self.nickname, nickname)
        self.input(self.user_id, user_id)
        self.input(self.user_password, user_password)
        self.input(self.email, email)
        self.click(self.b_sub)
        self.driver.switch_to.parent_frame()
        self.click(self.user)
        self.wait()

        self.click(self.user)
        self.click(self.admin)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.click(self.b_add)
        self.input(self.phone, phone)
        self.input(self.nickname, nickname)
        self.input(self.user_id, user_id)
        self.input(self.user_password, user_password)
        self.input(self.email, email)
        self.click(self.b_sub)
        self.driver.switch_to.parent_frame()
        self.click(self.user)
        self.wait()

    # 删除课程信息
    def del_(self):
        self.click(self.user)
        self.click(self.admin)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.click(self.del_l_2)
        self.click(self.b_delete)
        self.click(self.del_yes)
        self.driver.switch_to.parent_frame()
        self.wait()

        self.click(self.easy_user)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.click(self.del_l_1)
        self.click(self.b_delete)
        self.click(self.del_yes)
        self.driver.switch_to.parent_frame()
        self.click(self.user)
        self.wait()

    # 查看具体评论及详细信息
    def detail_(self):
        # 具体评论
        self.click(self.user)
        self.click(self.admin)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.click(self.b_detail1)
        self.driver.switch_to.parent_frame()
        self.wait()

        self.click(self.easy_user)
        self.driver.switch_to.frame(self.location(self.frame1))
        # self.click(self.b_detail2)
        self.driver.switch_to.parent_frame()
        self.click(self.user)
        self.wait()
#
#
# if __name__=='__main__':
#     driver = webdriver.Edge()
#     login_test = login_page.login_page(driver)
#     login_test.login('admin', 'asd123')
#     login_test.wait(3)
#     index_test = page(driver)
#     index_test.query_('admin')
#     index_test.add_('123456789', '123456789', 'syh', '2855483989@qq.com', '15380930116')
#     index_test.del_()