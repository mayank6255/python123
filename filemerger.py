#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:49:37 2017

@author: mayankparitosh
"""

import sys

fd = open( sys.argv[1], "rb" )
file_contents = fd.read()
fd.close()
print ("[*] Filesize: %d" % len( file_contents ))
# Now write it out to the ADS
fd = open( "%s:%s" % ( sys.argv[2], sys.argv[1] ), "wb" )
fd.write( file_contents )
fd.close()
