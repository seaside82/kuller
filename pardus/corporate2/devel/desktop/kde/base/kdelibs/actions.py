#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

KeepSpecial=["libtool"]

shelltools.export("HOME", get.workDIR())

def setup():
    # Fix automake and python detection
    pisitools.dosed("admin/cvs.sh", "automake\*1\.10\*", "automake*1.1[0-5]*")
    pisitools.dosed("admin/acinclude.m4.in", "KDE_CHECK_PYTHON_INTERN\(\"2.5", "KDE_CHECK_PYTHON_INTERN(\"%s" % get.curPYTHON().split("python")[1])
    kde.make("-f admin/Makefile.common")

    kde.configure('--with-distribution="Pardus" \
                   --enable-inotify \
                   --enable-cups \
                   --enable-dnssd \
                   --enable-gcc-hidden-visibility \
                   --with-libart \
                   --with-libidn \
                   --with-utempter \
                   --with-alsa \
                   --with-ssl \
                   --with-tiff \
                   --with-gssapi \
                   --with-openexr \
                   --with-jasper \
                   --with-aspell \
                   --with-acl \
                   --disable-libfam \
                   --without-lua \
                   --without-hspell')

def build():
    kde.make()

def install():
    kde.install()
