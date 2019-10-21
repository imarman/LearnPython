# __rerp__ __str__


class People:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '=='.join(self.name)

    def __repr__(self):
        return '-'.join(self.name)


people = People('arman')
print(people)

# >>> a==r==m==a==n
