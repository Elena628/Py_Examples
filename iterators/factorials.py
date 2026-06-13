class Factorial:
    def __init__(self, border):
        self.border = border
        self.current = 1
        self.count = 1

    def __iter__(self):
        # self.current = 1
        # self.count = 1
        # если нужно использовать один объект в программе для нескольких итераций, 
        # делаем такое обнуление, чтобы все работало
        return self

    def __next__(self):
        if self.current * self.count > self.border:
            raise StopIteration
        self.current *= self.count
        self.count += 1
        return self.current


for f in Factorial(150):
    print(f)