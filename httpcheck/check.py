import time
import urllib

var = 1
while var==1:
   try:
      print urllib.urlopen("http://quotes.prys.me.uk:3412/quote/random").getcode()
   except IOError:
      print "Error accessing website"
   time.sleep(5)

