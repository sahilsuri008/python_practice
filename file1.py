#!/usr/bin/python

import os

#names=open('file.txt') -> read content
#names=open('file.txt', 'w') -> overwrites existing content
names=open('file.txt', 'r+w')
names.seek(-1,os.SEEK_END) #get cursor position to last line

names.write('\nFor your eyes only\n')
names.write('Dr.No\n')


#Write function will overwrite existing content
#names.write('Spectre\n')
#names.write('Moonreker\n')

#for  name in names:
#	print(name)

#print(names.read())
