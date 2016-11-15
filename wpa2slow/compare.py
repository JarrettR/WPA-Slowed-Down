#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                            python_compare.py 
#    WPA2 Pseudo Random Function and MIC generator for comparison
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
import random
from binascii import a2b_hex, b2a_hex 
from sha1 import Sha1
from hmac_sha1 import Hmac_Sha1

class Prf(object):

    def __init__(self, objHmac):
        self.objHmac = objHmac
        self.a = "Pairwise key expansion"
        self.reset()
        
    def reset(self):
        self.b = ''
        
    def PRF(self, pmk, apMac, cMac, apNonce, cNonce):
        
        b = min(apMac, cMac) + max(apMac, cMac) + min(apNonce, cNonce) + max(apNonce, cNonce)
        #print b
        r = ""
        
        #Note: The spec says to loop this waaaay too many times and then truncate output
        for x in xrange(4):
            r = r + self.objHmac.load(a2b_hex(pmk), self.a + a2b_hex("00" + b + "{:02x}".format(x)))
            #print r
        
        out = r
        return out[0:32]

    def MIC(self, ptk, data):
        objSha = Sha1()
        objHmac = Hmac_Sha1(objSha)
        
        ptk = a2b_hex(ptk)
        data = a2b_hex(data)
        
        out = objHmac.load(ptk,data)       
        
        return out[0:32]
        