#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    pythonmodules.install()
    pisitools.dosed("%s/usr/bin/openerp-server" % get.installDIR(), "%s" % get.installDIR(), "")
    pisitools.domove("/usr/share/doc/openerp-server-%s/*" % get.srcVERSION(), "/usr/share/doc/%s/" % get.srcNAME())
    pisitools.removeDir("/usr/share/doc/openerp-server-%s" % get.srcVERSION())
    pisitools.dodir("/var/log/openerp-server")
    pisitools.dodir("/var/run/openerp-server")