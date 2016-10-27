#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                            handshake.py 
#    Pull all data from an hccapture file containing the 4-way handshake
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
import struct

class Handshake(object):

    def __init__(self):
        self.reset()
        
    def reset(self):
        self.b = ''
        
    def load(self, filename):
        fp = open(filename, mode='rb')
        
        #https://hashcat.net/wiki/doku.php?id=hccap
        #char          essid[36];
        #unsigned char mac1[6];
        #unsigned char mac2[6];
        #unsigned char nonce1[32];
        #unsigned char nonce2[32];
        #unsigned char eapol[256];
        #int           eapol_size;
        #int           keyver;
        #unsigned char keymic[16];
        
        self.ssid = struct.unpack('<36s', fp.read(36))
        self.mac1 = struct.unpack('<6s', fp.read(6))
        self.mac2 = struct.unpack('<6s', fp.read(6))
        self.nonce1 = struct.unpack('<32s', fp.read(32))
        self.nonce2 = struct.unpack('<32s', fp.read(32))
        self.eapol = struct.unpack('<256s', fp.read(256))
        self.eapol_size = struct.unpack('<1I', fp.read(4))
        self.keyver = struct.unpack('<1I', fp.read(4))   #0x01 means WPA - Abort! Anything else good.
        self.keymic = struct.unpack('<16s', fp.read(16))
        
        return (self.ssid, self.mac1, self.mac2, self.nonce1, self.nonce2, self.eapol, self.eapol_size, self.keymic)

if __name__ == "__main__":
    print 'Loading handshake...'
    obj = Handshake()
    obj.load('../test/wpa2.hccap')
    