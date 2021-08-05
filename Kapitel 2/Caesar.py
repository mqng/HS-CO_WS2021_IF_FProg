def caesar_encode(src, dist):
    cipher = ""
    for c in src:
        if (c.isupper()):
            a = ord('A')
            z = ord('Z')
            cipher += chr(((ord(c) - a + dist) % 26) + a)

        elif (c == " "):
            cipher += c

        elif (c.islower()):
            a = ord('a')
            z = ord('z')
            cipher += chr(((ord(c) - a + dist) % 26) + a)

    return cipher

def caeser_decode(src, dist):
    return caesar_encode(src, -dist)

print("Plaintext Message:")
src = input()
print("Distance:")
dist = int(input())

print("Original message:", src)
print("Ciphertext:", caesar_encode(src, dist))

print("\nInput cipher:")
src = input()
print("Distance:")
dist = int(input())

print("Original message:", caeser_decode(src, dist))
