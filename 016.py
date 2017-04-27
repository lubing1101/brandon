a = [0]*101
for i in range(2,11):
    for j in range(i+i,101,i):
        a[j]=-1;
for i in range(2,101):
    if a[i]!=-1:
        print ' ',i,







def fun(i,cnt):
    if i==0:
        print 'There are %d digit in the number.'%cnt
        return
    print i%10,
    i/=10
    cnt+=1
    fun(i,cnt)

i = int(raw_input('Input a number:'))
fun(i,0)