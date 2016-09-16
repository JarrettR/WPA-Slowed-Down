# WPA-Slowed-Down
A home-rolled Python implementation of the WPA2 encryption algorithm, using no encryption libraries.

## Project goals
This project grew out of the FPGA implementation of WPA2 [here](https://github.com/JarrettR/FPGA-Cryptoparty), as a platform for regression testing and experimentation.

WPA2 requires three or four different algorithms to calculate a final password, depending on how you count them.

There is a fair amount of discussion on these functions in [this](http://jrainimo.com/build/?cat=6) category of my site.

None of this is very polished. Each file was written quickly when it became necessary, with a period of several months seperating them. The entire goal was to have intermediate steps of the algorithms to compare with the VHDL implementation.
Perhaps this will be useful to someone else.

## Benchmarks

Hash speed of my general purpose computer; 2,000 keys / second

Hash speed of a Raspberry Pi 1: 45 keys / second

Hash speed of this project: 0.25 keys / second