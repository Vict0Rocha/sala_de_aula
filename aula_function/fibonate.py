t1 = 0
t2 = 1 
n = 12
# fib = t1 + t2
inicio = 3

while inicio <= n:
    fib = t1 + t2
    t1 = t2
    t2 = fib
    print(fib)
    inicio += 1