def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


x = int(10)
result = fibonacci(x-1)

print(f'O fibonacci de {x} é {result}')
