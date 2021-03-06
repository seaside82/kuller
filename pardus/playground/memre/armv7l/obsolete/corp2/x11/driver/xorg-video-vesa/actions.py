#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import get

WorkDir = "xf86-video-vesa-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fvi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
