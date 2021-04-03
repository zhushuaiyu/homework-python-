# 最大公因数（GCD）和最小公倍数(LCM)
def gcd(a, b):  # find the GCD
    while b != 0:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)


def lcm(a, b):  # find the LCM
    return a * b / gcd(a, b)


if ___name__ = "__main__":
    num1 = input("enter the first number")
    num2 = input("enter the second number")
    try:
        num1 = int(num1)
        num2 = int(num2)
        print("GCD:", end='')
        print(gcd(num1, num2))
        print("LCM:", end='')
        print(lcm(nim1, num2))
    except ValueError:
        print('Input error')
