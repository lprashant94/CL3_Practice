
from Crypto.Cipher import DES
from Crypto.Cipher import AES
import hashlib
from Crypto import Random
import codecs

class Encrypt:
    def __init__(self):
        self.iv8 = Random.get_random_bytes(8)
        self.iv16 = Random.get_random_bytes(16)
        self.key8 = '12345678'
        self.key16 = '1234567887654321'


    def HashSHA1(self,message):
        print('\nSHA1 Hash - ')
        obj = hashlib.sha1()
        obj.update(message)
        print(obj.hexdigest())
        return obj.hexdigest()

    def HashMD5(self,message):
        print('\nMD5 Hash - ')
        obj = hashlib.md5()
        obj.update(message)
        print(obj.hexdigest())
        return obj.hexdigest()

    def EncryptDES(self,message):
        print('\nDES Encryption - ')
        des1=DES.new(self.key8 , DES.MODE_CFB, self.iv8)
        cipher = des1.encrypt(message)
        hexlify = codecs.getencoder('hex')
        print(hexlify(cipher)[0])
        return cipher

    def EncryptAES(self,message):
        print('\nAES Encryption - ')
        aes1=AES.new(self.key16 , AES.MODE_CFB, self.iv16)
        cipher = aes1.encrypt(message)
        hexlify = codecs.getencoder('hex')
        print(hexlify(cipher)[0])
        return cipher

    def DecryptAES(self,cipher):
        print('\nAES Decryption - ')
        aes1=AES.new(self.key16 , AES.MODE_CFB, self.iv16)
        text = aes1.decrypt(cipher)
        print(text)
        return text

    def DecryptDES(self,cipher):
        print('\nDES Decryption - ')
        des1=DES.new(self.key8 , DES.MODE_CFB, self.iv8)
        text = des1.decrypt(cipher)
        print(text)
        return text


if __name__ == '__main__':

    e= Encrypt()
    password='Server2003'
    print('***')
    e.DecryptDES(e.EncryptDES(e.HashSHA1('hello1')))
    #e.HashSHA1(password)   
    #e.HashMD5(password)
    #cipher = e.EncryptDES(password)
    #e.DecryptDES(cipher)
    #cipher =e.EncryptAES(password)
    #e.DecryptAES(cipher)
