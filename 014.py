
u = 2.0
d = 1.0
s = 0.0
for i in range(0,20):
    s = s+u/d
    u = u+d
    d = u-d
print ('%f'%s)