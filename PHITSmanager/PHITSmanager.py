import sys, string
from os import path, makedirs,getcwd,remove
from shutil import copyfile
import glob

#This function manages the creation of the PHITS project by creating 1 directory
#   - InitFiles : which contains files for the definition of
#                 * parameters
#                 * materials
#                 * source
#                 * tallies
#                 * translations
#                 * cells
#                 * surfaces

def initCreateDir(directory):
    this_dir, this_filename = path.split(__file__)
    if not path.exists(directory):
        makedirs(directory)
    if not path.exists(path.join(directory, "InitFiles")):
        makedirs(path.join(directory, "InitFiles"))
    InitFiles = [   
                path.join(this_dir,"InitFiles/cell.mod"),
                path.join(this_dir,"InitFiles/materials.mod"),
                path.join(this_dir,"InitFiles/param.mod"),
                path.join(this_dir,"InitFiles/source.mod"),
                path.join(this_dir,"InitFiles/surface.mod"),
                path.join(this_dir,"InitFiles/title.mod"),
                path.join(this_dir,"InitFiles/t-track.tally")]
    for InitFile in InitFiles:
        copyfile(InitFile, path.join(directory, "InitFiles/",path.basename(InitFile)))

#This function defines a method to copy an existing project into an other project (a sort of new branch)
def cpPHITSproject(directory):
    wkdir=getcwd()
    if checkifPHITSproject(directory,1)==1:
        return 1
    elif checkifPHITSproject(wkdir,2)==2:
        return 2
    else:
        cpfiles = glob.glob(path.join(directory,"InitFiles/*"))
        for f in cpfiles:
            try:
                copyfile(f, path.join(wkdir, "InitFiles/",path.basename(f)))
            except Exception as e:
                print "\n\033[1;34mPHITSmanager cp error:\033[1;32m %s \033[0m\n" % (e)
        return 0

def buildPHITSproject(directory=getcwd(),outputfile = "phits.inp"):
    if checkifPHITSproject(directory,1)==1:
        return 1,"no file"
    inputmodules = glob.glob(path.join(directory,"InitFiles/*.mod"))
    inputtallies = glob.glob(path.join(directory,"InitFiles/*.tally"))
    f = open(outputfile, "w")
    for mod in inputmodules:
        cf = open(mod,'r')
        f.write("\r\n"+cf.read())
        cf.close()
    for tally in inputtallies:
        cf = open(tally,'r')
        f.write("\r\n"+cf.read())
        cf.close()
    f.close()
    return 0,outputfile

#Check if a directory contains an PHITSmanager project
def checkifPHITSproject(directory,r):
    if not path.exists(path.join(directory, "InitFiles")):
        print "\n\033[1;34mPHITSmanager error:\033[1;32m %s contains no PHITSmanager project\033[0m\n" % (directory)
        return r
