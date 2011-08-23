## Author: D Fehder
## Last Modified: 6/21/2011
## Purpose: described in nbt.org in this folder
import urllib2, sys, urllister, re
from sgmllib import SGMLParser


if "C:\\Users\\dfehder\\Documents\\dev\\nbt" not in sys.path:
    sys.path.append("C:\\Users\\dfehder\\Documents\\dev\\nbt")

## This is the seed page for all of the urls for the various editions of the journal
    
sock = urllib2.urlopen(r"file:///C:/Users/dfehder/Documents/dev/nbt/nbt_archive_index.html")

parser = urllister.URLLister()
parser.feed(sock.read())



## Now we want to print the data

logger = open(r'C:\\Users\\dfehder\\Documents\\dev\\nbt\\nbt_issue_list.txt','w')

## set the pattern for the re where it will only find the issue urls

patterner = "^/nbt/journal/v[1-9][0-9]*"

for url in parser.urls:
    if re.search(patterner,url):
        url2 = url + "\n" 
        logger.write(url2)
    else:
        pass


logger.close()
sock.close()
parser.close()


