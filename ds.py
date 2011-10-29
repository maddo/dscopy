#!/usr/bin/python

import shutil
import glob
import sys
import os
import re

__version__ = (0,0,3)

"""
Pass DS games from external to interal folder based on associated id
"""

PROMPT = "(Please Choose) > "

class FileMover:
    ids                 = []
    source_folder       = """/Volumes/Freeside/NintendoDS/"""
    destination_folder  = """/Users/maddo/transferToNintendo/"""
    
    def __init__(self, ids):
        self.ids = ids
        
    def copyAll(self):
        dst = self.destination_folder
        for id in self.ids:
            print "\nCopying id %s\n" % (id)
            src = self.getFullPath(id)
            if src:
                filename =  src.split('/').pop()
                final_dst = dst + filename[7:]
                print "\nCopying %s to %s\n" % (src, final_dst)
                shutil.copy(src, final_dst)
        print "\nDone with copy...\n"
        return True
        
    def getFullPath(self, str_id):
        id = int(str_id)
        rangeStart = (id/100)*100 + 1
        rangeEnd = (id/100)*100 + 100
        sub_folder = "%0*d-%0*d/" % (4,rangeStart,4,rangeEnd)
        folder = self.source_folder + sub_folder
        fullPath = glob.glob(folder + str_id + '*')
        if fullPath:
            return fullPath[0]

            
class Menu:

    ids = None

    def __init__(self):
        pass

    def run(self):
        run = True
        while run:
            if self.displayInputMenu():
                print "\nSending...\n"
                c = FileMover(self.ids)    
                c.copyAll()
            else:
                print "\n**Something didn't work...**\n"
            print "========================================"
            print "Done?"
            print "========================================"
            print "If you want to quit, hit CTRL-C (^C)."
            print "If you want to copy more files, hit RETURN."
            raw_input("?")

    def displayInputMenu(self):
        print "========================================"
        print "Please enter id(s) separated by spaces"
        print "========================================"
        ids = raw_input("?")
        self.ids = ids.split(' ')
        return True

m = Menu()

try:
    m.run()
except:
    print "\n\nHasta la vista baby!"

