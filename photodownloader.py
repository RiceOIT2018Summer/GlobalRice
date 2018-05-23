import readspreadsheet
import urllib.request
import urllib.error
from string import ascii_letters
import os

DEFAULT_FACULTY_SID = '14rWedcwXlFQdqjHw2MnAZL6qNxZYwDvZO4VF4BdrAf0'

values = readspreadsheet.read(DEFAULT_FACULTY_SID)

if not os.path.isdir('photos'):
    os.mkdir('photos')

for row in values:
    filename = ''.join([c.lower() for c in row[0] if c in ascii_letters]) + '.jpg'
    print("Downloading: "+ filename + " from " + row[5])
    try:
        urllib.request.urlretrieve(row[5], 'photos/' + filename)
    except urllib.error.HTTPError:
        print("Blocked")


