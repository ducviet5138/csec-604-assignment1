def factorize_prime(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

if __name__ == "__main__":
    print(f"Prime factors of 25: {factorize_prime(25)}")
    print(f"Prime factors of 49: {factorize_prime(49)}")
    print(f"Prime factors of 82: {factorize_prime(82)}")
    print(f"Prime factors of 1000: {factorize_prime(1000)}")
    print(f"Prime factors of 9999: {factorize_prime(9999)}")

