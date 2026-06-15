from mymodule import calculate_average as c_a
from random import randint

a = [randint(1, 100) for i in range(100)]

print("Среднее значение списка:", c_a(a))