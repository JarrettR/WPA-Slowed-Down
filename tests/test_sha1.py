# -*- coding: utf-8 -*-

from .context import wpa2slow

import unittest
import random
import hashlib


class Sha1TestSuite(unittest.TestCase):
    """SHA1 test cases."""
    
    def test_sha1_slow(self):
        obj = wpa2slow.Sha1()
        
        str = ''

        for x in range(0, 185):
            input = random.randint(0, 0xff)
            str = str + chr(random.randint(0, 0xff))
            
            v1 = obj.hashString(str)
            v2 = hashlib.sha1(str).hexdigest()
            print v1
            print v2
            
            self.assertEqual(v1, v2)
        
        
if __name__ == '__main__':
    unittest.main()