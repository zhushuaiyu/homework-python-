def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


num1 = int(input("Enter an integer"))
if num1 <= 0:
    print("Error")
else:
    print("Fibonacci number:")
    print(fib(num1))
