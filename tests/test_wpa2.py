# -*- coding: utf-8 -*-

from .context import wpa2slow

import unittest
import hmac
import hashlib


class Wpa2TestSuite(unittest.TestCase):
    """WPA2 test cases."""
    
    def test_wpa2_slow(self):
        #Todo: What does this even do!
        assert True
        
        
    def test_mic_slow(self):
        objSha = wpa2slow.Sha1()
        objHmac = wpa2slow.Hmac(objSha)
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
        objHmac = wpa2slow.Hmac(objSha)
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
        
        print 'ssid:        ' + objPrf.toHexString(ssid)
        print 'mac1:        ' + objPrf.toHexString(mac1)
        print 'mac2:        ' + objPrf.toHexString(mac2)
        print 'nonce1:      ' + objPrf.toHexString(nonce1)
        print 'nonce2:      ' + objPrf.toHexString(nonce2)
        print 'eapol:       ' + objPrf.toHexString(eapol[0:eapol_size])
        print 'eapol_size:  ' + str(eapol_size)
        print 'keymic:      ' + objPrf.toHexString(keymic)
                
        mk = 'dictionary'
        print 'mk:          ' + mk
        
        pmk = objPbkdf2.run(objHmac, mk, ssid)
        print 'pmk:         ' + pmk
        
        #This is so weird because of my terrible inconsistent binary types
        #     see https://github.com/JarrettR/WPA-Slowed-Down/issues/2
        ptk = objPrf.PRF(pmk, objPrf.toHexString(mac1), objPrf.toHexString(mac2), objPrf.toHexString(nonce1), objPrf.toHexString(nonce2))
        print 'ptk:         ' + ptk
        
        mic = objPrf.MIC(ptk, objPrf.toHexString(eapol[0:eapol_size]))
        print 'MIC:         ' + mic
        print 'Expected:    ' + objPrf.toHexString(keymic)

        self.assertEqual(mic, objPrf.toHexString(keymic))

        
if __name__ == '__main__':
    unittest.main()