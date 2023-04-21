# ask the user for input message and key
message = input("MESSAGE (input in uppercase letters, no spaces): ")
key = input("KEYWORD (input in uppercase letters, no spaces): ")
# convert message and key to lists of numbers 0-25 since A-Z is in 65-95 using ord(c)
message_num = [ord(c) - 65 for c in message]
key_num = [ord(c) - 65 for c in key]
# repeating the key until its the same length of the message
key_rep = []
key_index = 0
for i in range(len(message)):
    key_rep.append(key_num[key_index])
    key_index = (key_index + 1) % len(key)
# encrypt by adding message and key, take the result and use mod 26
# convert ciphertext numbers to letters
# print the output