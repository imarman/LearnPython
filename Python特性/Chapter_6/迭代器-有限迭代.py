my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # > 1
print(next(iterator))  # > 2
print(next(iterator))  # > 3
print(next(iterator))  # > StopIteration 抛异常,因为没有元素了


class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


repeater = BoundedRepeater('hello', 3)
for item in repeater:
    print(item)

# > hello
# > hello
# > hello
