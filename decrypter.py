import pyaes

def decrypt_file(encrypted_file_name, key):
    with open(encrypted_file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)

    original_file_name = encrypted_file_name.replace(".ransomwaretroll", "")
    with open(original_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    with open(original_file_name, "r") as file:
        print(f"Conteúdo descriptografado: {file.read()}")

if __name__ == "__main__":
    key = b"testeransomwares"
    encrypted_file_name = "teste.txt.ransomwaretroll"

    decrypt_file(encrypted_file_name, key)
