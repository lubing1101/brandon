# -*- coding:utf-8 -*-
import urllib2,re
from bs4 import BeautifulSoup
import time
import socket
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

fanly_url = "http://zhide.fanli.com/p" #多页地址
format_url = "http://zhide.fanli.com/detail/1-" #商品链接
class Fanly():
    def __init__(self):  #初始化构造函数
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
        self.html_data = []

    def get_html(self,start_page = 1,end_page = 3):
        for i in range(start_page,end_page):
            rt = urllib2.Request(fanly_url+str(i))
            rt.add_header('User-Agent',self.user_agent)
            try:

                my_data = urllib2.urlopen(rt).read()
                #print my_data
                self.html_data.append(my_data)
                time.sleep(2)
                socket.setdefaulttimeout(15) #控制下载内容的时间
            except urllib2.URLError,e:
                 if hasattr(e,'reason'):
                     print u'链接失败',e.reason
        return str(self.html_data)

#html = Fanly().get_html()
class GetData():
    def __init__(self):
        self.html = Fanly().get_html()
        self.href = []
        self.ls = []
        self.url = []
    def get_hrefurl(self):
        reg = r'data-id="\d{6}"' #6位数字
        result = re.compile(reg)
        tag = result.findall(self.html)
        #tag = re.findall(result,self.html)
        #print tag
        for i in tag:
            self.href.append(i)
            #print self.href
        #过滤掉重复信息
        reg2 = r"\d{2}"
        result2 = re.findall(reg2,str(self.href))
        if len(result2):
            for data in result2:
                if data not in self.ls:
                    self.ls.append(data)
                    url = format_url+str(data)
                    self.url.append(url)
                    print self.url[-1]
        return self.url

a = GetData().get_hrefurl()
'''
class Href_mg():
    def __init__(self):
        self.list = GetData().get_hrefurl()
        self.txt_list = []
    def show_mg(self):
        for item in range(len(self.list)):
            if len(self.list):
                url = str(self.list[item])
                mg = urllib2.Request(url)
                req = urllib2.urlopen(mg).read()
                soup = BeautifulSoup(req,"html.parser")
                txt = soup.find_all('h1')
                self.txt_list.append(txt)
                print self.txt_list

data = Href_mg().show_mg()

'''










