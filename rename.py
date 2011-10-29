#!/usr/bin/python

import shutil
import glob
import sys
import os
import re
import pprint

folder  = "/Users/maddo/transferToNintendo/"
print("%s[0-9].*" % folder)
for file in glob.iglob("%s*.nds" % folder):
	filename =  file.split('/').pop()
	filename = filename[7:]
	shutil.move(file, folder + filename)