# _*_ coding:utf-8 _*_
print 'input 10 numbers please:'
l = []
for i in range(10):
    l.append(int(raw_input('Input a number:')))
#可以直接使用sort函数：l.sort()
#也可以自己写排序代码(选择排序)
for i in range(9):
    for j in range(i+1,10):
        if l[j]<l[i]:
            temp = l[j]
            l[j] = l[i]
            l[i] = temp
print l