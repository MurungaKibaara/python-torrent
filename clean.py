import os
import fnmatch
from glob import glob
from contextlib import suppress
import shutil

def clean_files():
  localpath = './Downloads'

  for root, dirnames, filenames in os.walk(localpath):
    for filename in fnmatch.filter(filenames, '*'):
      os.remove(os.path.join(root, filename))

def clean_directories():
  root = './Downloads'
  folders = list(os.walk(root))[1:]

  for folder in folders:
      if not folder[2]:
          os.rmdir(folder[0])
