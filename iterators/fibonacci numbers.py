class Fib:
    def __init__(self, end):
        self.end = end
        self.previous = 0
        self.current = 1
        

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.previous > self.end:
            raise StopIteration
        out = self.previous
        result = self.previous + self.current
        self.previous, self.current = self.current, result
        return out

        
for f in Fib(10):
    print(f)