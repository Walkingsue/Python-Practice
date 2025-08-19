from random import random
import string
import random

char = string.ascii_letters + string.digits + string.punctuation
char = list(char)
key = char.copy()

random.shuffle(key)

plain_text = input("Enter the text to encrypt: ")
cipher_text = ""
for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]

print(f" original text: {plain_text}")
print(f" encrypted text: {cipher_text}")

cipher_text = input("Enter the encrypt message: ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]

print(f" encrypted text: {cipher_text}")
print(f" original text: {plain_text}")