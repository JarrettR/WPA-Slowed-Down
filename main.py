#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                              main.py 
#    Provides working examples for the wpa2slow library
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
import random
import hashlib 
import hmac 
    

if __name__ == "__main__":
    print "Testing SHA1: "
    test_sha1()
    print "Testing HMAC: "
    test_hmac()
    print "Testing PBKDF2: "
    test_pbkdf2()
    print "Testing PRF: "
    test_prf()
    print "Testing MIC: "
    test_mic()
    print 'Testing handshake load:'
    test_handshake_load()
    print 'Testing Full Process:'
    #test_full()
    print "Finished"
    