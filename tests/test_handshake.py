# -*- coding: utf-8 -*-

from .context import wpa2slow

import unittest
import hmac
import hashlib


class HandshakeTestSuite(unittest.TestCase):
    """Handshake test cases."""
    
    def test_handshake_load(self):
        obj = wpa2slow.handshake.Handshake()
        
        obj.load('test/wpa2.hccap')
        ssid = obj.ssid
        mac1 = obj.mac1
        mac2 = obj.mac2
        nonce1 = obj.nonce1
        nonce2 = obj.nonce2
        eapol = obj.eapol
        eapol_size = obj.eapol_size
        keymic = obj.keymic
        
        print ssid
        print mac1
        print mac2
        print nonce1
        print nonce2
        print eapol
        print eapol_size
        print keymic
        
        
if __name__ == '__main__':
    unittest.main()
