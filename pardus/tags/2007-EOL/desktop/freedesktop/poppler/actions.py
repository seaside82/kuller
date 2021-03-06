#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --enable-opi \
                         --enable-xpdf-headers \
                         --disable-cairo-output \
                         --enable-libjpeg \
                         --enable-zlib \
                         --enable-poppler-glib \
                         --enable-poppler-qt \
                         --enable-poppler-qt4")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS", "README-XPDF", "TODO")
