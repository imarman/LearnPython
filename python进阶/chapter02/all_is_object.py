def ask(name='bobby'):
    print(name)


class Person:
    def __init__(self):
        print('bobby1')


def test():
    print('this is test')
    return ask


# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())


my_func = test()
my_func('hahhaha')
