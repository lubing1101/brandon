#-*- coding:utf-8 -*-
from Tkinter import *
from ScrolledText import ScrolledText
root = Tk()
root.title('中国电信天翼视讯')
text = ScrolledText(root,font=('微软雅黑',10))
text.grid()
button = Button(root,text='开始爬取',font=('微软雅黑',10))
button.grid()
var1 = StringVar()
label = Label(root,font=('微软雅黑',10),fg='red',textvar)
label.grid()
avrl.set('')
root.mainloop()


