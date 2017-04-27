# -*- coding:utf-8 -*-
import urllib2
import re
import os

def filter_tags(htmlstr):
   re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I)
   re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)
   re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)
   re_p=re.compile('<P\s*?/?>')
   re_h=re.compile('</?\w+[^>]*>')
   re_comment=re.compile('<!--[^>]*-->')
   s=re_cdata.sub('',htmlstr)
   s=re_script.sub('',s)
   s=re_style.sub('',s)
   s=re_p.sub('\r\n',s)
   s=re_h.sub('',s)
   s=re_comment.sub('',s)
   blank_line=re.compile('\n+')
   s=blank_line.sub('\n',s)
   return s

urlcontent = urllib2.urlopen('http://news.qq.com/a/20120515/').read()
#print urlcontent.decode('gbk') #解码
rege = re.compile(r"/a/\d{8}/\d{6}.htm")
get_url = re.findall(rege,urlcontent)
#print get_url #打印list格式
get_url.sort()
for i in xrange(0,len(get_url)):
    get_url[i] = "http://news.qq.com"+get_url[i]
    #print get_url[i]
    try:
        sub_web = urllib2.urlopen(get_url[i]).read()
    except urllib2.URLError,e:
        print "获取连接失败，跳过"
        continue
    re_keyt = "<h1>(.*?)</h1>"
    title = re.findall(re_keyt,sub_web)
    #print title[0].decode("gbk")
    re_keyc = re.compile("<div id=\"Cnt-Main-Article-QQ\".*</p></div>\n</div>",re.DOTALL)
    content = re.findall(re_keyc,sub_web)
    #print content
    if len(title) == 0 or len(content) == 0:
        continue
    re_content = filter_tags(title[0]+"\r\n"+content[0])
    #print re_content.decode('gbk')
    w = file('a.txt','a+')
    w.write(re_content)
    w.close()
    print '正在获取下载'+get_url[i][-10:]+"网页内容"

print "全部下载完成"
