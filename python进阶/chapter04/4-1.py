class Cat:
    def say(self):
        print('i am a cat')


class Dog:
    def say(self):
        print('i am a dog')


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])


class Duck:
    def say(self):
        print('i am a duck')


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

a = ['bobby1', 'bobby2']
b = ['bobby3', 'bobby']
name_tuple = ('bobby3', 'bobby4')
name_set = set()
name_set.add('bobby5')
name_set.add('bobby6')


# 以下都可以 extend() 只要是可迭代对象就可以
a.extend(b)
a.extend(name_set)
a.extend(name_tuple)
a.extend(company)
print(a)
