#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#  Home-rolled HMAC algorithm allows better debugging of intermediate steps 
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

from sha1 import Sha1
import hashlib
import hmac

class Hmac_Sha1(object):
    
    def __init__(self, Sha1Obj):
        self.Sha1 = Sha1Obj
        self.shaBo = ''
        self.reset()
        
        
    def reset(self):
        self.Bi = [0x36] * 64
        self.Bo = [0x5c] * 64
    
    
    def run(self):
        secret = 'Jefe'
        value = 'what do ya want for nothing?'
        print "Goal: "
        #print hmac.new(secret, value, hashlib.sha1).hexdigest()
        return self.load(secret, value)
        
    def addSecret(self, secret):
        for x in range(0, len(secret)):
            self.Bi[x] = self.Bi[x] ^ ord(secret[x])
            self.Bo[x] = self.Bo[x] ^ ord(secret[x])

    def load(self, secret, value, fast=False):
        if fast == True:
            return hmac.new(secret, value, hashlib.sha1).hexdigest()
            
        self.reset()
        self.addSecret(secret)
        
        shaBi = self.Sha1.hashString(self.generateString(self.Bi) + value)
        shaBiDec = shaBi.decode("hex")
        
        Bo = self.generateString(self.Bo) + shaBiDec
        self.shaBo = self.Sha1.hashString(Bo)
        
        return self.shaBo
        
    def generateString(self, intList):
        out = ''
        for x in range(0, len(intList)):
            #print intList[x]
            out = out + chr(intList[x])
        
        return out
