# Rivest-Shamir-Adleman
"""
asymmetric
data transmission and digital signatures
difficulty of factoring large prime numbers

"""
import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_d(e, phi):
    k = 1
    while True:
        d = (1 + k * phi) // e
        if (1 + k * phi) % e == 0:
            return d
        k += 1


def generate_keypair(p, q):
    n = p * q
    # Euler's totient
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = find_d(e, phi)

    print(f"Public Key: (e={e}, n={n})")
    print(f"Private Key: (d={d}, n={n})")

    return ((e, n), (d, n))


def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = pow(plaintext, e, n)
    return ciphertext


def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext


p = 3
q = 11
message = 15


public_key, private_key = generate_keypair(p, q)


ciphertext = encrypt(message, public_key)
print("Ciphertext:", ciphertext)


decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted message:", decrypted_message)
