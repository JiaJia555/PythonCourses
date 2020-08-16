#1. 编写一个学生类,每当实例化一位同学时,该班级同学的数量增加1
#位。并且打印输出该班级总共的同学。

# class Students(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Students.count += 1
#
#     @classmethod
#     def print_info(cls):
#         print("该班级公有{}名同学".format(cls.count))
# apple = Students("apple")
# shelley = Students("shelley")
# Students.print_info()

# 2.士兵老Amy 有一把枪(AK47),
# 士兵可以开火
# 枪能够发射子弹
# 枪能够添加子弹
# 枪类:
# 属性:型号,子弹数量
# 行为:发射子弹,添加子弹
# 士兵类：
# 属性：士兵名称,枪支
# 行为：开火行为(需考虑到：是否有枪支？以及添加子弹,发射子弹)
class Gun(object):
    def __init__(self, name):
        self.type = type
        self.bullet_count = 0

    def __str__(self):
        return "{}有{}发子弹".format(self.type, self.bullet_count)

    def shoot(self):
        if self.bullet_count > 0:
            print("发射子弹")
            self.bullet_count -= 1
        else:
            print("没有子弹了，无法发射")

    def add_bullet(self, count):
        self.bullet_count += count
        print("添加子弹：{}".format(count))


class Soldier(object):
    def __init__(self, name):
        self.name = name
        self.Gun = 0

    def fire(self):
        if self.Gun == 0:
            print("{}还没有枪".format(self.name))
        else:
            self.Gun.add_bullet(10)
            print("开火")
            self.Gun.shoot()
# 创建抢对象


AK47 = Gun("AK47")
print(AK47)
# 创建士兵对象
keen = Soldier("keen")
keen.fire()
keen.Gun = AK47
keen.fire()
print(AK47)

# 3.车类1：
# 属性:颜色,轮子个数(默认4 个),重量级,速度(默认为0)
# 行为:加速,减速,停车
# 车类2：
# 属性：在基于车类的基础上,添加一些比如：牌子,型号,空调系统等
# 行为：覆盖车类1 的加速与减速,打印输出车辆信息
class Car:
    def __init__(self, color, weight, speed=0, tire=4):
        self.tire = tire
        self.color = color
        self.weight = weight
        self.speed = speed

    def add_speed(self, value):
        self.speed += value
        if self.speed >= 200:
            self.speed = 200

    def sub_speed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

    def stop(self):
        self.speed = 0


class CarAuto(Car):
    def __init__(self, color, weight, brand, air_conditioner, speed=0, tire=4, cd=''):
        super().__init__(color, weight, speed, tire)
        self.cd = cd
        self.brand = brand
        self.air_conditioner = air_conditioner

    def add_speed(self, value):
        self.speed += value
        if self.speed >= 300:
            self.speed = 300

    def sub_speed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

    def print_info(self):
        print("颜色:{},重量:{},品牌:{}, 空调系统:{}".format(self.color,self.weight,self.brand, self.air_conditioner))

bigG = CarAuto("白色","1G","BMW", "美的")
bigG.print_info()
