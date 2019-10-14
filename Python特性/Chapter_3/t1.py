# 1.
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

# HEY IS ARMAN!
# hey is arman...


# 2.
def to_upper(text):
    return text.upper()


res = list(map(to_upper, ['arman', 'dawran', 'dilazt']))
print(res)

# ['ARMAN', 'DAWRAN', 'DILAZT']


# 3.
def bark(text):
    return text.upper() + '!'


func = [bark, str.lower, str.capitalize]
for f in func:
    print(f, f('hey, this is arman'))

# <function bark at 0x7f31b393b1e0> HEY, THIS IS ARMAN!
# <method 'lower' of 'str' objects> hey, this is arman
# <method 'capitalize' of 'str' objects> Hey, this is arman
