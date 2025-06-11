from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64




def gerar_par_chaves(caminho_privada="chave_privada.pem", caminho_publica="chave_publica.pem"):
    chave = RSA.generate(2048)

    chave_privada = chave.export_key()
    with open(caminho_privada, "wb") as f:
        f.write(chave_privada)

    chave_publica = chave.publickey().export_key()
    with open(caminho_publica, "wb") as f:
        f.write(chave_publica)


def carregar_chave_publica(caminho):
    with open(caminho, "rb") as f:
        chave = RSA.import_key(f.read())
    return chave


def carregar_chave_privada(caminho):
    with open(caminho, "rb") as f:
        chave = RSA.import_key(f.read())
    return chave


def criptografar_texto(texto, chave_publica):
    cipher = PKCS1_OAEP.new(chave_publica)
    texto_bytes = texto.encode('utf-8')
    texto_criptografado = cipher.encrypt(texto_bytes)
    return base64.b64encode(texto_criptografado).decode('utf-8')


def descriptografar_texto(texto_criptografado_base64, chave_privada):
    cipher = PKCS1_OAEP.new(chave_privada)
    dados = base64.b64decode(texto_criptografado_base64)
    texto = cipher.decrypt(dados)
    return texto.decode('utf-8')