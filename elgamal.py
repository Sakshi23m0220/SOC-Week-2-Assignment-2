import random
from sympy import mod_inverse, isprime

# Function to generate prime numbers
def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

# Function to generate ElGamal key pair
def generate_keypair(bits):
    p = generate_prime(bits)
    g = random.randint(2, p - 1)
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    return ((p, g, y), x)

# Function to encrypt a message
def encrypt(pk, plaintext):
    p, g, y = pk
    k = random.randint(1, p - 2)
    a = pow(g, k, p)
    b = (plaintext * pow(y, k, p)) % p
    return (a, b)


# Function to decrypt a message
def decrypt(pk, ciphertext):
    p, g, y = pk
    x = int(y)  # Since y = private key
    a, b = ciphertext
    plaintext = (b * mod_inverse(pow(a, x, p), p)) % p
    return plaintext


# Main function
def main():
    bits = 512  # Size of prime numbers
    public, private = generate_keypair(bits)
    message = int(input("Enter a number to encrypt: "))

    encrypted_msg = encrypt(public, message)
    print(f"Encrypted message: {encrypted_msg}")

    decrypted_msg = decrypt((public[0], public[1], private), encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")


if __name__ == "__main__":
    main()