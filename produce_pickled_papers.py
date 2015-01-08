
import urllib2
import json
from pprint import pprint
import cPickle


# this string is opened by urllib2, we get a JSON file as output
searchString = "http://adslabs.org/adsabs/api/search/?q=infrared&fl=author,citation_count,title,aff&dev_key=scw4BR6QU675MSJm"

# do the request
req = urllib2.Request(searchString)
response = urllib2.urlopen(req)
the_page = response.read()

# parse the JSON output
data = json.loads( the_page )

# debug output
print "Example: " + str( data[u"results"][u"docs"][0] )

# save the data to a pickle file
cPickle.dump(data[u"results"][u"docs"], open('paperlist.p', 'wb')) 

# more debugging output
#obj = cPickle.load(open('paperlist.p', 'rb'))
#print obj[0]
#pprint( data )