# import requests  # 工具包发送网络请求
# from lxml import etree   # 转换成对象
# import csv    # 处理表格数据
# url = "https://sj.qq.com/myapp/category.htm?orgame=1"
# response = requests.get(url)
# print(response.text)
# html_data = etree.HTML(response.text)
# li_list = html_data.xpath('//ul[@data-modname="cates"][position()>1]/a/@href')
# # del(li_list[-1])
# for url1 in li_list:
#     for i in range(10):
#         new_url = "https://sj.qq.com/myapp/cate/appList.htm" + url1 + "&pageSize=20&pageContext={}".format(i*20)
#         res = requests.get(new_url).json()
#         if res["count"] == 0:
#             break
#         with open("应用宝.csv", "a", newline="", encoding="utf-8")as f:
#             csv_data = csv.DictWriter(f, fieldnames=["appName", 'authorName', "apkUrl"])
#             for info in res["obj"]:
#                 appName = info['appName']
#                 authorName = info['authorName']
#                 apkUrl = info['apkUrl']
#                 print({"appName": appName, "authorName": authorName, "apkUrl": apkUrl})
#                 csv_data.writerow({"appName": appName, "authorName": authorName, "apkUrl": apkUrl})


"""
可以跳过js获取到了
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
chrome_options.add_argument('--disable-gpu') # 禁止加载图片
driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行

url = "https://sj.qq.com/myapp/category.htm?orgame=1"

driver.get(url)
print(driver.page_source)
# //*[@id="J_NecessaryAppBox"]/ul/li[2]/div
html = etree.HTML(driver.page_source)
print(html)
# extract_announcements_list = html.xpath('//*[@id="J_NecessaryAppBox"]')
# print(extract_announcements_list)
# extract_announcements_list = html.xpath('//*[@id="22786"]/div[2]/div[1]/table/tbody/tr[2]/td/table')
# print(extract_announcements_list)
# for i in extract_announcements_list:
#     announcement_date = i.xpath('./tbody/tr/td[2]/span/text()')
#     announcement_title = i.xpath('./tbody/tr/td[2]/font/a/@title')
#     announcement_link = i.xpath('./tbody/tr/td[2]/font/a/@href')
#     real_link = 'http://www.pbc.gov.cn' + announcement_link[0]
#     print(announcement_title,announcement_date,real_link)
