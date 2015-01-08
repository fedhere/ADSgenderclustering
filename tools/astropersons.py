#!/usr/bin/env python

def astropersons_search(name):
    """Search astropersons database to retrieve person information
        For now, returns fullname of first hit in database (or None if not found)
    """
    import urllib2

    search_name = name.replace(' ', '+')
    baseString = "http://ads.harvard.edu/cgi-bin/search_persons.sh?cases=ignore&words=substring&fuzzy=exact&name="
    req = urllib2.Request(baseString + search_name)
    response = urllib2.urlopen(req)
    page = response.readlines()

    fullname = None

    for line in page:
        if 'Name: ' in line:
            print(line)
            fullname = line.partition(r'Name: </td><td>')[2].partition(r'</td')[0]
            break

    return fullname
    

if __name__ == "__main__":
    import sys
    print(astropersons_search(sys.argv[1]))
