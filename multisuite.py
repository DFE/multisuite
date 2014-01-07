#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# multisuite tests many suits in one run
#
# Copyright (C) 2014 DResearch Fahrzeugelektronik GmbH
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version
# 3 of the License, or (at your option) any later version.
#

"""
Run test suites independently to allow separate pip requirements for each
suite.
"""

import nose.core as nc
import argh

def test():
    print nc.TestProgram().success

def greet():
    print "hi, handsome"

def pwd():
    from subprocess import call
    call(["pwd"])

if __name__ == "__main__":
    argh.dispatch_commands([test, greet, pwd])
