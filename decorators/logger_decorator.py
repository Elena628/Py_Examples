# Напишите декоратор с именем "logger", который будет записывать информацию о вызове функции в файл. 
# Декоратор должен записывать переданные аргументы и 
# результат выполнения функции в формате "[аргументы] -> результат" в файл с именем "log.txt". 
# Каждый вызов функции должен быть записан на новой строке.

def logger(func):

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        args_str = ", ".join(map(str, args))
        with open("decorators/log.txt", "a") as f:
            f.write(f"{args_str} ---> {res}\n")
        return res

    return wrapper

@logger
def square(x):
    return x ** 2


for i in range(15):
    square(i)
    