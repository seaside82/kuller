#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xen-4.0.1-rc2"
NoStrip = ["/"]

def build():
    #shelltools.export("LDFLAGS", "-Wl,-O1 -Wl,-z,relro -Wl,--hash-style=gnu -Wl,--as-needed -Wl,--sort-common")
    shelltools.export("LDFLAGS", "")
    shelltools.export("CFLAGS", "")
    shelltools.export("CXXFLAGS", "")
    # shelltools.system("make -j1 dist-xen dist-tools dist-stubdom dist-docs")
    # shelltools.system("make -j1 dist-xen")
    # shelltools.system("make -j1 dist-tools")
    # shelltools.system("make -j1 dist-stubdom")
    # shelltools.system("make -j1 dist-docs")
    # autotools.make("dist-xen dist-tools dist-stubdom dist-docs")
    autotools.make("dist-xen")
    autotools.make("dist-tools")
    # autotools.make("dist-stubdom")
    # autotools.make("dist-docs")

def install():
    shelltools.system("rm -rf dist/install/etc/hotplug")
    shelltools.system("chmod -R a+rX dist/install")
    shelltools.system("((cd dist; tar -cf - *) | tar --no-same-owner -C %s/ -xf -)" % get.pkgDIR())
    # shelltools.chmod(get.workDIR() + "dist/install/*")
    # shelltools.copytree("dist/install/*", "%s/" % get.installDIR()) 