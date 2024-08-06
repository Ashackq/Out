import random


def is_prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def generate_prime(bits):
    while True:
        num = random.randrange(2 ** (bits - 1) + 1, 2**bits - 1)
        if num % 2 == 0:
            num += 1
        if is_prime_fermat(num):
            return num


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_d(e, phi):
    k = 0
    while True:
        d = (1 + k * phi) // e
        if (1 + k * phi) % e == 0:
            return d
        k += 1


def generate_keypair(bits):
    # p = generate_prime(bits // 2)
    # q = generate_prime(bits // 2)
    p = int(input("Give p"))
    q = int(input("Give q"))
    print(f"P = {p} Q = {q} \n")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = find_d(e, phi)
    print(f"Public Key {(e,n)} Private Key {(d,n)}")
    return ((e, n), (d, n))


def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = []
    for char in plaintext:
        ciphertext.append(pow(ord(char), e, n))
    return ciphertext


def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = ""
    for cipher in ciphertext:
        plaintext += chr(pow(cipher, d, n))
    return plaintext


public_key, private_key = generate_keypair(2048)
message = "15"
ciphertext = encrypt(message, public_key)
print(ciphertext)
decrypted_message = decrypt(ciphertext, private_key)
print(decrypted_message)
