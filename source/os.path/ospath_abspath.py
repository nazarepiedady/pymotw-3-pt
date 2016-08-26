#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Compute an absolute path from a relative path.
"""

#end_pymotw_header

import os
import os.path

os.chdir('/tmp')

PATHS = [
    '.',
    '..',
    './one/two/three',
    '../one/two/three',
]

for path in PATHS:
    print('%17s : "%s"' % (path, os.path.abspath(path)))
