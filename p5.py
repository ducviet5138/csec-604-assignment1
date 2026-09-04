def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(gcd(188,220))
    print(gcd(300,142))