#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re

page = requests.get('http://tieba.baidu.com/p/2460150866')
re_jpg = re.compile(r'http://imgsrc\.baidu\.com/forum/w%3D580/sign=.*?jpg')
imgs = re.findall(re_jpg, page.text)
for i in imgs:
    print(i[-44:])
    with open('imgs/' + i[-44:], 'wb') as img_file:
        img_file.write(requests.get(i).content)

'''
[root@lb3 python]# cat 3.py
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import re
for img_url in re.findall(r'http://imgsrc\.baidu\.com/forum/w%3D580/sign=.*?jpg',requests.get('http://tieba.baidu.com/p/2460150866').text):
     with open('imgs/' + img_url[-44:],'wb') as img_file:
          img_file.write(requests.get(img_url).content)
