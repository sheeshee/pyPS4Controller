"""
Byte Stream Inspector
=====================
By Samuel Sheehy, June 2020

On some platforms the byte stream sent by the controller
to the PC may be different than the default. This can cause
some unusual behaviour such as 1. Button mapping is off
2. Need to press button twice to register the release event
(see README.md for more details).

This script will print the byte stream to the console for
visual inspection. Feel free to play around with the values
to try different configurations.

Start by trying different byte lengths of "b" (e.g. "bbbbbbbb")
until a single button press (NOTE: only the PRESS, this does
not include the RELEASE) consistently returns just a single line.
The Release of the button should print its own line of data.

For the same button being pressed and released, there should be
some consistency in the data. If the data keeps changing, then
you are probably specifying too small of a package size. If
the buttons seem "sticky" and are not consistent after ten or so
presses, then the package size may be too big.

Once you have a consistent data, then play
around with different unpacking structures until you find
something that makes sense, especially with regards to the joy
sticks.

You may find it easier to start by connecting the device via
USB. This ensures that information is only sent when a button
is pressed instead of consistently streamed. It can help make
the incoming data easier to read.

Tested on Python 3.8 only.

"""
import os
import time
import struct
import datetime

# PACKET_FORMAT tells `struct.unpack` how to interpret the
# bytes it receives. The format must be compatible with PACKET_SIZE
# See https://docs.python.org/3/library/struct.html#format-characters
# Default is LhBB, maybe try 3Bh2b?
PACKET_FORMAT = "3Bh2b"
# INTERFACE is where the script will look for the byte stream.
# Depending on what devices you have connected to your computer
# you may need to change it like so: js0 -> js1 or other.
INTERFACE = "/dev/input/js0"


def stream(interface):
    """
    Runs a continous loop that repeatidly reads the device interface.
    """
    # Connect
    assert os.path.exists(interface), "Device must be connected."
    print('Connecting...', end='')
    handle = open(interface, "rb")
    print('done! Press Ctrl+C to exit.')
    # Read
    while True:
        try:
            read(handle)
        except KeyboardInterrupt:
            break
    # Finish
    print('\nExitted.')


def read(handle):
    """
    Prints the extracted data to the console with a timestamp.
    """
    size = struct.calcsize(PACKET_FORMAT)
    raw = handle.read(size)
    # The typical structure tends to be something like
    # TIME_ELAPSED_S, TIME_ELAPSED_MINS, VALUE, TYPE, ID
    data = struct.unpack(PACKET_FORMAT, raw)
 
    print(datetime.datetime.now(), end='  ')
    format_string = "{:7d} "*len(data)
    print(format_string.format(*data))

if __name__ == "__main__":
    stream(INTERFACE)
