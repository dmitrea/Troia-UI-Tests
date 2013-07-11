import unittest
import xmlrunner
import sys

from xvfbwrapper import Xvfb

import settings

vdisplay = Xvfb(width=1280, height=720)
vdisplay.start()

if len(sys.argv) > 1:
    settings.Settings.url = sys.argv[1]
    sys.argv = sys.argv[:1]

print "Started Xvfb"

unittest.main(testRunner=xmlrunner.XMLTestRunner(output='selenium-demos-reports', verbosity=2),
        module="testDemoApp")

vdisplay.stop()
print "Ended Xvfb"

