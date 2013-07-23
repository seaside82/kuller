#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mozilla"

#locales = ["be", "ca", "de", "es-AR", "es-ES", "fr", "hu", "it", "nl", "pl", "pt-BR", "ru", "sv-SE", "tr"]
locales = ["be", "ca", "de", "es-AR", "es-ES", "fr", "hu", "it", "nl", "pl", "ru", "sv-SE", "tr"]

def setup():
    #Use autoconf-213 which we provide via a hacky pathc to produce configure
    shelltools.system("/bin/bash ./autoconf-213/autoconf-2.13 --macro-dir=autoconf-213/m4")
    shelltools.cd("js/src")
    shelltools.system("/bin/bash ../../autoconf-213/autoconf-2.13 --macro-dir=../../autoconf-213/m4")
    shelltools.cd("../..")

    shelltools.makedirs("../l10n")

    shelltools.makedirs("objdir")
    shelltools.cd("objdir")

    #this dummy configure is needed to build locales.
    #shelltools.system("../configure --prefix=/usr --libdir=/usr/lib --disable-strip --disable-install-strip")

    #now we have Makefiles needed to build locales (like toolkit/Makefile)
    #since we need debug symbols in dbginfo packages, we shouldn't strip binaries
    shelltools.system("../configure --prefix=/usr --libdir=/usr/lib --with-libxul-sdk=/usr/lib/xulrunner-devel-2.0 --enable-chrome-format=jar --disable-strip --disable-install-strip")

def build():
    shelltools.cd("objdir")

    autotools.make()

    for locale in locales:
        autotools.make("-C browser/locales langpack-%s" % locale)

def install():
    shelltools.cd("objdir")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.domove("/usr/lib/%s-%s" % (get.srcNAME(), get.srcVERSION()), "/usr/lib", "MozillaFirefox")
    olddir = shelltools.ls("%s/usr/lib/firefox*" % get.installDIR())[0].replace(get.installDIR(), "")
    pisitools.domove(olddir, "/usr/lib", "MozillaFirefox")

    pisitools.remove("/usr/bin/firefox")

    #install locales
    for locale in locales:
        pisitools.copytree("dist/xpi-stage/locale-%s" % locale, "%s/usr/lib/MozillaFirefox/extensions/langpack-%s@firefox.mozilla.org" % (get.installDIR(), locale))

    # Remove these
    #pisitools.remove("/usr/lib/MozillaFirefox/defaults/profile/mimeTypes.rdf")
    pisitools.remove("/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
    #pisitools.remove("/usr/lib/MozillaFirefox/.autoreg")

    shelltools.cd("..")

    # Install branding icon
    pisitools.insinto("/usr/share/pixmaps", "other-licenses/branding/firefox/default256.png", "firefox.png")

    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")