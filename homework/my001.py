r1= dict(name="高小一",age=18,salary=30000,city="北京")
r2= dict(name="高小二",age=19,salary=20000,city="上海")
r3= dict(name="高小三",age=20,salary=10000,city="深圳")
tb = [r1,r2,r3]
print(tb)
for x in tb:
    if x.get("salary")>15000:
        print(x)

import time

start = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
        result.append(i*1000+m*100)

end = time.time()
print("耗时：{0}".format((end-start)))

start2 = time.time()
for i in range(1000):
    result = []
    c = i*1000
    for m in range(10000):
        result.append(c+m*100)

end2 = time.time()
print("耗时：{0}".format((end2-start2)))
