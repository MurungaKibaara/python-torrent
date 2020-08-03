import os
import fnmatch
from glob import glob
from contextlib import suppress
import shutil

def clean():
  localpath = './Downloads'

  for root, dirnames, filenames in os.walk(localpath):
    for filename in fnmatch.filter(filenames, '*'):
      path = os.path.realpath(filename)
      # shutil.rmtree(filename)
      print(path)

clean()

