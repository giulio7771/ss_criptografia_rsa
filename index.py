
#q1 
import rsa
(pubkey, privkey) = rsa.newkeys(512, poolsize=8)
print("\n\nChave pública\n\nMódulo:{}\n\nExpoente e:{}".format(pubkey.n, pubkey.e))
print("\n\nChave privada\n\nMódulo:{}\n\nExpoente d:{}".format(privkey.n, privkey.d))

file = open("chave_publica.pem", "w")
file.write("{}\n{}".format(pubkey.n, pubkey.e))
file.close()

file = open("chave_privada.pem", "w")
file.write("{}\n{}".format(pubkey.n, privkey.d))
file.close()

#q2

#getting the user simple text file
#file_name = input("Informe o nome do arquivo que deseja cifrar\n")
file_name = "texto_simples.txt"
simple_text = open(file_name, "r").read()

from Crypto.Cipher import AES
simple_aes_key = '0123456789abcdef'
cipher_aes_key = rsa.encrypt(simple_aes_key.encode("utf8"), pubkey)

file = open("chave_aes_cifrada.pem", "w")
file.write(str(cipher_aes_key))
file.close()

obj = AES.new(simple_aes_key, AES.MODE_ECB)
texto_cifrado = obj.encrypt(simple_text)
print("Texto cifrado:\n")
print(texto_cifrado)

file = open("texto_cifrado.txt", "w")
file.write(str(texto_cifrado))
file.close()

#q3
chave_aes_simples = rsa.decrypt(cipher_aes_key, privkey)
obj = AES.new(chave_aes_simples, AES.MODE_ECB)
texto_simples = obj.decrypt(texto_cifrado)
print("Texto simples:\n")
print(texto_simples)


