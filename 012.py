from math import sqrt
n = int(raw_input('input a number:'))
sum = n*-1
k = int(sqrt(n))
for i in range(1,k+1):
    if n%i == 0:
        sum += n/i
        sum += i
if sum == n:
    print 'YES'
else:
    print 'NO'