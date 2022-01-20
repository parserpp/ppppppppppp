import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def request(appname, pkg, url):
    chrome_options = Options()  # 实例化Option对象
    chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
    chrome_options.add_argument('--disable-gpu')  # 禁止加载图片
    driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行

    driver.get(url)
    print("=================webdriver=before[" + appname + "]======================")

    print("title:" + driver.title)
    print(driver.page_source)
    # //*[@id="J_NecessaryAppBox"]/ul/li[2]/div
    # html = etree.HTML(driver.page_source)
    # print(html)
    print("===============webdriver===after[" + appname + "]======================")
    return driver.page_source


def get(appname, pkg, url):
    HEADER = {
        # 'User-Agent': ua.random,
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.8'}
    resp = requests.get(url
                        , headers=HEADER
                        , timeout=3
                        , verify=False
                        )
    print("===============get===before[" + appname + "]======================")
    print(resp.text)
    print("===============get===after[" + appname + "]======================")


if __name__ == '__main__':
    print("===============应用已下架，不可分析======================")
    print("===============应用已下架，不可分析======================")
    print("===============应用已下架，不可分析======================")

    request("Plugo WiFi-应用已下架，不可分析", "com.way.smsmaster"
            , "https://www.wandoujia.com/apps/com.way.smsmaster")
    get("Plugo WiFi-应用已下架，不可分析", "com.way.smsmaster"
        , "https://www.wandoujia.com/apps/com.way.smsmaster")

    print("===============豌豆们没有找到这个页面(从未有,不可访问)======================")
    print("===============豌豆们没有找到这个页面(从未有,不可访问)======================")
    print("===============豌豆们没有找到这个页面(从未有,不可访问)======================")
    # request("豌豆们没有找到这个页面", "com.nobody.smsmasterxx", "https://www.wandoujia.com/apps/com.nobody.smsmasterxx")
    # get("豌豆们没有找到这个页面", "com.nobody.smsmasterxx", "https://www.wandoujia.com/apps/com.nobody.smsmasterxx")

    print("===============应用曾上架，现状下架，可继续分析======================")
    print("===============应用曾上架，现状下架，可继续分析======================")
    print("===============应用曾上架，现状下架，可继续分析======================")
    # 异常流量下午分析
    request(" 语音拨号(应用曾上架，现状下架，可继续分析)", "app.taolessyuyinbohao"
            , "https://www.wandoujia.com/apps/app.taolessyuyinbohao")
    get(" 语音拨号(应用曾上架，现状下架，可继续分析)", "app.taolessyuyinbohao"
        , "https://www.wandoujia.com/apps/app.taolessyuyinbohao")

    print("===============正常,可分析======================")
    print("===============正常,可分析=======================")
    print("===============正常,可分析=======================")
    request("微信", "com.tencent.mm", "https://www.wandoujia.com/apps/com.tencent.mm")
    get("微信", "com.tencent.mm", "https://www.wandoujia.com/apps/com.tencent.mm")
