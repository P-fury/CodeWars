def product_fib(_prod):
    a, b = 0, 1
    while True:
        if a * b == _prod:
            return [a, b, True]
        elif a * b > _prod:
            return [a, b, False]
        a, b = b, a + b

print(product_fib(4353))



