#使用1个函数代替上面的两个函数
def printName(isChinese,name,familyName):
    def inner_print(a,b):
        print("{0} {1}".format(a,b))

    if isChinese:
        inner_print(familyName,name)
    else:
        inner_print(name,familyName)

printName(True,"小七","高")
printName(False,"George","Bush")
