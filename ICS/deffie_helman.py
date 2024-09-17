import random

"""
symmetric encryption
share a symmetric key
difficulty of the inverse modulus problem
SSL/TLS

"""


def power_mod(base, exp, mod):
    return pow(base, exp, mod)


def diffie_hellman():
    # prime number (p) and base (g)
    # private key (a, b)
    # A = (g^a) % p
    # B = (g^b) % p
    # S_A = (B^a) % p
    # S_B = (A^b) % p

    p = 23
    g = 5

    print(f"Publicly known values: Prime (p) = {p}, Base (g) = {g}")

    a = random.randint(1, p - 1)
    b = random.randint(1, p - 1)

    print(f"A's private key (a): {a}")
    print(f"B's private key (b): {b}")

    A = power_mod(g, a, p)
    print(f"A's public value (A): {A}")

    B = power_mod(g, b, p)
    print(f"B's public value (B): {B}")
    S_A = power_mod(B, a, p)
    print(f"A's shared secret key (S_A): {S_A}")

    S_B = power_mod(A, b, p)
    print(f"B's shared secret key (S_B): {S_B}")

    # If both keys are the same, the key exchange was successful
    if S_A == S_B:
        print("Key exchange successful! Shared secret key:", S_A)
    else:
        print("Key exchange failed. Keys do not match.")


diffie_hellman()
