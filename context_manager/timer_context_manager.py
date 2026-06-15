import time

class timer():
    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc, tb):
        self.end = time.perf_counter()
        result = self.end - self.start
        print(f"{result:.6f}")

a = []

with timer():
    time.sleep(10)
    for i in range(10000):
        a.append(i)
