def gcd_on(a, b):
    """Calculate GCD using O(N) method."""
    if b > a:
        a, b = b, a
    gcd = 1
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def gcd_euclidean(a, b):
    """Calculate GCD using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    gcd1 = gcd_on(num1, num2)
    gcd2 = gcd_euclidean(num1, num2)

    print(f"The GCD of {num1} and {num2} using O(N) method is: {gcd1}")
    print(f"The GCD of {num1} and {num2} using the Euclidean method is: {gcd2}")

if __name__ == "__main__":
    main()
