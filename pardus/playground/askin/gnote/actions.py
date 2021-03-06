#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.autoreconf("-fiv")
	autotools.rawConfigure("--enable-dbus \
                                --disable-schemas-install \
                                --enable-applet \
                                --disable-static")

def build():
	autotools.make()

def install():
        autotools.install()
	pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
