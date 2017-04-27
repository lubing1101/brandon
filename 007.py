#!/usr/bin/python
#-*- coding:utf-8 -*-
def main():
    for i in range(100,1000):
        a = i%10
        b = i/100
        c = (int(i/10))%10
        if i == a**3+b**3+c**3:
            print "%5d"%(i),

if __name__ == "__main__":
    main()