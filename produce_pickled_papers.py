
import urllib2
import json
from pprint import pprint
import cPickle
import tools.astropersons as ap


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
print data[u"results"][u"docs"][:]

for entry in data[u"results"][u"docs"][:]:
    names = entry[u"author"]
    full_names = []
    for author in names:
        last, _, first = author.partition(',')
        if '.' in first:
            if len(first.partition('.')[0].strip()) > 1:
                continue
            else:
                print("searching for: " + author)
                search_result = ap.astropersons_search(last + ', ' + first)
                if search_result is None:
                    print("No match")
                    continue
                else:
                    print("Found match!")
                    elems = search_result.split(' ')
                    author = elems[-1] + ', '
                    for i in range(len(elems) - 1):
                        author += ' ' + elems[i]
                    print author
        full_names.append(author)

# save the data to a pickle file
cPickle.dump(data[u"results"][u"docs"], open('paperlist.p', 'wb')) 

# more debugging output
#obj = cPickle.load(open('paperlist.p', 'rb'))
#print obj[0]
#pprint( data )
