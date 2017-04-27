#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = [1, 2, 3]
b = a[:]
print b

# !/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(1, 10):
    print
    for j in range(1, i + 1):
        print "%d*%d=%d" % (i, j, i * j),



#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
	print key, value
	time.sleep(1) # 暂停 1 秒