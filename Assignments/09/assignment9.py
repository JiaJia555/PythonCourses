# 1. self 指的是什么? 形参，对象本身
# 2. __init__什么时候调用? 实例化类对象的时候调用
# 3. 当没有__str__方法时,打印出的对象是什么？有__str__方法时,打印出的对象是?返回的必须是什么类型?注意:在返回多个值的时候,默
# 认是元组。
# 返回的是内存地址。返回的必须是字符串
# 4. 创建一个煎饼类调用烹饪时长的方法累计煎饼状态
# 如果煎的时间在0-3 之间则状态为生的
# 如果煎的时间在3-5 之间则状态为半生不熟的
# 如果煎的时间在5-8 之间则状态为全熟的
# 当时间超过8 分钟状态焦了
# 并且还可以给煎饼添加作料
# 比如大葱(hhh),大蒜(hhh)？,烤肠等等
# class pancake(object):
#     def __init__(self):
#         self.cook_status = "生的"
#         self.cook_level = 0
#         self.ingred = []
#
#     def cooking(self,cooked_time):
#         self.cook_level += cooked_time
#         if self.cook_level >= 0 and self.cook_level <3:
#             self.cook_status = "生的"
#         elif self.cook_level >= 3 and self.cook_level <5:
#             self.cook_status = "半生不熟的"
#         elif self.cook_level >= 5 and self.cook_level < 8:
#             self.cook_status = "熟的"
#         else:
#             self.cook_status = "焦的"
#     def addingred(self, food):
#         self.ingred.append(food)
#
#     def pancake_info(self):
#         print("煎饼状态:{},加上作料{}".format(self.cook_status, self.ingred))
#
# jb = pancake()
# jb.cooking(2)
# jb.cooking(4)
# jb.addingred('培根')
#
# jb.pancake_info()
print('hello')