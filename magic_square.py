import math


def encrypt_text(text, magic_square):
    encrypted_text = ""

    for i in range(size):
        for j in range(size):
            if magic_square[i][j] <= n:
                encrypted_text += text[magic_square[i][j] - 1]
            else:
                encrypted_text += ''
    
    return encrypted_text


def decrypt_text(text, magic_square):
    decrypted_text = ""
    index = 0
    for i in range(size):
        for j in range(size):
            if magic_square[i][j] <= n:
                decrypted_text += text[magic_square[i][j] - 1]
            else:
                decrypted_text += ''
            index += 1
            
            if index == n:
                return decrypted_text
    
    return decrypted_text



with open("G:\input.txt", "r") as f:
    text = f.read()
print(text)

n = len(text)
size = math.ceil(math.sqrt(n))
magic_square = [[0 for _ in range(size)] for _ in range(size)]
    
x, y = 0, size // 2
for i in range(1, size * size + 1):
    magic_square[x][y] = i
    x -= 1
    y += 1
        
    if i % size == 0:
        x += 2
        y -= 1
    elif x < 0:
        x = size - 1
    elif y == size:
        y = 0


print(magic_square)
encrypted_text = encrypt_text(text, magic_square)
print(encrypted_text)

with open("G:\output.txt", "w") as f:
    f.write(encrypted_text)

reversed_decrypted_text = decrypt_text(encrypted_text, magic_square)
decrypted_text = reversed_decrypted_text[::-1]
print(decrypted_text)

with open("G:\output2.txt", "w") as f:
    f.write(decrypted_text)
