#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/build-docbook-catalog")
    os.system('/usr/bin/install-catalog --add /etc/sgml/xml-docbook-4.5.cat \
               /etc/sgml/sgml-docbook.cat')
    os.system('/usr/bin/install-catalog --add /etc/sgml/xml-docbook-4.5.cat \
               /usr/share/sgml/docbook/xml-dtd-4.5/docbook.cat')

def preRemove():
    os.system('/usr/bin/install-catalog --remove /etc/sgml/xml-docbook-4.5.cat \
               /etc/sgml/sgml-docbook.cat')
    os.system('/usr/bin/install-catalog --remove /etc/sgml/xml-docbook-4.5.cat \
               /usr/share/sgml/docbook/xml-dtd-4.5/docbook.cat')