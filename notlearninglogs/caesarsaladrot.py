""" caesar cipher """


text = input().strip()
k = int(input())

encrypted_text = ""

for char in text:

    shifted_pos = (ord(char) - ord('a') + k) % 26
    encrypted_text += chr(shifted_pos + ord('a'))

print(encrypted_text)
