s = 0
t = 1
for i in range(1,21):
    t*=i
    s+=t
print s


def fun(i):
    if i==1:
        return 1
    return i*fun(i-1)

print (fun(5))





def output(s,l):
    if l==0:
        return
    print s[l-1]
    output(s,l-1)

s = raw_input('Input a string:')
l = len(s)
output(s,l)



def fun(i):
    if i==1:
        return 10
    return fun(i-1)+2

print fun(5)