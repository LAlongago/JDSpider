from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("开始爬取京东商品信息")
# 创建一个新的Selenium浏览器实例
driver = webdriver.Firefox()
print("打开浏览器")

# 打开登录页面
driver.get('https://passport.jd.com/new/login.aspx')

# 在这一步，你需要手动完成登录操作
print("请在浏览器中完成登录，然后按回车继续...")
input()

# 人为登录完成后，现在可以自动导航到其他页面进行爬取
driver.get('https://item.jd.com/100043085799.html')

# 进行页面内容的提取等爬取操作
# 例如，提取页面的标题
title = driver.title
print("页面标题:", title)

# 完成爬取操作后关闭浏览器
driver.quit()
