from Crypto.Cipher import AES
import rsa

#problema para criar o objeto chave privada
#privkey = rsa.PrivateKey(n, None, d, None, None)
with open('chave_privada.pem', mode='rb') as privatefile:
    keydata = privatefile.read()
print(keydata)
privkey = rsa.PrivateKey.load_pkcs1(keydata, format='PEM')

file = open("chave_aes_cifrada.pem", "r")
chave_aes_cifrada = file.read().encode('utf8')
file.close()

chave_aes_simples = rsa.decrypt(chave_aes_cifrada, privkey)
print(chave_aes_simples)

file = open("texto_cifrado.txt", "r")
texto_cifrado = file.read()
file.close()

obj = AES.new(chave_aes_simples, AES.MODE_ECB)
texto_cifrado = obj.decrypt(texto_cifrado)
print(texto_cifrado)

