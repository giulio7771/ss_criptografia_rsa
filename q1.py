import rsa
(pubkey, privkey) = rsa.newkeys(512, poolsize=8)
print("\n\nChave pública\n\nMódulo:{}\n\nExpoente e:{}".format(pubkey.n, pubkey.e))
print("\n\nChave privada\n\nMódulo:{}\n\nExpoente d:{}".format(privkey.n, privkey.d))

file = open("chave_publica.pem", "w")
file.write("{}\n{}".format(pubkey.n, pubkey.e))
file.close()

file = open("chave_privada.pem", "wb")
file.write(pubkey.save_pkcs1())
file.close()
