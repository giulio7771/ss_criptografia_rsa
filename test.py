import rsa
(pubkey, privkey) = rsa.newkeys(512, poolsize=8)

print(privkey.save_pkcs1())
