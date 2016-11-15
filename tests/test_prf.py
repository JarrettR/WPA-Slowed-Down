# -*- coding: utf-8 -*-

from .context import wpa2slow

import unittest
import hmac
import hashlib


class PrfTestSuite(unittest.TestCase):
    """PRF test cases."""
    
    def test_prf_slow(self):
        objSha = wpa2slow.Sha1()
        objHmac = wpa2slow.Hmac_Sha1(objSha)
        objPrf = wpa2slow.Prf(objHmac)
        
        pmk = '9051ba43660caec7a909fbbe6b91e4685f1457b5a2e23660d728afbd2c7abfba'
        cMac = '001dd0f694b0'
        apMac = '489d2477179a'
        apNonce = '87f2718bad169e4987c94255395e054bcaf77c8d791698bf03dc85ed3c90832a'
        cNonce = '143fbb4333341f36e17667f88aa02c5230ab82c508cc4bd5947dd7e50475ad36'
        
        ptk = '9287f887faade9257f5a806309a2bac8956fcbec'
        
        #Todo: check desired output lengths
        self.assertEqual(objPrf.PRF(pmk, apMac, cMac, apNonce, cNonce), ptk[0:32])
        
        pmk = '01b809f9ab2fb5dc47984f52fb2d112e13d84ccb6b86d4a7193ec5299f851c48'
        apMac = '001e2ae0bdd0'
        cMac = 'cc08e0620bc8'
        apNonce = '61c9a3f5cdcdf5fae5fd760836b8008c863aa2317022c7a202434554fb38452b'
        cNonce = '60eff10088077f8b03a0e2fc2fc37e1fe1f30f9f7cfbcfb2826f26f3379c4318'
        
        ptk = 'bf49a95f0494f44427162f38696ef8b6'
        
        self.assertEqual(objPrf.PRF(pmk, apMac, cMac, apNonce, cNonce), ptk)
        
        #Finish
        
        
if __name__ == '__main__':
    unittest.main()