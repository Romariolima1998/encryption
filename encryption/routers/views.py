from fastapi import APIRouter

from encryption.schemas import EncryptInput, EncryptOutput, DecriptInput, DecriptOutput
from encryption.utils.encryption import encrypt, decrypt


encryption = APIRouter(prefix='/encryption', tags=['encryption'])

@encryption.post('/encrypt', response_model=EncryptOutput)
def encrypt_view(dados: EncryptInput):
    return encrypt(dados.text)


@encryption.post('/decript', response_model=DecriptOutput)
def decrypt_view(dados: DecriptInput):
    return decrypt(dados.encryption_key, dados.encrypted_text)
