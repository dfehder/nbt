# Author: D Fehder
# Create Date: 7/2/2011
# Purpose: To parse the data from the index pages of the websites
import os
import sys
from UserDict import UserDict
import re
from BeautifulSoup import BeautifulSoup

class FileInfo(UserDict):
    "store file metadata"
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename


class issueIndexParser(FileInfo):
    " This class takes the index.html file from each issue and then creates returns a list of dictionaries with one of its methods"
    
    def __init__(self):
        """
        define the internal list that will be used to collect the initial parse
        """
        self.searcher = ["here", "there"]

    def IndexParse(self, htmlPath):

        f = open(htmlPath)
        page = f.read()
        l = page.split("\n")
        pager = "".join(l)

        #No for the re. First define the search pattern, then
        pattern = r'<tr><td colspan="2" valign="top"><.*?></a><span class="articletitle">.*?</span>&nbsp;<span class="pagenum"><b>.*?</b></span><br><span class="author">.*?</span>.*?</td></tr>'
        pattern_obj = re.compile(pattern)
        self.searcher = pattern_obj.findall(pager)

        
    def ISIprep(self):
        """
        This function will process list created by the IndexParse method and create a list of dictionaries that can be processes by the 
        """        


        


#compile the search string for author information and run the search on the who webpage using re.search

#pattern = r'<tr><td colspan="2" valign="top"><a name=.*?></a><span class="articletitle">.*?</span>&nbsp;<span class="pagenum"><b>.*?</b></span><br><span class="author">.*?</span><br><span class="doi">.*?<br></span><a class="contentslink" href=".*?">PDF.*?(.*?).*?</a></td></tr>'

#pattern = r'<span class="articletitle">.*?</span>&nbsp;<span class="pagenum"><b>.*?</b></span><br><span class="author">.*?</span>'


#pager = re.sub("\n", "", page)

#searcher = pattern_obj.findall(page)
