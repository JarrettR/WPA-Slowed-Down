#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                            python_pbkdf2.py 
#    PBKDF2 mock object
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
import hashlib #For testing mock objects
import random
from sha1 import Sha1
from hmac_sha1 import Hmac_Sha1
from binascii import a2b_hex, b2a_hex 

class Pbkdf2(object):
    
    def __init__(self):
        self.W = [0] * 80
        self.reset()
        
    def reset(self):
        self.message = [0] * 64
        self.messageLength = 0
        
    def run(self, objHmac, mk, ssid, fast=False):
        #Requires Python 2.7.8 or later
        #Ubuntu 14.04 LTS generally only updates to 2.7.6 :(
        #if fast==True:
        #   return hashlib.pbkdf2_hmac('sha1', mk, ssid, 4095)
        
        x1 = objHmac.load(mk, ssid + '\0\0\0\1', fast)
        x2 = objHmac.load(mk, ssid + '\0\0\0\2', fast)
        
        f1 = a2b_hex(x1)
        f2 = a2b_hex(x2)
        
        for x in xrange(4095):
            x1 = objHmac.load(mk, a2b_hex(x1), fast)
            x2 = objHmac.load(mk, a2b_hex(x2), fast)
            
            f1 = self.xorString(a2b_hex(x1), f1)
            f2 = self.xorString(a2b_hex(x2), f2)
        
        out = b2a_hex(f1) + b2a_hex(f2)
        return out[0:64]
        
    def xorString(self, in1, in2):
        i = 0
        out = ''
        
        x1 = in1
        x2 = in2
        for x in xrange(len(x1)):
            what = chr(ord(x1[x]) ^ ord(x2[x]))
            out += what
            
        return out
        