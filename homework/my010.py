#测试__call__，可调用对象

class SalaryAccount:
    '''工资计算类'''

    def __call__(self, salary):
        yearSalary = salary*12
        daySalary = salary//30
        hourSalary = daySalary//8

        return dict(monthSalary=salary, yearSalary=yearSalary, daySalary=daySalary, hourSalary=hourSalary)


s = SalaryAccount()
print(s(5000))
