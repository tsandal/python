# import getpass
# userdb = {}
# def register():
#     username = input('username: ')
#     if username in userdb:
#         print('\033[31;1m%s already exists.\033[0m' % username)
#     else:
#         password = input('password: ')
#         userdb[username] = password
# def login():
#     username = input('username: ')
#     password = getpass.getpass('password: ')
#     # if username not in userdb or userdb['username'] != password:
#     if userdb.get(username) != password:
#         print('\033[31;1mLogin incorrect\033[0m')
#     else:
#         print('\033[32;1mLogin successful\033[0m')
# def show_menu():
#     prompt = """(0) register
# (1) login
# (2) quit
# Please input your choice(0/1/2): """
#     cmds = {'0': register, '1': login}
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice not in '012':
#             print('Invalid choice. Try again.')
#             continue
#             if choice == '2':
#                 break
#             cmds[choice]()
# if __name__ == '__main__':
#     show_menu()

# def zhuc():
#     username=input('username:')
#     if username not in userdb:
#         password=input('password:')
#         userdb[username]=password
#     else:
#         print('用户已存在')
# def dengl():
#     if userdb.get(username)!=password:
#         print('登陆失败')
#     else:
#
# def show_menu():
#     cmds={'0':zhuc,'1':dengl}
#     prompt='''(0)注册
# (1)登陆
# (2)退出
# 请选择(0/1/2):'''
#     while True:
#         choice=input(prompt).strip()[0]
#         if choice not in '012':
#             print('无效输入,请重试')
#             continue
#         if choice=='2':
#             break
#         cmds[choice]()
# if __name__ == '__main__':
#     show_menu()

import getpass
userdb = {}
def register():
    username = input('username: ')
    if username in userdb:
        print('\033[31;1m%s already exists.\033[0m' % username)
    else:
        password = input('password: ')
        userdb[username] = password
def login():
    username = input('username: ')
    password = getpass.getpass('password: ')
    # if username not in userdb or userdb['username'] != password:
    if userdb.get(username) != password:
        print('\033[31;1mLogin incorrect\033[0m')
    else:
        print('\033[32;1mLogin successful\033[0m')
def show_menu():
    prompt = """(0) register
(1) login
(2) quit
Please input your choice(0/1/2): """
    cmds = {'0': register, '1': login}
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '012':
            print('Invalid choice. Try again.')
            continue
        if choice == '2':
            break
        cmds[choice]()
if __name__ == '__main__':
    show_menu()




















