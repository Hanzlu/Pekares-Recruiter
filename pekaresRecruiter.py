#a NationStates recruitment-telegram sender made by Pekares, using the NS api
#current version: 1.2.1

#versions:
#1.0
#1.1, fixed the exceeding of rate-limit, sends telegram without opening the browser, and some smaller changes
#1.1.1 added what time a telegram was sent at, and minor changes
#1.2 doesn't send telegram to same nation twice
#1.2.1 made the code shorter
#1.3 Thanks to MilkyWay90 for their proposal. Include keys and id through input and
#tries to run the program, running it again after a minute if error was given

#to use:
#run, and fill in your "client key", "tgid" and "secret key" when asked 
#for errrors, read the README.md

import time
import urllib.request

x = 1

class old:
    old = ""

client = input("Enter client key: ")
tgid = input("Enter telegram id: ")
key = input("Enter secret key: ")


while x > 0:
    
    try:
        name = ""
    
        #page with new nations
        page = urllib.request.urlopen("https://www.nationstates.net/cgi-bin/api.cgi?q=newnations")
        content = str(page.read())
        index = content.index(",")
        name = content[23:index]
    
        #if trying to send to same nation twice
        while old.old == name:
            time.sleep(30)
            page = urllib.request.urlopen("https://www.nationstates.net/cgi-bin/api.cgi?q=newnations")
            content = str(page.read())
            index = content.index(",")
            name = content[23:index]
        
        #send telegram
        urllib.request.urlopen("https://www.nationstates.net/cgi-bin/api.cgi?a=sendTG&client=%s&to=%s&tgid=%s&key=%s" % (client, name, tgid, key))
        
        print("telegram sent to" , name, "at", time.strftime("%H:%M:%S"))
        old.old = name
    
    except:
        time.sleep(60)
        continue
    
    time.sleep(180)
