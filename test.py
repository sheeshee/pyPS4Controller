import sys

from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


if __name__ == "__main__":
    ds4drv = (len(sys.argv) > 1 and sys.argv[1] != '--usb')
    
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=ds4drv)
    controller.listen()
