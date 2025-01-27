#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure('--disable-static')

    # Disable rpath
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

    shelltools.cd("src")
    shelltools.system("gcc $CFLAGS $LDFLAGS -I.. -Ilibgnu -o localepaper localepaper.c libgnu/.libs/libgnupaper.a")

def install():
    autotools.install()

    pisitools.dolib("src/localepaper")

    for lang in shelltools.ls("debian/po/*.po"):
        pisitools.domo(lang, shelltools.baseName(lang).replace(".po", ""), "libpaper.mo")

    pisitools.dodoc("README", "ChangeLog")
