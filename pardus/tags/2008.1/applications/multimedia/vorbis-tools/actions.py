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
    shelltools.export("AT_M4DIR", "m4")
    autotools.autoreconf("-fi")

    autotools.configure('--enable-nls \
                         --enable-vcut \
                         --enable-ogg123 \
                         --with-flac \
                         --with-speex \
                         --docdir="/%s/%s"' % (get.docDIR(), get.srcTAG()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "ogg123/ogg123rc-example")
