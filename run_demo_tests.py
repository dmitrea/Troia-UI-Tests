import unittest

from xvfbwrapper import Xvfb

vdisplay = Xvfb(width=1280, height=720)
vdisplay.start()
print "Started Xvfb"

unittest.main(module="testDemoApp", verbosity=2)

vdisplay.stop()
print "Ended Xvfb"

