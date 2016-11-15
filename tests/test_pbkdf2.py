# -*- coding: utf-8 -*-

from .context import wpa2slow

import unittest
import hmac
import hashlib


class Pbkdf2TestSuite(unittest.TestCase):
    """PBKDF2 test cases."""
    
    def test_pbkdf2_slow(self):
        objSha = wpa2slow.Sha1()
        objHmac = wpa2slow.Hmac_Sha1(objSha)
        objPbkdf2 = wpa2slow.Pbkdf2()
        secret = 'Jefe'
        value = 'what do ya want for nothing?'
        secret = 'secret'
        value = 'value'
        
        # 64 hex digits / 32 bytes / 256 bits
        out = objPbkdf2.run(objHmac, secret, value)
        
        pbkdf2 = '75b5b11e4b8ac91b7542c62302e5ce4373591285923d496d082c6e2c744e0717'
        
        self.assertEqual(out, pbkdf2)
        
        
if __name__ == '__main__':
    unittest.main()