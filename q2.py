from Crypto.Cipher import AES
import rsa

#building the rsa pubkey object
file = open("chave_publica.pem", "r")
n = int(file.readline())
e = int(file.readline())
file.close()
pubkey = rsa.PublicKey(n, e)

#getting the user simple text file
#file_name = input("Informe o nome do arquivo que deseja cifrar\n")
file_name = "texto_simples.txt"
simple_text = open(file_name, "r").read()

#aes key simple
simple_aes_key = '0123456789abcdef'
cipher_aes_key = rsa.encrypt(simple_aes_key.encode("utf8"), pubkey)

file = open("chave_aes_cifrada.pem", "w")
file.write(str(cipher_aes_key))
file.close()

obj = AES.new(simple_aes_key, AES.MODE_ECB)
texto_cifrado = obj.encrypt(simple_text)
print(texto_cifrado)

file = open("texto_cifrado.txt", "w")
file.write(str(texto_cifrado))
file.close()