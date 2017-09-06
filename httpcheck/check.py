import httplib
import time

var = 1
while var==1:
	conn = httplib.HTTPConnection("quotes.prys.me.uk:3412")
	conn.request("HEAD", "/")
	r1 = conn.getresponse()
	if str(r1.status) != "200":
		print "broken"
	time.sleep(5)

