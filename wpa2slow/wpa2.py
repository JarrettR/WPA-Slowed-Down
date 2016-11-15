#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                            wpa2.py 
#    WPA2 Parent Class
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

from . import Sha1
from . import Hmac_Sha1
from . import Pbkdf2
from . import Handshake
from . import Prf
from binascii import a2b_hex, b2a_hex 

class Wpa2(object):
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.objSha = Sha1()
        self.objHmac = Hmac_Sha1(self.objSha)
        self.objPbkdf2 = Pbkdf2()
        self.objPrf = Prf(self.objHmac)
        
    def loadAP(self, input):
        self.ap = input
        
    def loadMK(self, input):
        self.mk = input
        
    def genMic(self, pmk):
        ptk = self.objPrf.PRF(pmk, b2a_hex(self.ap.mac1),
                                    b2a_hex(self.ap.mac2),
                                    b2a_hex(self.ap.nonce1),
                                    b2a_hex(self.ap.nonce2))        
        mic = self.objPrf.MIC(ptk, b2a_hex(self.ap.eapol[0:self.ap.eapol_size]))
        return mic
        
    def test(self, input, fast=False):
        self.loadMK(input)
        pmk = self.objPbkdf2.run(self.objHmac, self.mk, self.ap.ssid, fast=fast)
        mic = self.genMic(pmk)
        keymic = b2a_hex(self.ap.keymic)
        if mic == keymic:
            return True
        else:
            return False
        
