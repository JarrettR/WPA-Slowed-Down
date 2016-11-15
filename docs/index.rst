.. wpa2slow documentation master file, created by
   sphinx-quickstart on Tue Nov 15 11:47:51 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

wpa2slow
====================================

wpa2slow is a home-rolled Python implementation of the WPA2 encryption algorithm, using no encryption libraries.

## Project goals
This project grew out of the FPGA implementation of WPA2 [here](https://github.com/JarrettR/FPGA-Cryptoparty), as a platform for regression testing and experimentation.

WPA2 requires three or four different algorithms to calculate a final password, depending on how you count them.

There is a fair amount of discussion on these functions in [this](http://jrainimo.com/build/?cat=6) category of my site.

The entire goal was to have intermediate steps of the algorithms to compare with the VHDL implementation.
Perhaps this will be useful to someone else.


## Benchmarks

Hash speed of my general purpose computer; 2,000 keys / second

Hash speed of a Raspberry Pi 1: 45 keys / second

Hash speed of this project: 0.25 keys / second

## Sounds great! How can I get started?

Clone this repo, and then from this directory, type `pip install .`

Check `main.py` for examples and test cases.

Can read and parse capture files in [hccap](https://hashcat.net/cap2hccap/) format, outputting the required inputs.

## Further reading

* `Announcement post: <http://jrainimo.com/build/?p=1157>`_
* `GitHub: <https://github.com/JarrettR/WPA-Slowed-Down>`_


Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

