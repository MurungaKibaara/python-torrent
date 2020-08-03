from mega import Mega
from dotenv import load_dotenv, find_dotenv
from os import getenv
import glob

load_dotenv(find_dotenv())

EMAIL = getenv("EMAIL")
PASSWORD = getenv("PASS")

def upload(filename):

  mega = Mega()
  m = mega.login(EMAIL, PASSWORD)

  folder = m.find('Downloads', exclude_deleted=True)

  upload = m.upload(filename, folder[0])
  upload_link = m.get_upload_link(upload)

  print(upload_link)