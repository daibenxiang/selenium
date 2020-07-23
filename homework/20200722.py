#  9*9乘法表啊
for i in range(1, 10):
    for j in range(1, i+1):
        print("%s*%s=%s" % (j, i, j*i), end=" ")
    print()
s = 100

while s < 1000:
    n = s % 1000
    u = s % 100
    m = s % 10
    if s == n*3+u*3+m*3:
        print(s)
    else:s+=1





