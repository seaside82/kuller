#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get


exampledir = "%s/%s/examples" % (get.docDIR(), get.srcTAG())
examples = ["bigtext.py", "browse.py", "calc.py", "dialog.py", "edit.py", "fib.py", "graph.py", "input_test.py", "tour.py"]

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.dohtml("tutorial.html", "reference.html")

    for f in examples:
        pisitools.insinto(exampledir, f)
    shelltools.chmod("%s/%s/*" % (get.installDIR(), exampledir), 0644)

