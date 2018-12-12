# stack = []
# def push_it():
#     item = input('item to push: ')
#     stack.append(item)
# def pop_it():
#     if stack:
#         print("\033[31;1mPopped %s\033[0m" % stack.pop())
#     else:
#         print('\033[31;1mEmpty stack\033[0m')
# def view_it():
#     print("\033[32;1m%s\033[0m" % stack)
# def show_menu():
#     prompt = """(0) push_it
# (1) pop_it
# (2) view_it
# (3) quit
# Please input your choice(0/1/2/3): """
#     cmds = {'0': push_it, '1': pop_it, '2': view_it}
#     while True:
#         # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
#         choice = input(prompt).strip()[0]
#         if choice not in '0123':
#             print('Invalid input. Try again.')
#             continue  # 结束本次循环
#
#         if choice == '3':
#             break  # 结束整个循环
#
#         cmds[choice]()  # push_it()  pop_it()
#         # if choice == '0':
#         #     push_it()
#         # elif choice == '1':
#         #     pop_it()
#         # elif choice == '2':
#         #     view_it()
# if __name__ == '__main__':
#     show_menu()
# stack=[]
# def push_it():
#     item=input('数据:').strip()
#     if item:
#         stack.append(item)
# def pop_it():
#     if stack:
#         print('从栈中弹出%s'%stack.pop())
#     else:
#         print('\033[31;1m空栈\033[0m')
# def view_it():
#     print('\033[32;1m%s\033[0m'%stack)
# def show_menu():
#     cmds={'0':push_it(),'1':pop_it(),'2':view_it()}
#     prompt="""(0)压栈
# (1)出栈
# (2)查询
# (3)退出
# 请选择(0/1/2/3):"""
#     while True:
#         choice=input(prompt).strip()[0]
#         if choice not in '0123':
#             print('无效输入，重试')
#             continue
#         if choice=='3':
#             print('bey-bey')
#             break
#         cmds[choice]()
#         # if choice=='0':
#         #     push_it()
#         # elif choice=='1':
#         #     pop_it()
#         # else:
#         #     view_it()
# if __name__ == '__main__':
#     show_menu()
# stack = []
#
#
# def push_it():
#     item = input('item to push: ')
#     stack.append(item)
#
#
# def pop_it():
#     if stack:
#         print("\033[31;1mPopped %s\033[0m" % stack.pop())
#     else:
#         print('\033[31;1mEmpty stack\033[0m')
#
#
# def view_it():
#     print("\033[32;1m%s\033[0m" % stack)
#
#
# def show_menu():
#     prompt = """(0) push_it
# (1) pop_it
# (2) view_it
# (3) quit
# Please input your choice(0/1/2/3): """
#     cmds = {'0': push_it, '1': pop_it, '2': view_it}
#     while True:
#         # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
#         choice = input(prompt).strip()[0]
#         if choice not in '0123':
#             print('Invalid input. Try again.')
#             continue  # 结束本次循环
#
#         if choice == '3':
#             break  # 结束整个循环
#
#         cmds[choice]()  # push_it()  pop_it()
#         # if choice == '0':
#         #     push_it()
#         # elif choice == '1':
#         #     pop_it()
#         # elif choice == '2':
#         #     view_it()
# if __name__ == '__main__':
#     show_menu()





























