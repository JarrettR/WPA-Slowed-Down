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
        self.ssid = None
        self.mac1 = None
        self.mac2 = None
        self.nonce1 = None
        self.nonce2 = None
        self.eapol = None
        self.eapol_size = None
        self.keyver = None
        self.keymic = None
        
    def load(self, filename, hccap=True):
        '''
        Load handshake file.
        Defaults:
        hccap=True - File to be loaded is in Hashcat capture format
        '''
        fp = open(filename, mode='rb')
        
        if hccap == True:
        
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
            
            #Todo: investigate null byte removal rules in original spec
            self.ssid = struct.unpack('<36s', fp.read(36))[0].rstrip('\0')
            self.mac1 = struct.unpack('<6s', fp.read(6))[0]
            self.mac2 = struct.unpack('<6s', fp.read(6))[0]
            self.nonce1 = struct.unpack('<32s', fp.read(32))[0]
            self.nonce2 = struct.unpack('<32s', fp.read(32))[0]
            self.eapol = struct.unpack('<256s', fp.read(256))[0]
            self.eapol_size = struct.unpack('<1I', fp.read(4))[0]
            self.keyver = struct.unpack('<1I', fp.read(4))[0]   #0x01 means WPA - Abort! Anything else good.
            self.keymic = struct.unpack('<16s', fp.read(16))[0]
            
            fp.close()
        else:
            fp.close()
            raise NotImplementedError('Write Wireshark / AC capture format parser')
        
    def is_wpa2(self):
        '''
        Checks to make sure that:
        A) self.keyver is set, and
        B) self.keyver is not 0x01.
        0x01 means original WPA, and is not supported
        '''
        raise NotImplementedError('Write WPA / WPA2 check')
        
    def fix_order(self):
        '''
        The pseudorandom function(PRF) that generates the PTK requires both MAC and Nonce values 
        to be sorted in numerical order. The CAP formats don't re-order these, so this should be
        checked or automatically fixed.
        '''
        raise NotImplementedError('Write MAC/Nonce sorter')