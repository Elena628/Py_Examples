def fib(n):
    prev = 0
    cur = 1
    while prev < n:
        yield prev
        result = prev + cur
        prev, cur = cur, result

for f in fib(10):
    print(f)