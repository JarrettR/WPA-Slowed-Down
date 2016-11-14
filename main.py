#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                              main.py 
#    Provides working examples for the wpa2slow library
#    Copyright (C) 2016  Jarrett Rainier
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import wpa2slow
import random
import hashlib 
import hmac 

def test_hmac():
    objSha = wpa2slow.sha1.Sha1()
    objHmac = wpa2slow.hmac.Hmac(objSha)
    
    secret = 'Jefe'
    value = 'what do ya want for nothing?'
    print "Goal:   " + hmac.new(secret, value, hashlib.sha1).hexdigest()
    print "Result: " + objHmac.load(secret, value)
    
    secret = 'secret'
    value = 'value'
    print "Goal:   " + hmac.new(secret, value, hashlib.sha1).hexdigest()
    print "Result: " + objHmac.load(secret, value)
    
def test_pbkdf2():
    objSha = wpa2slow.sha1.Sha1()
    objHmac = wpa2slow.hmac.Hmac(objSha)
    objPbkdf2 = wpa2slow.pbkdf2.Pbkdf2()
    secret = 'Jefe'
    value = 'what do ya want for nothing?'
    secret = 'secret'
    value = 'value'
    
    # 64 hex digits / 32 bytes / 256 bits
    print objPbkdf2.run(objHmac, secret, value)
    
def test_prf():
    objSha = wpa2slow.sha1.Sha1()
    objHmac = wpa2slow.hmac.Hmac(objSha)
    objPrf = wpa2slow.compare.Prf(objHmac)
    
    pmk = '9051ba43660caec7a909fbbe6b91e4685f1457b5a2e23660d728afbd2c7abfba'
    cMac = '001dd0f694b0'
    apMac = '489d2477179a'
    apNonce = '87f2718bad169e4987c94255395e054bcaf77c8d791698bf03dc85ed3c90832a'
    cNonce = '143fbb4333341f36e17667f88aa02c5230ab82c508cc4bd5947dd7e50475ad36'
    
    ptk = '9287f887faade9257f5a806309a2bac8956fcbec'
    
    print "Result: " + objPrf.PRF(pmk, apMac, cMac, apNonce, cNonce)
    print "Goal:   " + ptk
    
    pmk = '01b809f9ab2fb5dc47984f52fb2d112e13d84ccb6b86d4a7193ec5299f851c48'
    apMac = '001e2ae0bdd0'
    cMac = 'cc08e0620bc8'
    apNonce = '61c9a3f5cdcdf5fae5fd760836b8008c863aa2317022c7a202434554fb38452b'
    cNonce = '60eff10088077f8b03a0e2fc2fc37e1fe1f30f9f7cfbcfb2826f26f3379c4318'
    
    ptk = 'bf49a95f0494f44427162f38696ef8b6'
    
    print "Result: " + objPrf.PRF(pmk, apMac, cMac, apNonce, cNonce)
    print "Goal:   " + ptk
    
def test_mic():
    objSha = wpa2slow.sha1.Sha1()
    objHmac = wpa2slow.hmac.Hmac(objSha)
    objPrf = wpa2slow.compare.Prf(objHmac)
    
    ptk = 'bf49a95f0494f44427162f38696ef8b6'
    
    data = '0103005ffe01090020000000000000000100000000' + \
    '0000000000000000000000000000000000000000000000000' + \
    '0000000000000000000000000000000000000000000000000' + \
    '00000000000000000000000000000000000000000000000000000000'

    print "Result: " + objPrf.MIC(ptk, data)
    print 'Goal:   45282522bc6707d6a70a0317a3ed48f0'
    
def test_handshake_load():
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
    
def test_full():
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
    

if __name__ == "__main__":
    print "Testing SHA1: "
    test_sha1()
    print "Testing HMAC: "
    test_hmac()
    print "Testing PBKDF2: "
    test_pbkdf2()
    print "Testing PRF: "
    test_prf()
    print "Testing MIC: "
    test_mic()
    print 'Testing handshake load:'
    test_handshake_load()
    print 'Testing Full Process:'
    #test_full()
    print "Finished"
    