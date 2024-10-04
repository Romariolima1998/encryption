from cryptography.fernet import Fernet


def encrypt(text: str) -> dict:

# Geração de uma chave de criptografia
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # Dados a serem criptografados
    data = text.encode()

    # Criptografar os dados
    encrypted_data = cipher_suite.encrypt(data)
    return {
        "encryption_key": key.decode(),
        "encrypted_text": encrypted_data.decode()
    }


def decrypt(encrypt_key: str, encrypted_text: str) -> dict:
    # Usando a mesma chave de criptografia para criar o objeto Fernet
    cipher_suite = Fernet(encrypt_key.encode())

    # Descriptografar os dados
    decrypted_data = cipher_suite.decrypt(encrypted_text.encode())

    return {"decrypted_text": decrypted_data.decode()}


if __name__ == '__main__':
    e = encrypt('criptografando')

    print(e)

    i =decrypt(e['encryption_key'], e["encrypted_text"])
    print(i)