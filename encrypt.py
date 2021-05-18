char = 'qwertyuiopasdfghjklzxcvbnm'
enc_str = input("Enter a string: ").lower()

enc = ''
dec = ''
shift = int(input("Enter Caesar Shift: "))
def encrypt(enc_str, shift):
    global enc
    for i in enc_str:
        if i in char:
            check = ord(i) + shift
            if check > 97 and check < 122:
                new = check
            if check > 122:
                new = check - 26
            new2 = chr(new)
            enc = enc + new2
        elif i not in char:
            enc = enc + i
    return enc 

def decrypt(enc, shift):
    global dec
    for i in enc_str:
        if i in char:
            check = ord(i) - shift
            if check > 97 and check < 122:
                old = check
            if check < 122:
                old = check + 26
            old2 = chr(old)
            dec += old2
        elif i not in char:
            enc = enc + i
    return dec

print(encrypt(enc_str, shift))
print(decrypt(enc_str, shift))