import time
import urllib

var = 1
while var==1:
	print urllib.urlopen("http://quotes.prys.me.uk:3412/quote/random").getcode()
	time.sleep(5)

