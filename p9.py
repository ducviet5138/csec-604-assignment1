from p5 import gcd

def euler_totient(n):
    result = 0

    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            result += 1

    return result


if __name__ == "__main__":
    print(f"Phi(29): {euler_totient(29)}")
    print(f"Phi(32): {euler_totient(32)}")
