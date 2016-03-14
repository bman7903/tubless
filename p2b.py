#!/usr/bin/env python
### for converting images to base64 for all sorts of good reasons
import sys,base64,os

ARGS = sys.argv
lA = len(ARGS)
Usage = './p2b.py </path/to/img.png>'

def Exit():
  print(Usage)
  sys.exit()

if lA == 0:
  Exit()

def sixfo(img):
  icn = open(img, 'rb')
  icondata = icn.read()
  icondata = base64.b64encode(icondata)
  return icondata

try:
  file = str(sys.argv[1])
except:
  pass

base = str(sixfo(file))
print(base)
