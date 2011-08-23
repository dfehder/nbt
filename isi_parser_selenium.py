# Author: DFehder
# Create Date: July 11, 2011
# Purpose: See nbt.org for details
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time, os, random, sys

titler = "10.1038/nbt1096"

dicter = {"DOI":titler}
Listdicter = [dicter]

class isi_parser:
    """
    The purpose of this object is to use selenium to drive downloading of the 
    """
    
    def __init__(self, ):
        """
        Set up the necessary initalization values
        """
        self.base_url = "http://libraries.mit.edu/get/webofsci"

    def article_grabber(self,articleList):

        #establish the browser for use across the articles
        browser = webdriver.Firefox() # Get local session of firefox
        browser.get(self.base_url) # Load page
        
        for artDict in articleList:
            #check to make sure that the 
            if artDict.has_key("DOI"):

                #put in title info
                try:
                    elem = browser.find_element_by_id("value(input1)") # Find the query box
                    elem.send_keys(artDict["DOI"])

                except:
                    print "DOI Error"

                #Choose title from dropdown box
                try:
                    elem = browser.find_element_by_id("select1") # Find the drop box
                    elem.send_keys("DOI")
                except:
                    print "DOI Search option error"

                #Click search
                try:
                    elem = browser.find_element_by_xpath("//input[@alt='Search']")
                    time.sleep(random.randint(2,6))
                    elem.click()
                    time.sleep(random.randint(4,15))
                    # Let the page load, will be added to the API
                except:
                    print "Search button error"

                #click on the "times cited" href
                try:
                    time.sleep(random.randint(4,15))
                    elem = browser.find_element_by_xpath("//a[@title= 'View all of the articles that cite this one']")
                    elem.click()
                    time.sleep(15)
                except:
                    print "Cited Ref Error"
                    exit

                #read the number of references
                try:
                    elem = browser.find_element_by_xpath("//span[@id = 'hitCount.bottom']")
                    boo = elem.text
                    sizeTest = 0
                    try:
                        if int(boo)>500:
                            print artDict["DOI"] + "Has more than 500"
                            sizeTest = 1
                        else:
                            pass

                    except:
                        print "Comparison Error"
                except:
                    print "result number error"                 
                
                #start making preperations for the saving
                try:
                    elem = browser.find_element_by_xpath("//input[@value='range']")
                    elem.click()
                    time.sleep(random.randint(3,8))
                    # Enter the range
                    elem = browser.find_element_by_xpath("//input[@name = 'markFrom']")
                    elem.send_keys("1")
                    time.sleep(random.randint(3,8))

                    elem = browser.find_element_by_xpath("//input[@name = 'markTo']")
                    #ask for total records if less than 500, just 500 if more
                    if sizeTest == 0:
                        elem.send_keys(boo)
                    else:
                        elem.send_keys("500")

                    
                    #choose HTML encoding for the record
                    elem = browser.find_element_by_xpath("//select[@name='save_options']")
                    elem.send_keys("Save to HTML")
                except:
                    print "saving options error"
                    sys.exit(1)

                #more html options
                try:
                    #click the option to get full records
                    elem = browser.find_element_by_xpath("//input[@id='fullrec_fields']")
                    elem.click()
                    #click the option to get cited references
                    elem = browser.find_element_by_xpath("//input[@name='fullrec_fields_option']")
                    elem.click()
                except:
                    print "more html options errors"
                    sys.exit(1)

                #click the save button
                try:
                    elem = browser.find_element_by_xpath("//input[@alt='Save the selected records']")
                    elem.click()
                    time.sleep(random.randint(8,20))
                    # blanking the below out because I think i fixed the saving problem seperately
                    #os.system('xte "key Return"')
                except:
                    print "save button erroring"

                # loop the key return, check presence of file, loop again
                try:
                    os.system('xte "key Return"')
                    if os.path.isfile('/tmp/savedrecs.html'):
                        print "GOTIT 1"
                    else:
                        print "nope1"
                        time.sleep(5)
                        os.system('xte "key Return"')
                        if os.path.isfile('/tmp/savedrecs.html'):
                            print "GOTIT 2"
                        else:
                            print "nope2"
                            time.sleep(10)
                            os.system('xte "key Return"')
                            if os.path.isfile('/tmp/savedrecs.html'):
                                print "GOTIT 3"
                            else:
                                print "nope3"
                                time.sleep(15)
                                os.system('xte "key Return"')
                                if os.path.isfile('/tmp/savedrecs.html'):
                                    print "GOTIT 4"
                                else:
                                    print "nope4"
                                    time.sleep(25)
                                    os.system('xte "key Return"')
                                    if os.path.isfile('/tmp/savedrecs.html'):
                                        print "GOTIT 5"
                                    else:
                                        print "nope5"
                                        time.sleep(30)
                                        os.system('xte "key Return"')
                                        if os.path.isfile('/tmp/savedrecs.html'):
                                            print "GOTIT 5"
                                        else:
                                            print "nope6"
                                            time.sleep(90)
                                            os.system('xte "key Return"')
                                            if os.path.isfile('/tmp/savedrecs.html'):
                                                print "GOTIT 6"
                                            else:
                                                print "FinalNope"
                                                sys.exit(1)
                                            
                                        
                                    
                except:
                    print "Waiting game error"
                            

                #once you detect the precence of the file, save it with the right name
                try:
                    stringStart = 'mv /tmp/savedrecs.html'
                    stringMid = ' /home/dcfehder/dev/nbt/download/ISI/cf-'
                    saveString = stringStart + stringMid + artDict["DOI"][8:] + '.html'

                    os.system(saveString)
                    
                    print "do stuff here with processing the file before moving onto the next loop"
                except:
                    print "processing errors"

                #go back to the start in the same browser
                try:
                    elem = browser.find_element_by_xpath("//img[@alt='Return']")
                    elem.click()
                    time.sleep(random.randint(2,5))

                    elem = browser.find_element_by_link_text("Search")
                    elem.click()
                    time.sleep(5)

                    elem = browser.find_element_by_xpath("//img[@alt='Clear All Search Fields']")
                    elem.click()
                    
                    t = random.randint(3,20)
                    time.sleep(t)

                except:
                    print "going back to Cali error"
                    
                
                    
            else:
                print "ArtDict Error"



pdog = isi_parser()
pdog.article_grabber(Listdicter)

