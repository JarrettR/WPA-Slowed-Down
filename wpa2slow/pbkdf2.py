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
from hmac import Hmac

class Pbkdf2(object):
    
    def __init__(self):
        self.W = [0] * 80
        self.reset()
        
    def reset(self):
        self.message = [0] * 64
        self.messageLength = 0
        
    def run(self, objHmac, mk, ssid, fast=False):
        
        x1 = objHmac.load(mk, ssid + '\0\0\0\1')
        x2 = objHmac.load(mk, ssid + '\0\0\0\2')
        
        f1 = self.toAscii(x1)
        f2 = self.toAscii(x2)
        
        for x in xrange(4095):
            x1 = objHmac.load(mk, self.toAscii(x1))
            x2 = objHmac.load(mk, self.toAscii(x2))
            
            f1 = self.xorString(self.toAscii(x1), f1)
            f2 = self.xorString(self.toAscii(x2), f2)
        
        out = self.toHexString(f1) + self.toHexString(f2)
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