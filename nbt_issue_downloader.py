## Author: D Fehder
## Created: 6/21/2011
## Purpose: Described in nbt.org file
import urllib, re, os, random, time

## Initializations
urlbase = "http://www.nature.com"

Filebase = "/home/dcfehder/dev/nbt/download"

#So this is the file that i will be reading lines off of
logger = open('/home/dcfehder/dev/nbt/nbt_issue_list.txt','r')



#generate a list of random numbers
rand_int_dict = {}

for int in range(random.randint(3,20)):
    a = random.randint(1,352)
    if rand_int_dict.has_key(a):
        pass
    else:
        rand_int_dict[a]= ""

print rand_int_dict

#this function will grab the url
def issue_index_grab(liner, urlbase, Filebase):
    "The point of this function is to grab the index"
    line = liner.rstrip('\r\n')
    filename = Filebase + line
    urlname = urlbase + line
    
    if os.path.exists(filename):
        print "file"+ filename + "already exists" 
    else:
        try:
            path = Filebase + line.rstrip("/index.html")
            if os.path.exists(path):
                print path + "  already exists"
                
                urllib.urlretrieve(urlname,filename)
            else:
                try:
                    os.makedirs(path)
                    urllib.urlretrieve(urlname,filename)
                except:
                    print "fail 3"
                
            
        except:
            print "something wrong in the downloading"

    return


#Not use the dict of random numbers to select which lines to import from
counter = 1
for line in logger:
    
    if rand_int_dict.has_key(counter):
        try:
            issue_index_grab(line,urlbase,Filebase)
            t = random.randint(3,20)
            time.sleep(t)
            print t
        except:
            print "Something wrong with issue grab"
    else:
        pass
    
    
    counter = counter + 1



## finish stuff up
logger.close()

## We will define a function that checks for the existence of a file. if it does not exist, then it downloads it

## Begin by creating a class that takes the url file ref and changes it to windows based address if necessary







