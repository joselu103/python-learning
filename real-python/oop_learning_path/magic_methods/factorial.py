from time import perf_counter


class Factorial:
    def __init__(self):
        self.cache = {}

    def __call__(self, n: int):
        if n <= 0:
            raise ValueError
        if n in self.cache:
            print(f"Found in cache!")
            return self.cache[n]

        if n == 0 or n == 1:
            return 1

        result = n * self(n - 1)
        self.cache[n] = result

        return result

    def __repr__(self):
        print(f"{self.__class__.__name__}(cache = {self.cache})")


factorial_gen = Factorial()

# for i in range(2):
#     for j in range(1, 10):
#         start = perf_counter()
#         print(f"Factorial of {j}: {factorial_gen(j)}")
#         print(f"{perf_counter() - start}s")
#         print('---')

for i in range(2):
    start = perf_counter()
    print(f"Factorial of 1000: {factorial_gen(200)}")
    print(f"{perf_counter() - start}s")
    print("-" * 20)

print(factorial_gen)