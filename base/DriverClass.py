from appium import  webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Galaxy'
        desired_caps['automationName'] = 'UiAutomator1'
        desired_caps['appPackage'] = 'com.android.vending'
        desired_caps['appActivity'] = 'com.android.vending.AssetBrowserActivity'
        desired_caps['UDID']='RZ8M844H7VE'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver






















#
# from appium import webdriver
# import time
#
#
# class Driver:
#
#     def __init__(self):
#
#         desired_caps = {
#             'platformName': 'Android',
#             'deviceName': 'Galaxy',
#             'platformVersion': '9',
#             'automationName' :'UiAutomator1',
#             'appPackage' :'com.android.vending',
#             'appActivity' : 'com.android.vending.AssetBrowserActivity'
#         }
#
#         self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)