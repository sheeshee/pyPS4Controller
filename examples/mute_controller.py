"""
Mute Controller Example
=======================
By Samuel Sheehy, June 2020

The default behaviour of an event in the Controller
object is to print to the console every time an event
happens, which is great for debugging, but the messages
can be a bit irksome when you want to use the console
for other purposes.

This script shows a quick way to subclass the Controller
to "mute" those print statements. It does this by
overwritting all Controller methods that begin with "on_"
and replacing them with a function that does nothing.

This avoids having to redefine each trigger independentely.

Tested on Python 3.8 only.

"""

from pyPS4Controller.controller import Controller


def do_nothing(self, value=None): 
    """
    This functions does nothing. It is made to replace
    all event methods of the Controller class.
    """
    pass


class MuteController(Controller):
    """
    Same as the Controller method, but triggers do nothing
    by default.
    """
    def __init__(self, **kwargs):
        # Rewrite all methods in Controller class
        # to do nothing. Only the methods defined
        # below as methods will do anything.
        for attr in dir(Controller):
            if attr.startswith('on_'):  
                setattr(Controller, attr, do_nothing)
        # Run the initalisation to define the rest of
        # the attributes.
        Controller.__init__(self, **kwargs)
    
    # Some example custom triggers:
    def on_x_press(self):
        print('X pressed')
    
    def on_circle_press(self):
        print('O pressed')


if __name__ == "__main__":
    controller = MuteController(
        interface="/dev/input/js0",
        # Note: You may also need to remap the button id's
        # depending on how your system reads the events.
        # See README for more details.

        # event_definition=RemappedEvent,        

        # Note: You may also need to change the format
        # of the events being received by your PC.
        # See README for more details.

        # event_format="3Bh2b"
    )
    controller.listen()
