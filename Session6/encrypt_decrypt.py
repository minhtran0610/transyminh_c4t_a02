string = input("Enter a string: ")
shift = int(input("Enter Caesar shift: "))
char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

enc = ''
dec = ''

def encrypt(str, n):
    global enc
    for i in str:
        if i in char:
            check = ord(i) + shift
            if check >= 97 and check <= 122 or check >= 65 and check <= 90:
                new = check
            elif check > 122 or 90 < check <= 96:
                new = check - 26
            new2 = chr(new)
            enc += new2
        else:
            enc += i
    return enc

def decrypt(str, n):
    global dec
    for i in str:
        if i in char:
            check = ord(i) - shift
            if check >= 97 and check <= 122 or check >= 65 and check <= 90:
                new = check
            elif check < 65 or 90 < check <= 96:
                new = check + 26
            new2 = chr(new)
            dec += new2
        else:
            dec += i
    return dec

print(encrypt(string, shift))
print(decrypt(enc, shift))

