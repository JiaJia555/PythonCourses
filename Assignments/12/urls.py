import views

def run():
    url = input('请输入路由地址:\n')
    target_models,target_function = url.split('/')
    m =__import__(target_models)
    if hasattr(m,target_function):
        target_function = getattr(m,target_function)
        target_function()
    else:
         print ('Not Found 404 Page')

run()

# def run():
#     ipt = input("请输入您要访问的页面:").strip()  # 模块名/函数
#     modules,func = ipt.split('/')    # a,b = (1,2) a =1 b =2
#     # print(res)
#     module = __import__(modules)
#     # print(obj)
#     if hasattr(module,func):
#         res = getattr(module,func)
#         res()
#     else:
#         print("404")
#
# run()