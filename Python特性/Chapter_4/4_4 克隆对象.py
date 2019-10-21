# 制作浅复制

xs = [[1, 2, 3, ], [4, 5, 6]]
xy = list(xs)

xs.append([7, 8])  # 不会有影响

xs[1][0] = 'x'  # 会造成 xy 的变化
print(xs)
print(xy)


# 制作深复制
# copy 模块中的 copy,copy() 和 copy.deepcopy() 函数可以复制任何对象
import copy

zx = [[1, 2, 3], [4, 5, 6]]
zy = copy.deepcopy(zx)

zx.append([7, 8])
zx[1][0] = 'x'   # 不会对 zy 造成任何影响

print(zx)
print(zy)


# 复制任意对象
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomtight = bottomright

    def __repr__(self):
        return f'Rectangle({self.topleft}, {self.bottomtight})'


rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)

rect.topleft.x = 999
xrect = copy.deepcopy(rect)
xrect.topleft.x = 888


print(rect)
print(srect)
print('----------deepcopy------------')
print(rect)
print(xrect)