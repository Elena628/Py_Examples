def factorial(n):
    count = 1
    current = 1
    while True:
        if current * count > n:
            break
        current *= count
        count += 1 
        yield current

for f in factorial(150):
    print(f)
