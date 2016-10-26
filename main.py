#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                              main.py 
#    Tests and provides working examples for the wpa2slow library
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


def test_sha1():
    obj = wpa2slow.sha1.Sha1Model()
    
    str = ''

    for x in range(0, 185):
        input = random.randint(0, 0xff)
        str = str + chr(random.randint(0, 0xff))
        
        v1 = obj.hashString(str)
        v2 = hashlib.sha1(str).hexdigest()
        print v1
        print v2
        if v1 != v2:
            print "-------------- NOT EQUAL"
        print "------------"



if __name__ == "__main__":
    test_sha1()
    print "Finished"
    