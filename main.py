#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                              main.py 
#    Provides working examples for the wpa2slow package
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

if __name__ == "__main__":
    capFile = wpa2slow.Handshake()
    
    capFile.load('tests/data/wpa2.hccap')
    
    print 'Loaded capture file for ' + capFile.ssid + '!'
    print 'This contains several variables that go into the PRF'
    
    wpa = wpa2slow.Wpa2()
    wpa.loadAP(capFile)
    
    print wpa.test('Foo')
    print wpa.test('Bar')
    print wpa.test('dictionary')    #This is the AP's password
    
    
    