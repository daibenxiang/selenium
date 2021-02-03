#测试方法的动态性
class Person:
    def work(self):
        print("努力上班！")

def play_game(self):
    print("{0}玩游戏".format(self))

def work2(s):
    print("好好工作，努力上班！")


Person.play = play_game
Person.work = work2
p = Person()
p.play()
p.work()

