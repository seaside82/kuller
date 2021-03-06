#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "xen-3.0.3_0-src"
NoStrip = "/"

def setup():
    shelltools.cd("tools/ioemu")
    autotools.configure("--enable-sdl")

def build():
    shelltools.cd("tools/")
    autotools.make()

    shelltools.cd("../docs/")
    autotools.make()

def install():
    shelltools.cd("tools/")
    autotools.rawInstall("DESTDIR=%s XEN_PYTHON_NATIVE_INSTALL=1" % get.installDIR())

    shelltools.cd("../docs/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # clean pyc/o's
    pythonmodules.fixCompiledPy()

    # remove redhat specific dirs
    pisitools.removeDir("/etc/sysconfig")

    # remove unneeded dirs
    pisitools.removeDir("/etc/init.d")
    pisitools.removeDir("/etc/udev")
    pisitools.removeDir("/etc/hotplug")

    # Just pdf ones
    pisitools.removeDir("/usr/share/doc/xen/ps/")

    # xend expects these to exist
    pisitools.dodir("/var/log/xen-consoles")
    pisitools.dodir("/var/run/xenstored")
    pisitools.dodir("/var/lib/xenstored")
    pisitools.dodir("/var/xen/dump")

    # conflicting with qemu
    pisitools.remove("/usr/share/man/man1/qemu-img.1");
    pisitools.remove("/usr/share/man/man1/qemu.1");
