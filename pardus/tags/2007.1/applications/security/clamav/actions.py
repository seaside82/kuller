#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-id-check \
                         --disable-clamav \
                         --disable-zlib-vcheck \
                         --with-dbdir=/var/lib/clamav")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "NEWS", "README", "ChangeLog", "FAQ", "INSTALL")
    pisitools.dodir("/var/run/clamav")
    pisitools.dodir("/var/log/clamav")
