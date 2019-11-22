def my_func(a, b):
    return a + b


def handle_a():
    return 'This is handle_a function'


def handle_b():
    return 'This is handle_b function'


def handle_default():
    return 'This is default function'


func_dick = {
    'cond_a': handle_a,
    'cond_b': handle_b,
}

my_choose = func_dick.get('cond_a', handle_default)()


# 例子2
# function
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y


# dict
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, None)()


result = dispatch_if('add', 1, 2)
result1 = dispatch_dict('sub', 1, 2)
print(result)
print(result1)

