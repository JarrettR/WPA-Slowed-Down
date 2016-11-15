# -*- coding: utf-8 -*-

from .context import wpa2slow

import unittest
import hmac
import hashlib
from binascii import a2b_hex, b2a_hex 


class Wpa2TestSuite(unittest.TestCase):
    """WPA2 test cases."""
    
    def test_wpa2_slow(self):
        #Todo: What does this even do!
        assert True
        
        
    def test_mic_slow(self):
        objSha = wpa2slow.Sha1()
        objHmac = wpa2slow.Hmac_Sha1(objSha)
        objPrf = wpa2slow.Prf(objHmac)
        
        ptk = '5e9805e89cb0e84b45e5f9e4a1a80d9d'
        
        data = '0103007502010a0000000000000000000' + \
            '1e8dfa16b8769957d8249a4ec68d2b7641d3' + \
            '782162ef0dc37b014cc48343e8dd20000000' + \
            '000000000000000000000000000000000000' + \
            '000000000000000000000000000000000000' + \
            '00000000000000000001630140100000fac0' + \
            '40100000fac040100000fac022800'
            
        mic = '56f98b98da5d55e3be396b43c7eb012a'

        self.assertEqual(objPrf.MIC(ptk, data), mic)
        
            
    def test_full_slow(self):
        obj = wpa2slow.Handshake()
        objSha = wpa2slow.Sha1()
        objHmac = wpa2slow.Hmac_Sha1(objSha)
        objPbkdf2 = wpa2slow.Pbkdf2()
        objPrf = wpa2slow.Prf(objHmac)
        
        obj.load('tests/data/wpa2.hccap')
        ssid = obj.ssid
        mac1 = obj.mac1
        mac2 = obj.mac2
        nonce1 = obj.nonce1
        nonce2 = obj.nonce2
        eapol = obj.eapol
        eapol_size = obj.eapol_size
        keymic = obj.keymic
        
        print 'ssid:        ' + b2a_hex(ssid)
        print 'mac1:        ' + b2a_hex(mac1)
        print 'mac2:        ' + b2a_hex(mac2)
        print 'nonce1:      ' + b2a_hex(nonce1)
        print 'nonce2:      ' + b2a_hex(nonce2)
        print 'eapol:       ' + b2a_hex(eapol[0:eapol_size])
        print 'eapol_size:  ' + str(eapol_size)
        print 'keymic:      ' + b2a_hex(keymic)
                
        mk = 'dictionary'
        print 'mk:          ' + mk
        
        pmk = objPbkdf2.run(objHmac, mk, ssid)
        print 'pmk:         ' + pmk
        
        #This is so weird because of my terrible inconsistent binary types
        #     see https://github.com/JarrettR/WPA-Slowed-Down/issues/2
        ptk = objPrf.PRF(pmk, b2a_hex(mac1), b2a_hex(mac2), b2a_hex(nonce1), b2a_hex(nonce2))
        print 'ptk:         ' + ptk
        
        mic = objPrf.MIC(ptk, b2a_hex(eapol[0:eapol_size]))
        print 'MIC:         ' + mic
        print 'Expected:    ' + b2a_hex(keymic)

        self.assertEqual(mic, b2a_hex(keymic))

        
if __name__ == '__main__':
    unittest.main()