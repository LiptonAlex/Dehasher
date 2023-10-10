import hashlib

hashed_message = ""

message_list = "ignis-100K.txt"

for message in open(message_list, 'r').readlines():
    hashed = hashlib.sha3_256(message.strip().encode()).hexdigest()
    if hashed == hashed_message:
        print(f' the message is {message}')