#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                            python_compare.py 
#    WPA2 Pseudo Random Function and MIC comparison mock objects
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

'''
                          KEY FOUND! [ dictionary ]


  Master Key     : 5D F9 20 B5 48 1E D7 05 38 DD 5F D0 24 23 D7 E2
                   52 22 05 FE EE BB 97 4C AD 08 A5 2B 56 13 ED E2

  Transient Key  : 1E 5A DB F5 22 3A 16 57 D9 6A 99 A5 DB 1E 66 BC
                   75 78 10 2D 78 0E 59 37 84 1B B0 73 6A FA 67 18
                   03 C8 A3 E8 F5 B3 C8 25 D3 DC CC E7 E5 E3 F2 63
                   D1 BF 55 EE C9 41 0F 03 BD 39 12 36 12 C2 A6 BA

  EAPOL HMAC     : 0E 71 A6 25 FA AD E7 CE 9C 82 21 F7 B1 DB CE 46
'''
      
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
            r = r + self.objHmac.load(self.toAscii(pmk), self.a + self.toAscii("00" + b + "{:02x}".format(x)))
            #print r
        
        out = r
        return out[0:32]

    def MIC(self, ptk, data):
        objSha = Sha1()
        objHmac = Hmac_Sha1(objSha)
        
        ptk = self.toAscii(ptk)
        data = self.toAscii(data)
        
        out = objHmac.load(ptk,data)       
        
        return out[0:32]
        
    def toAscii(self, input):
        str = ''
        #print input
        while len(input) > 0:
            #print input[-2:]
            str = chr(int(input[-2:], 16)) + str
            input = input[0:-2]
        return str
        
    def toHexString(self, input):
        str = ''
        #print input
        for x in xrange(len(input)):
            #print input[-2:]
            str += "{:02x}".format(ord(input[x]))
        return str
