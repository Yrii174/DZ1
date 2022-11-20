from os.path import exists
from blok1 import creating
from blok2 import writing_scv
from blok2 import writing_txt


path = 'Phone.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()