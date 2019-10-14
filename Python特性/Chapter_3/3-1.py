# 1. 函数的嵌套
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 5:
        return yell
    return whisper


print(get_speak_func(6)('Hey Is Arman'))
print(get_speak_func(3)('Hey Is Arman'))

# >>  HEY IS ARMAN!
# >>  hey is arman...


# 2. map() 函数的使用
def to_upper(text):
    return text.upper()


res = list(map(to_upper, ['arman', 'dawran', 'dilazt']))
print(res)

# >>  ['ARMAN', 'DAWRAN', 'DILAZT']


# 3. 函数可存储在数据结构中
def bark(text):
    return text.upper() + '!'


func = [bark, str.lower, str.capitalize]
for f in func:
    print(f, f('hey, this is arman'))

# >>  <function bark at 0x7f31b393b1e0> HEY, THIS IS ARMAN!
# >>  <method 'lower' of 'str' objects> hey, this is arman
# >>  <method 'capitalize' of 'str' objects> Hey, this is arman


# 4.函数可传递给其他函数
def bark(text):
    return text.upper() + '!'


def whisper(text):
    return text.lower() + '...'


def greet(func):
    greeting = func('Hi, I am a Python programmer')
    print(greeting)


greet(bark)
greet(whisper)

# >>  HI, I AM A PYTHON PROGRAMMER!
# >>  hi, i am a python programmer...
