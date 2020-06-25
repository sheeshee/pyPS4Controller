"""
Remaped Event Triggers Example
==============================
By Samuel Sheehy, June 2020

On some machines, buttons on the PS4 controller may
have different ID's. This example shows you how to
create a redefine the Event class with your desired
mapping.

Tested on Python 3.8 only.

"""
from pyPS4Controller.controller import Controller, Event


class RemappedEvent(Event):
    """
    Event with button id's remapped to different buttons.
    """
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
    
        self.keymap = dict(
            x        = 0 if not self.connecting_using_ds4drv else 1,
            circle   = 1 if not self.connecting_using_ds4drv else 2,
            triangle = 2 if not self.connecting_using_ds4drv else 3,
            square   = 3 if not self.connecting_using_ds4drv else 0
        )

    def x_pressed(self):
        return self.button_id == self.keymap['x'] and self.button_type == 1 and self.value == 1

    def x_released(self):
        return self.button_id == self.keymap['x'] and self.button_type == 1 and self.value == 0

    def triangle_pressed(self):
        return self.button_id == self.keymap['triangle'] and self.button_type == 1 and self.value == 1

    def triangle_released(self):
        return self.button_id == self.keymap['triangle'] and self.button_type == 1 and self.value == 0

    def square_pressed(self):
        return self.button_id == self.keymap['square'] and self.button_type == 1 and self.value == 1

    def square_released(self):
        return self.button_id == self.keymap['square'] and self.button_type == 1 and self.value == 0

    def circle_pressed(self):
        return self.button_id == self.keymap['circle'] and self.button_type == 1 and self.value == 1

    def circle_released(self):
        return self.button_id == self.keymap['circle'] and self.button_type == 1 and self.value == 0


if __name__ == "__main__":
    controller = Controller(
        interface="/dev/input/js0",
        event_definition=RemappedEvent,
        # Note: You may also need to change the format
        # of the events being received by your PC.
        # See README for more details.

        # event_format="3Bh2b"
    )
    controller.listen()
