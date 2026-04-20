#Caesar Cipher
#take an input string, shift the characters by three letters, 
#then output the resulting string


def decrypt(text, shift):
    result = ""
    
    for l in range(len(text)):
        char = text[l]
        if (char.isupper()):
            result += chr((ord(char) - shift -65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)

    return result


text =  "m[xay_\llvk\cmxw"
shift = -26

while shift <=27:

    print("Shift factor: " + str(shift), ": Decrypted Message: " + decrypt(text, shift))
    print()
    shift+=1


