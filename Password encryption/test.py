import unittest
from encryption import *

class TestEcryption(unittest.TestCase):
    def test_md5(self):
        e= Encrypt()
        res = e.HashMD5('hello1')
        self.assertEqual(res, '203ad5ffa1d7c650ad681fdff3965cd2')

    def test_sha1(self):
        e= Encrypt()
        res = e.HashSHA1('hello1')
        self.assertEqual(res, '88fdd585121a4ccb3d1540527aee53a77c77abb8')

    def test_aes(self):
        e= Encrypt()
        text = 'Hello World'
        res1 = e.EncryptAES(text)
        res2 =e.DecryptAES(res1)
        self.assertEqual(text,res2)

    def test_des(self):
        e= Encrypt()
        text = 'Hello World'
        res1 = e.EncryptDES(text)
        res2 =e.DecryptDES(res1)
        self.assertEqual(text,res2)

if __name__ == '__main__':
    unittest.main()
