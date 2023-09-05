def fatorial(num):
    if num == 1:
        return num
    return num * fatorial(num-1)


print(fatorial(5))