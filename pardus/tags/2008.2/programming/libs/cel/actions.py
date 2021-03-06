#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-optimize-mode-debug-info=no \
                         --enable-separate-debug-info=no \
                         --with-cs-prefix=/usr \
                         --with-python=yes")

def build():
    shelltools.system("jam -qa")

def install():
    for f in ("install_bin", "install_plugin", "install_lib",
              "install_include", "install_data", "install_config", "install_doc"):
        shelltools.system("jam -s DESTDIR=%s %s" % (get.installDIR(), f))

    shelltools.copytree("data/library/blpython/widgets", "%s/usr/share/cel-1.3/data/library/blpython/" % get.installDIR())

    pisitools.domove("/usr/share/cel-1.3/bindings/python/*", "/usr/lib/%s/site-packages/" % get.curPYTHON())
    pisitools.removeDir("/usr/share/cel-1.3/bindings")

    pisitools.rename("/usr/share/doc/cel-1.3", get.srcTAG())
