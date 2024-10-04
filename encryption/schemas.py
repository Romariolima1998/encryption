from pydantic import BaseModel

class EncryptInput(BaseModel):
    text: str

class EncryptOutput(BaseModel):
    encryption_key: str
    encrypted_text: str


class DecriptInput(BaseModel):
    encryption_key: str
    encrypted_text: str

class DecriptOutput(BaseModel):
    decrypted_text: str