import hashlib

"""
hash function
input data into a fixed-length output 
collision attacks, where two different inputs produce the same hash
128-bit hash (32 hexadecimal characters)
"""


def generate_md5_hash(message):
    md5 = hashlib.md5()
    md5.update(message.encode("utf-8"))
    return md5.hexdigest()


def verify_message_integrity(original_message, received_message):
    original_hash = generate_md5_hash(original_message)
    received_hash = generate_md5_hash(received_message)
    print(original_hash)
    # 737aa7c8 358cfc6b caca906a e21183bd
    if original_hash == received_hash:
        print("message  not  altered.")
    else:
        print("message altered.")


original_message = input("Enter original message")
received_message = input("Enter recieved message")
verify_message_integrity(original_message, received_message)
