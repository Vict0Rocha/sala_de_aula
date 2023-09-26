# def fatorial(num):
#     if num == 1:
#         return 1
#     return num * fatorial(num-1)


# print(fatorial(5))

def func(qtd: int) -> int:
    if qtd <= 1:
        return print("Hello, World!")
    print("Hello, World!")
    return func(qtd - 1)


if __name__ == "__main__":
    # print("Hello, world!")
    func(10)
