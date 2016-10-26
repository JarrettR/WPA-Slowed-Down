#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                              main.py 
#    Tests and provides working examples for the wpa2slow library
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


def test_sha1():
    obj = wpa2slow.sha1.Sha1Model()
    
    str = ''

    for x in range(0, 185):
        input = random.randint(0, 0xff)
        str = str + chr(random.randint(0, 0xff))
        
        v1 = obj.hashString(str)
        v2 = hashlib.sha1(str).hexdigest()
        print v1
        print v2
        if v1 != v2:
            print "-------------- NOT EQUAL"
        print "------------"

def test_hmac():
    objSha = wpa2slow.sha1.Sha1Model()
    objHmac = wpa2slow.hmac.HmacModel(objSha)
    
    secret = 'Jefe'
    value = 'what do ya want for nothing?'
    print "Goal:   " + hmac.new(secret, value, hashlib.sha1).hexdigest()
    print "Result: " + objHmac.load(secret, value)
    
    secret = 'secret'
    value = 'value'
    print "Goal:   " + hmac.new(secret, value, hashlib.sha1).hexdigest()
    print "Result: " + objHmac.load(secret, value)
    
def test_pbkdf2():
    objSha = wpa2slow.sha1.Sha1Model()
    objHmac = wpa2slow.hmac.HmacModel(objSha)
    objPbkdf2 = wpa2slow.pbkdf2.Pbkdf2Model()
    secret = 'Jefe'
    value = 'what do ya want for nothing?'
    secret = 'secret'
    value = 'value'
    
    # 64 hex digits / 32 bytes / 256 bits
    print objPbkdf2.run(objHmac, secret, value)

if __name__ == "__main__":
    print "Testing SHA1: "
    test_sha1()
    print "Testing HMAC: "
    test_hmac()
    print "Testing PBKDF2: "
    test_pbkdf2()
    print "Finished"
    