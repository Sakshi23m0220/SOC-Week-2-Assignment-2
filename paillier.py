import random
from sympy import mod_inverse, gcd

# Function to generate prime numbers
def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

# Function to generate Paillier key pair
def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    nsquare = n * n
    g = n + 1
    lambda_ = (p - 1) * (q - 1)
    mu = mod_inverse(lambda_, n)
    return ((n, g), (lambda_, mu))

# Function to encrypt a message
def encrypt(pk, plaintext):
    n, g = pk
    nsquare = n * n
    r = random.randint(1, n - 1)
    while gcd(r, n) != 1:
        r = random.randint(1, n - 1)
    c = (pow(g, plaintext, nsquare) * pow(r, n, nsquare)) % nsquare
    return c


# Function to decrypt a message
def decrypt(pk, ciphertext):
    lambda_, mu = pk
    n = int(mu)  # Since mu = lambda_
    nsquare = n * n
    x = pow(ciphertext, lambda_, nsquare) - 1
    plaintext = ((x // n) * mu) % n
    return plaintext


# Main function
def main():
    bits = 512  # Size of prime numbers
    public, private = generate_keypair(bits)
    message = int(input("Enter a number to encrypt: "))

    encrypted_msg = encrypt(public, message)
    print(f"Encrypted message: {encrypted_msg}")

    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")


if __name__ == "__main__":
    main()