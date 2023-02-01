from Crypto.Cipher import DES

key = b'abcdefgh'
plaintext = b'The quick brown fox jumps over the lazy dogs hos'

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)

print(ciphertext)

plain = cipher.decrypt(ciphertext)
print(plain)