#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Dgtk_doc=false \
                          -Dman=false")

def build():
    mesontools.build()


def install():
    mesontools.install()

    pisitools.dodoc("README", "COPYING", "AUTHORS", "NEWS", "ChangeLog")
