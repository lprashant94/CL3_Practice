import unittest
from dsa import * 


class dsatesting(unittest.TestCase):
    def test_dsa(self):
        print('abcdd')
        d=DSA(797,199,81)
        d.GenerateKeyPair()
        (r,s)=d.Signature("Hello world")
        status=d.verify("Hello world",r,s)
        self.assertEqual(status,True)
    def test_negative(self):
        d=DSA(797,199,81)
        d.GenerateKeyPair()
        (r,s)=d.Signature("Hello world")
        status=d.verify("Hello World",r,s)
        self.assertNotEqual(status,True)

if __name__=='__main__':
    unittest.main()
        
