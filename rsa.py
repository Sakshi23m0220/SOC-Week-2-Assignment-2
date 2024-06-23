import random
from sympy import isprime, mod_inverse

# Function to generate prime numbers
def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

# Function to generate RSA key pair
def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Commonly used prime exponent
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

# Function to encrypt a message
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


# Function to decrypt a message
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)


# Main function
def main():
    bits = 1024  # Size of prime numbers
    public, private = generate_keypair(bits)
    message = input("Enter a message to encrypt: ")

    encrypted_msg = encrypt(public, message)
    print(f"Encrypted message: {encrypted_msg}")

    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")


if __name__ == "__main__":
    main()