Using this library
====================================

Check out `main.py <https://github.com/JarrettR/WPA-Slowed-Down/blob/master/main.py>`_ for a few examples of the top level methods.

Additionally, this library is used in the regression tests for my `VHDL implementation of WPA2 <https://github.com/JarrettR/FPGA-Cryptoparty/FPGA/tests>`_ .

All of the intermediate methods(SHA1, HMAC, PBkDF2, and PRF) are available too, but undocumented at this time.

This module read and parse capture files in `hccap <https://hashcat.net/cap2hccap/>`_ format, outputting the required inputs.
Standard capture formats may eventually be supported, but it's low priority, as the linked web converter is pretty good.
