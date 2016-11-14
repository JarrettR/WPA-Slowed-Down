# -*- coding: utf-8 -*-

from .context import wpa2slow

import unittest
import hmac
import hashlib


class Pbkdf2TestSuite(unittest.TestCase):
    """PBKDF2 test cases."""
    
    def test_pbkdf2_slow(self):
        objSha = wpa2slow.sha1.Sha1()
        objHmac = wpa2slow.hmac.Hmac(objSha)
        objPbkdf2 = wpa2slow.pbkdf2.Pbkdf2()
        secret = 'Jefe'
        value = 'what do ya want for nothing?'
        secret = 'secret'
        value = 'value'
        
        # 64 hex digits / 32 bytes / 256 bits
        print objPbkdf2.run(objHmac, secret, value)
        
        #Grab comparison constant for test case
        assert False
        
        
if __name__ == '__main__':
    unittest.main()