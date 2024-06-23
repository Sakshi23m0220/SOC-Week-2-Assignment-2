def extended_gcd(a, b):
    """Extended Euclidean algorithm."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def main():
    A = int(input("Enter the value for A: "))
    B = int(input("Enter the value for B: "))
    C = int(input("Enter the value for C: "))
    D = int(input("Enter the value for D: "))

    gcd_ab, x_ab, y_ab = extended_gcd(A, B)
    gcd_abc, x_abc, y_abc = extended_gcd(gcd_ab, C)

    if D % gcd_abc != 0:
        print("No solution exists")
        return

    # Solution exists, now find the specific solution
    x_abc *= D // gcd_abc
    y_abc *= D // gcd_abc
    z_abc = D // gcd_abc

    print(f"The solutions for aA + bB + cC = D are: a = {x_ab}, b = {y_ab}, c = {y_abc}")

if __name__ == "__main__":
    main()

