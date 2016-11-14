# -*- coding: utf-8 -*-

from .context import wpa2slow

import unittest
import hmac
import hashlib
import binascii


class HandshakeTestSuite(unittest.TestCase):
    """Handshake test cases."""
    
    def test_handshake_load(self):
        obj = wpa2slow.Handshake()
        
        obj.load('tests/data/wpa2.hccap')
        
        ssid = 'linksys'
        mac1 = '000b86c2a485'
        mac2 = '0013ce5598ef'
        #nonce1 = ''
        nonce2 = 'ae12a150652e9bc22063720c5081e9eb74077fb19fffe871dc4ca1e6f448af85'
        #eapol = ''
        eapol_size = 121
        keymic = '56f98b98da5d55e3be396b43c7eb012a'
        
        self.assertEqual(ssid, obj.ssid)
        self.assertEqual(mac1, binascii.hexlify(obj.mac1))
        self.assertEqual(mac2, binascii.hexlify(obj.mac2))
        self.assertEqual(nonce2, binascii.hexlify(obj.nonce2))
        self.assertEqual(eapol_size, obj.eapol_size)
        self.assertEqual(keymic, binascii.hexlify(obj.keymic))
        
        
        
if __name__ == '__main__':
    unittest.main()
