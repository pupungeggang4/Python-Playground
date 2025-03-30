import copy

class A():
    def __init__(self):
        self.x = 10

    def print_x(self):
        print(self.x)

a = A()
b = copy.deepcopy(a)

print(a.x)
print(b.x)

b.x = 1000

print(a.x)
print(b.x)

a.print_x()
b.print_x()
