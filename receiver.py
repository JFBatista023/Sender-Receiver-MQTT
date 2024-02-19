import json
import sqlite3

import paho.mqtt.client as mqtt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

broker_address = "mqtt.eclipseprojects.io"
port = 1883
topic = "topic/messages"

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

def descriptografar_mensagem(ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'\0' * 16), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    decrypted_string = decrypted_data.decode()

    mensagem_dict = json.loads(decrypted_string)

    sender_name = mensagem_dict["sender"]
    mensagem = mensagem_dict["mensagem"]

    return sender_name, mensagem

def on_message(client, userdata, msg):
    sender_name, mensagem_decifrada = descriptografar_mensagem(msg.payload)
    
    print(f"Mensagem de {sender_name}: {mensagem_decifrada}")

    conn = sqlite3.connect('mensagens.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS mensagens (sender TEXT, mensagem TEXT)')
    cursor.execute('INSERT INTO mensagens (sender, mensagem) VALUES (?, ?)', (sender_name, mensagem_decifrada))
    conn.commit()
    conn.close()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect(broker_address, port, 60)
client.subscribe(topic + "/#")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Programa encerrado pelo usuário.")
    client.disconnect()
