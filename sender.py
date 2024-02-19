import json
import time

import paho.mqtt.publish as publish
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def obter_mensagem():
    return input("Digite a mensagem dinâmica: ")

def criptografar_mensagem(mensagem):
    password = b"senha_super_secreta"
    salt = b"sal_garante_seguranca"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password)

    mensagem_dict = {"sender": sender_name, "mensagem": mensagem}

    cipher = Cipher(algorithms.AES(key), modes.CFB(b'\0' * 16), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(json.dumps(mensagem_dict).encode()) + encryptor.finalize()
    return ciphertext


def enviar_mensagem(sender_name):
    while True:
        mensagem = obter_mensagem()
        mensagem_cifrada = criptografar_mensagem(mensagem)

        publish.single(topic, payload=mensagem_cifrada, hostname=broker_address)
        print(f"Mensagem criptografada enviada.")
        time.sleep(5)

if __name__ == "__main__":
    sender_name = input("Digite o nome do sender: ")
    topic = "topic/messages"
    broker_address = "mqtt.eclipseprojects.io"

    enviar_mensagem(sender_name)
