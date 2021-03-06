#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-shared \
                         --enable-threads \
                         --enable-unicode \
                         --with-system-gmp \
                         --enable-boehm=system \
                         --with-clx")
    # ecl is installing some files direcly under /usr/share/doc directory wich is not normal.
    pisitools.dosed("build/doc/Makefile", 'doc/\$\{PACKAGE_TARNAME\}', 'doc/ecl')

def build():
    # ecl has parallel make problems, bug reported upstream. (ecls-Bugs-2823867)
    autotools.make("-j1")

def install():
    autotools.install()
    autotools.install("-C build/doc")
    pisitools.dodoc("src/CHANGELOG")
