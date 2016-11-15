# -*- coding: utf-8 -*-

from .context import wpa2slow

import unittest
import hmac
import hashlib


class HmacTestSuite(unittest.TestCase):
    """HMAC test cases."""
    
    def test_hmac_slow(self):
        objSha = wpa2slow.Sha1()
        objHmac = wpa2slow.Hmac_Sha1(objSha)
        
        secret = 'Jefe'
        value = 'what do ya want for nothing?'
        self.assertEqual(hmac.new(secret, value, hashlib.sha1).hexdigest(), objHmac.load(secret, value))
        
        secret = 'secret'
        value = 'value'
        self.assertEqual(hmac.new(secret, value, hashlib.sha1).hexdigest(), objHmac.load(secret, value))
        
        
if __name__ == '__main__':
    unittest.main()