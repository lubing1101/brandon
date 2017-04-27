#!/usr/bin/env python
#-*- coding:utf-8 -*-
import datetime

d0 = d1 = datetime.datetime(2000,1,1,11,23)
d2 = datetime.datetime(2000,1,1,12,0)
d3 = datetime.timedelta(seconds=60)

time_list = []

num = 1

while d0 < d2:
    d0 += d3
    num += 1

for i in range(0,num):
    d4 = set(str(int((d1 + d3 * i).strftime("%Y%m%d%H%M")) % 10000))
    time_list.append(d4)

out = 0

for j in range(0,len(time_list)):
    if (time_list[1] == time_list[j]):
        out += 1

print time_list
print out
