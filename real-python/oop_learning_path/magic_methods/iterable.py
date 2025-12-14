class Iterable:
    def __init__(self, max_number):
        self.items = (i ** 2 for i in range(1, max_number+1))

    def __iter__(self):
        return iter(self.items)

it = Iterable(10)
for i in it:
    print(i)