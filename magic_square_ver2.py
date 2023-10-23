def encrypt_text(text):
    magic_square = [[17, 24, 1, 8, 15],
                    [23, 5, 7, 14, 16],
                    [4, 6, 13, 20, 22],
                    [10, 12, 19, 21, 3],
                    [11, 18, 25, 2, 9]]

    encrypted_text = ""

    for char in text:
        if char.isalpha(): 
            char_index = ord(char.lower()) - ord('a')
            row = char_index // 5
            column = char_index % 5
            encrypted_text += str(magic_square[row][column])
        else:
            encrypted_text += char  

    return encrypted_text


def decrypt_text(encrypted_text):
    magic_square = [[17, 24, 1, 8, 15],
                    [23, 5, 7, 14, 16],
                    [4, 6, 13, 20, 22],
                    [10, 12, 19, 21, 3],
                    [11, 18, 25, 2, 9]]
    
    decrypted_text = ""

    for num_str in encrypted_text:
        if num_str.isdigit():  
            number = int(num_str)
            for row in magic_square:
                if number in row:
                    column = row.index(number)
                    char_index = (row.index(number) + magic_square.index(row) * 5)
                    decrypted_text += chr(char_index + ord('a'))
                    break
        else:
            decrypted_text += num_str 

    return decrypted_text


with open("G:\input.txt", "r") as f:
    text = f.read()
print(text)

encrypted_text = encrypt_text(text)
print(encrypted_text)

with open("G:\output.txt", "w") as f:
    f.write(encrypted_text)

reversed_decrypted_text = decrypt_text(encrypted_text)
decrypted_text = reversed_decrypted_text[::-1]
print(decrypted_text)

with open("G:\output2.txt", "w") as f:
    f.write(decrypted_text)