from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.edge.options import Options
import requests

id = [
    #更多成员直接往这里添加就是了
    'B21043229','B21043228',    #2
    # '学号1','密码1',    #1
]

EDGE = {
            "browserName": "MicrosoftEdge",
            "version": "",
            "platform": "WINDOWS",
 
            # 关键是下面这个
            "ms:edgeOptions": {
                'extensions': [],
                'args': [
                    '--headless',
                    '--disable-gpu',
                    '--remote-debugging-port=9222',
                ]}
        }
#这是实现无界面的关键代码


url = 'http://hmgr.sec.lit.edu.cn/web/#/login'
for i in range(0,len(id),1):
    browser = webdriver.Edge(capabilities=EDGE)  # 声明浏览器
    browser.get(url)  # 打开网址
    time.sleep(3)  # 延时加载

    browser.find_element_by_xpath("//*[@id='app']/div/div/div/div[1]/div[2]/div/input").send_keys(id[i])# 自动输入账号
    browser.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/div/input").send_keys(id[i])# 自动输入密码
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id='app']/div/div/button").click()#点击登录
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id='app']/div/div/ul/div[1]/div[2]/li[1]").click()#点击对应的打卡
    time.sleep(3)
    # browser.find_element_by_xpath("//*[@id='app']/div/div[4]/div[8]/input")
    # 点击输入体温
    # browser.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[8]/input').send_keys("36.5")
    # time.sleep(3)
    # browser.find_element_by_xpath("//*[@id='app']/div/button/div").click()#点击提交
    
    # print('执行',i/2+1,'次' )
    time.sleep(0.5) # 休眠0.5秒
    browser.close()

# 发送消息
d1 = '今日已签到'+str(i+1)+'人'

# qqtalk = 'https://qmsg.zendee.cn/send/【Qmsg酱的key】?msg=' + d1 + '&qq=【通知的QQ号】'
# browser = webdriver.Edge(capabilities=EDGE)
# browser.get(qqtalk)

# 微信推送
token = '6fc6c359e6504f27bc72d56d2a965464' #在pushplus网站中可以找到 http://pushplus.hxtrip.com
title= '疫情填报' #改成你要的标题内容
content =d1 #改成你要的正文内容
url = 'http://pushplus.hxtrip.com/send?token='+token+'&title='+title+'&content='+content
requests.get(url)

browser.quit()
