#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def build():
    autotools.make("KERNELDIR=/usr/src/linux-%s" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "usbcam/*.ko")
    pisitools.insinto("/lib/firmware", "*.fw")

    pisitools.dodoc("ChangeLog","README")
