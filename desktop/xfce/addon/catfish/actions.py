#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.system("grep -rl '^#!.*python$' | xargs sed -i '1s/python/&3/'")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    
    pisitools.dosym("/usr/share/icons/hicolor/scalable/apps/org.xfce.catfish.svg", "/usr/share/pixmaps/org.xfce.catfish.svg")

    #pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "NEWS", "README")
