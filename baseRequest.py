from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree



def request(pkg,url):
    chrome_options = Options()  # 实例化Option对象
    chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
    chrome_options.add_argument('--disable-gpu')  # 禁止加载图片
    driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行
    driver.get(url)
    print("==================before[" + pkg + "]======================")

    print("title:"+driver.title)
    print(driver.page_source)

    # //*[@id="J_NecessaryAppBox"]/ul/li[2]/div
    # html = etree.HTML(driver.page_source)
    # print(html)
    print("==================after[" + pkg + "]======================")
    return driver.page_source


if __name__ == '__main__':
    request("com.wifi.wifiswys","https://www.wandoujia.com/apps/com.wifi.wifiswys")
    request("app.taolessyuyinbohao","https://www.wandoujia.com/apps/app.taolessyuyinbohao")
    request("com.way.smsmaster","https://www.wandoujia.com/apps/com.way.smsmaster")
    request("xxxxx","https://www.wandoujia.com/apps/xxxx")