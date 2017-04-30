#!/usr/bin/env python
import os
import sys
import re
from sys import argv
from pprint import pprint
from models import config
from models import destinationMainPath
from models import originMainPath



def copyAndResize( originFile, destinationFile, modelName, sizeName, factor_x, factor_y, factor_z ):

    sbOriginFile = originMainPath +'/'+ originFile
    sbDestinationFullPath = destinationMainPath + '/' + modelName +'/'+ sizeName +'/'+ destinationFile
    sbDestinationDir = destinationMainPath + '/' + modelName +'/'+ sizeName

    if os.path.exists( sbOriginFile ):

        # exist final gcode, then remove it
        if os.path.exists( sbDestinationFullPath  ):
            os.remove( sbDestinationFullPath )

        # if doesn't exist main path, remove it
        if not os.path.exists(sbDestinationDir):
            os.makedirs(sbDestinationDir)



        #if< sys.argv[3]

        i = 0
        f = open( sbOriginFile ,"r")
        copy = open( sbDestinationFullPath ,"wt")

        for l in f:


             my = re.match('(.*Y)(\-?[0-9]+\.?[0-9]?)(.*)', l)
             if my:
               l = my.group(1) +   str( float(my.group(2)) * factor_y ) +  my.group(3)


             mx = re.match('(.*X)(\-?[0-9]+\.?[0-9]?)(.*)', l)
             if mx:
                l = mx.group(1) +   str( float(mx.group(2)) * factor_x ) +  mx.group(3)


             mz = re.match('(.*Z)(\-?[0-9]+\.?[0-9]?)(.*)', l)
             if mz:
                l = mz.group(1) +   str( float(mz.group(2)) * factor_z ) +  mz.group(3)



             copy.write(str(l)+'\n')

        f.close()
        copy.close()
    else:
        print "No gcode file found:" +sbOriginFile




argv.append('FinalArgument')
if argv[1]!="FinalArgument":
    selectedModel = sys.argv[1]
    if selectedModel in config:
        for sizeKey in config['stuby']['resizes']:
            ##print config['stuby']['resizes'][sizeKey]

            size = config[ selectedModel ]['resizes'][sizeKey]
            originFiles = config[ selectedModel ]['origin']
            destinationFiles = config[ selectedModel ]['destination']
            print '\n## Converting model "'+selectedModel+'" in "'+sizeKey+ '" ##'
            copyAndResize( originFiles[0], destinationFiles[1],selectedModel ,sizeKey ,  size[0], size[1], size[2] ) # fist gcode file
            copyAndResize( originFiles[1], destinationFiles[1],selectedModel ,sizeKey ,  size[0], size[1], size[2] ) # fist gcode file
    else:
        print 'model "'+selectedModel+'" not declared. Edit models.py'
else:
    print 'Must specify a model name ex: ./resize stuby'
