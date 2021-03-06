#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.dodir("/opt/eclipse")

    shelltools.copytree("features", "%s/opt/eclipse" % get.installDIR())
    shelltools.copytree("plugins", "%s/opt/eclipse" % get.installDIR())
