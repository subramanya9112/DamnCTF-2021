import string

with open("flags.txt", "r") as txt_file:
    lines = txt_file.readlines()

for line in lines:
    line = line.strip()
    for letter in string.printable:
        b = bytearray.fromhex(line).decode('utf-8')
        if "dam" in "".join([chr(ord(val) ^ ord(letter)) for val in b]):
            print(letter)
            print(line)
            print("".join([chr(ord(val) ^ ord(letter)) for val in b]))
