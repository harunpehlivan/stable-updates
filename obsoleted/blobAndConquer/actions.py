#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

params = {"CXX": get.CXX(), \
          "datadir": get.dataDIR(), \
          "installdir": get.installDIR(), \
          "htmldir": "%s/%s/html" % (get.docDIR(),get.srcNAME())}

def build():
    autotools.make("CXX=%(CXX)s \
                    DATADIR=/%(datadir)s/blobAndConquer/ \
                    DOCDIR=/%(htmldir)s/" % params)

def install():
    autotools.rawInstall('DESTDIR=%(installdir)s \
                          BINDIR=%(installdir)s/usr/bin/ \
                          DATADIR=%(installdir)s/%(datadir)s/blobAndConquer/ \
                          DOCDIR=%(installdir)s/%(htmldir)s/' % params)

    pisitools.insinto("/usr/share/pixmaps", "icons/blobAndConquer.png")
