#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())

    for f in ["NEWS", "README", "AUTHORS", "ChangeLog"]:
        shelltools.touch(f)

    autotools.autoreconf("-fi")
    autotools.configure("--enable-mmx \
                         --disable-css")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dohtml("docs")