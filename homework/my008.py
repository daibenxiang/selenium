class Student:
    company = "SXT"  # 类属性

    @staticmethod
    def add(a, b):  # 静态方法
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a+b

Student.add(20,30)
