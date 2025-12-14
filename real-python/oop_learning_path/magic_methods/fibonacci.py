class FibonacciIterator:
    def __init__(self, max_count):
        self.current = 0
        self.next = 1
        self.count = 0
        self.max_count = max_count

    def __iter__(self):
        return self

    def __next__(self):
        if not self.max_count or self.count > self.max_count:
            raise StopIteration

        value = self.current
        self.current, self.next = self.next, self.next + self.current
        self.count += 1
        return value

f_iter = FibonacciIterator(10)
for i in f_iter:
    print(i)