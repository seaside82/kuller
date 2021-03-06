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

# We are making our own package to support 2.6 kernels
#
# http://www.sfu.ca/~cth/ltmodem/ltmodem-8.31a10.tar.gz   as main directory and
# http://linmodems.technion.ac.il/packages/ltmodem/kernel-2.6/ltmodem-2.6-alk-9.tar.bz2
# as "modules" directory
# After unpacking use the following commands in DOCs directory
#
# rm -rf Installers build* Build* gcc3.txt Examples Suse*
# rm -rf fixscript* slackware srcprep.man scanmodem.man conf*
# rename .man .1 *.man

WorkDir = "ltmodem-8.31_alpha10-alk9"

def setup():
    pisitools.dosed("modules/Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("modules/Makefile", "`uname -r`", get.curKERNEL())

def build():
    shelltools.cd("modules")
    autotools.make("KERNEL_DIR=/lib/modules/%s/build module" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "modules/*.ko")
    pisitools.insinto("/etc/udev/rules.d/", "modules/docs/ltmodem.rules", "55-ltmodem.rules")

    # install utilities
    pisitools.dosbin("utils/lt_*")
    pisitools.insinto("/usr/sbin", "utils/unloading","lt_unloading")

    # install docs
    pisitools.dohtml("DOCs/*")
    pisitools.doman("DOCs/*.1")
    pisitools.dodoc("1ST-READ", "DOCs/*")


