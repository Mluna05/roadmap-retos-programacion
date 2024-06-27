"""Recursividad"""

#No Recursivo
def recursividad(number: int):
    for i in range(101):
        print(number - i)
        if i == 100:
            break

print(recursividad(100))

#Recursivo
def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number-1)

countdown(10)

"""Extra"""

def factorial(number: int):
    if number <= 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(4))


def fibonacci(number: int):
    if number <= 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(6))
