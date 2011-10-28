#!/usr/bin/python

import sys, os, re, shutil, fnmatch, pprint

__version__ = (0,0,1)

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
            print "\nCopying id " + str(id) + "\n"
            src = self.getFullPath(id)
            if src:
                print "\nCopying " + src + " to " + dst + "\n"
                shutil.copy(src, dst)
        print "\nDone with copy...\n"
        return True
        
    def getFullPath(self, id):
        
        id = str(id)
        end = str(int(id[0:2])+1)
        sub_folder = id[0:2] + '01-' + end + '00/'
        folder = self.source_folder + sub_folder
        fullPath = self.locate(id, folder)
        if fullPath:
            return fullPath[0]
        
    def locate(self, pattern, root=os.curdir):
        pattern = pattern + "*"
        matches = []
        for path, dirs, files in os.walk(os.path.abspath(root)):
            for filename in fnmatch.filter(files, pattern):
                matches.append(os.path.join(path, filename))
        return matches
            
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

