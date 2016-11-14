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
        objSha = wpa2slow.sha1.Sha1()
        objHmac = wpa2slow.hmac.Hmac(objSha)
        objPrf = wpa2slow.compare.Prf(objHmac)
        
        ptk = 'bf49a95f0494f44427162f38696ef8b6'
        
        data = '0103005ffe01090020000000000000000100000000' + \
        '0000000000000000000000000000000000000000000000000' + \
        '0000000000000000000000000000000000000000000000000' + \
        '00000000000000000000000000000000000000000000000000000000'

        self.assertEqual(objPrf.MIC(ptk, data), '45282522bc6707d6a70a0317a3ed48f0')
        
            
    def test_full(self):
        obj = wpa2slow.handshake.Handshake()
        objSha = wpa2slow.sha1.Sha1()
        objHmac = wpa2slow.hmac.Hmac(objSha)
        objPbkdf2 = wpa2slow.pbkdf2.Pbkdf2()
        objPrf = wpa2slow.compare.Prf(objHmac)
        
        obj.load('test/wpa2.hccap')
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
        if mic == objPrf.toHexString(keymic):
            print 'Key found!'
        else:
            print 'Attempt failed!'
        
        
if __name__ == '__main__':
    unittest.main()