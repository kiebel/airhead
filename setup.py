#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
"""
Airhead - Python based ActiveSync Server
========================================

The Airhead project implements an ActiveSync server. It is intended to be a
light solution that is easy to install, configure and use. The objective is to
provide an ActiveSync server that can be used as either standalone server or a
module for other projects (e.g. Radicale see http://www.radicale.org).

Airhead runs on most of the UNIX-like platforms (Linux, BSD, MacOS X) and
Windows. It is free and open-source software, released under GPL version 3.
"""

from distutils.core import setup
import airhead

# TODO 20121116[kiebel]: add further information about version changing
setup(
    name="Airhead",
    version=airhead.VERSION,
    description="Python based ActiveSync Server",
    long_description=__doc__,
    author="Thomas Kiebel",
    author_email="tomuchan76@gmail.com",
    url="http://github.com/kiebel/airhead/",        # FIXME 20121116[kiebel]: change to appropriated URL
    download_url=("%s" % airhead.VERSION),          # FIXME 20121116[kiebel]: change to appropriated URL
    license="GNU GPL v3",
    platforms="Any",
    packages=["airhead", "airhead.providers", "airhead.server"],
    provides=["airhead"],
    scripts=["/bin/airhead"],
    keywords=["activesync", "email", "contacts", "calendar", "tasks", "synchronisation"],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End user/Desktop",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Office/Business :: Groupware"])
