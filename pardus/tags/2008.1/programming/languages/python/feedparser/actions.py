#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/doc/%s/html" % get.srcTAG(), "docs/*")
    pisitools.dodoc("README","LICENSE")
