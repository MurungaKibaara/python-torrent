from mega import Mega
from dotenv import load_dotenv, find_dotenv
from os import getenv
import os
import fnmatch
from clean import clean_files, clean_directories

load_dotenv(find_dotenv())

EMAIL = getenv("EMAIL")
PASSWORD = getenv("PASS")

def upload():

  mega = Mega()
  m = mega.login(EMAIL, PASSWORD)

  localpath = './Downloads'

  list_of_files = []

  for root, dirnames, filenames in os.walk(localpath):
    for filename in fnmatch.filter(filenames, '*'):
        list_of_files.append(os.path.join(root, filename))
  latest_file = max(list_of_files, key=os.path.getctime)

  folder = m.find('Downloads', exclude_deleted=True)

  upload = m.upload(latest_file, folder[0])
  upload_link = m.get_upload_link(upload)

  clean_files()
  clean_directories()

  print(upload_link)
