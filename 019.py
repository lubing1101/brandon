#_*_ coding:utf-8 _*_

a = [1,2,3,4,5,6,7,8,9]
l = len(a)
print a
for i in range(l/2):
    a[i],a[l-i-1] = a[l-i-1],a[i] #注意此句
print a


MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print 'The largar one is %d' % MAXIMUM(a,b)
    print 'The lower one is %d' % MINIMUM(a,b)

    a = 100
    print 100 & 0x00F0

    if __name__ == '__main__':
        from Tkinter import *

        canvas = Canvas(width=800, height=600, bg='violet')
        canvas.pack(expand=YES, fill=BOTH)
        k = 1
        j = 1
        for i in range(0, 26):
            canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
            k += j
            j += 0.3

        mainloop()

        if __name__ == '__main__':
            from Tkinter import *

            canvas = Canvas(width=300, height=300, bg='green')
            canvas.pack(expand=YES, fill=BOTH)
            x0 = 263
            y0 = 263
            y1 = 275
            x1 = 275
            for i in range(19):
                canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
                x0 = x0 - 5
                y0 = y0 - 5
                x1 = x1 + 5
                y1 = y1 + 5

            x0 = 263
            y1 = 275
            y0 = 263
            for i in range(21):
                canvas.create_line(x0, y0, x0, y1, fill='red')
                x0 += 5
                y0 += 5
                y1 += 5

            mainloop()