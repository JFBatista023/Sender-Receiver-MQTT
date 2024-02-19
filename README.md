# MQTT Sender-Receiver Application

Este é um exemplo simples de uma aplicação Sender-Receiver utilizando MQTT para comunicação entre os Senders e o Receiver.

## Requisitos

- Python 3.10 ou superior

## Configuração do Ambiente

### Criando um Virtual Environment (Ambiente Virtual)

Recomendamos o uso de ambientes virtuais para isolar as dependências do seu projeto. Para criar um ambiente virtual, execute o seguinte comando no terminal:

```bash
python -m venv env
```

### Ativando o Ambiente Virtual

- No Windows:

```bash
env\Scripts\activate
```

- No macOS e Linux:

```bash
source env/bin/activate
```

## Instalando Dependências

Certifique-se de estar no ambiente virtual e execute o seguinte comando para instalar todas as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Criptografia e Banco de Dados

### Criptografia

O sistema utiliza criptografia para garantir a segurança das mensagens trocadas entre os Senders e o Receiver. O algoritmo AES (Advanced Encryption Standard) é empregado para cifrar e decifrar as mensagens. Cada mensagem é criptografada antes de ser enviada e descriptografada pelo Receiver, garantindo a confidencialidade das informações transmitidas.

### Banco de Dados

O histórico de mensagens recebidas é armazenado em um banco de dados SQLite local. Cada mensagem, juntamente com o nome do sender, é registrada no banco de dados. Isso permite ao Receiver manter um registro das mensagens recebidas, facilitando a auditoria e análise posterior.

## Execução

- Abra um terminal e execute o Receiver:

    ```bash
    python receiver.py
    ```

- Abra um ou mais terminais adicionais e execute os Senders:

    ```bash
    python sender.py
    ```

    Siga as instruções para digitar o nome do sender e enviar mensagens.

- Observe as mensagens sendo trocadas e exibidas pelo Receiver.
