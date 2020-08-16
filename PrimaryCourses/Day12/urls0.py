'''
1.用户输入哪一个页面,我就去跳转到那个页面
getattr()  getattr(x, 'y') is equivalent to x.y.
# res = getattr(views,'signin') # views.signin
# res()
hasattr()
setattr()
delattr()
'''
# import views
#
#
# def run():
#     ipt = input("请输入您要访问的页面:").strip()  # signin-->print("登录页")
#     # ipt()   # signin()
#     if hasattr(views, ipt):
#         func = getattr(views, ipt)
#         func()
#     else:
#         print("404")
#
#
#     # if ipt == "signin":
#     #     views.signin()
#     # elif ipt == "signup":
#     #     views.signup()
#     # elif ipt == "home":
#     #     views.home()
#     # else:
#     #     print("404")
# run()

#urls1

import views0

def run():
    ipt = input("请输入您要访问的页面:").strip()  # 模块名/函数
    modules,func = ipt.split('/')    # a,b = (1,2) a =1 b =2
    # print(res)
    module = __import__(modules)
    # print(obj)
    if hasattr(module,func):
        res = getattr(module,func)
        res()
    else:
        print("404")

run()

