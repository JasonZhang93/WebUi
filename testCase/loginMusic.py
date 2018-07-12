"""
登陆界面的case
继承Driver类,获取浏览器的driver
"""
import time
#导入浏览器driver类
from common.webDriver1 import webDriver
#导入界面元素类
import pageElement.loginPage as loginPage
#导入日志模块类
from common.md_logger import myLog
import unittest
class loginMusic(webDriver,unittest.TestCase):

    #正常登陆的case
    def test_login1(self):
        print("driver",self.driver)
        time.sleep(3)
        loginPage.setUserName(self.driver, 'zhangzichao@newborntown.com')
        loginPage.setUserPwd(self.driver, 'zhangzichao')
        loginPage.click_login(self.driver)
        time.sleep(5)
        isLogin = loginPage.isLogin(self.driver)
        try:
            self.assertEqual(isLogin,True)
            print("登录成功!")
        except Exception as e:
            print("登录成功判断有误",e)
        loginPage.click_exit(self.driver)
    #用户名错误的case
    def test_login2(self):
        time.sleep(3)
        print('login2')
        loginPage.setUserName(self.driver, 'zhangzichao1@newborntown.com')
        loginPage.setUserPwd(self.driver, 'zhangzichao')
        loginPage.click_login(self.driver)

    # 密码错误的的case
    def test_login3(self):
        time.sleep(3)
        print('login3')
        loginPage.setUserName(self.driver, 'zhangzichaoaa@newborntown.com')
        loginPage.setUserPwd(self.driver, 'zhangzichao1')
        loginPage.click_login(self.driver)