# Program Details:
# This program checks for same Image & XML Names
# If present will be stored in respective outIMG & outXml
# "no" variable - Increment starts from the number assigned  
# Input format:
# python JpegXmlRename.py ImageSourcePath xmlSourcePath 


import os
from os.path import isfile, isdir, join, dirname, splitext, basename
import sys
from shutil import copyfile
import xml.etree.ElementTree as et
import time

args = sys.argv[1:]
if (args[0]=="help" or len(args)!=2):
    print("Please give correct arguments")
    print("format:python JpegXmlRename.py ImageSourcePath XMLSourcePath")
    sys.exit(0)

srcimg=args[0] #input("Enter Dataset Path")
srcxml=args[1] #input("Enter xml Path")

baseimg=[]
basexml=[]

destimg=os.path.join(os.path.split(srcimg)[0],"outIMG")
if not os.path.exists(destimg):
    os.mkdir(destimg)

destxml=os.path.join(os.path.split(srcxml)[0],"outXml")
if not os.path.exists(destxml):
    os.mkdir(destxml)


for file in os.listdir(srcimg):
    if(os.path.splitext(os.path.basename(file))[1]==".jpg"):
        baseimg.append(os.path.splitext(os.path.basename(file))[0])

for file in os.listdir(srcxml):
    if(os.path.splitext(os.path.basename(file))[1]==".xml"):
        basexml.append(os.path.splitext(os.path.basename(file))[0])
no=1


for i in baseimg:
    for j in basexml:
        if i==j:
            #os.rename(os.path.join(srcimg,i+".jpg"),os.path.join(destimg,str(no).zfill(5)+".jpg"))
            #os.rename(os.path.join(srcxml,j+".xml"),os.path.join(destxml,str(no).zfill(5)+".xml"))
            output_filename = str(no).zfill(5)
            
            copyfile(os.path.join(srcimg,i+".jpg"),os.path.join(destimg,output_filename+".jpg"))
            copyfile(os.path.join(srcxml,j+".xml"),os.path.join(destxml,output_filename+".xml"))

            # EDIT XML FILE ( Renames updated image name in xml file inside 'filename' tag)
            tree = et.parse(os.path.join(destxml,output_filename+".xml"))
            tree.find('.//filename').text = output_filename+".jpg"
            tree.write(os.path.join(destxml,output_filename+".xml"))
            no=no+1
            

print("DONE!")
