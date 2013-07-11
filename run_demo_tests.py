import unittest
import xmlrunner

from xvfbwrapper import Xvfb

vdisplay = Xvfb(width=1280, height=720)
vdisplay.start()
print "Started Xvfb"

unittest.main(testRunner=xmlrunner.XMLTestRunner(output='selenium-demos-reports', verbosity=2),
        module="testDemoApp")

vdisplay.stop()
print "Ended Xvfb"

