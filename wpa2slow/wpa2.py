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

from . import compare
from . import handshake
from . import hmac
from . import pbkdf2
from . import sha1

class Wpa2(object):
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.message = [0] * 64
        self.messageLength = 0
        
    def addByte(self, input):
        self.shiftMessage()
        self.message[0] = input
        self.messageLength = self.messageLength + 1

    def formatW(self, start = 0, stop = 80):
        W = ''
        for x in range(start, stop):
            W = W + '{:08X} '.format(self.W[x])
        
        return W[:-1]
