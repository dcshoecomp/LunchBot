import sys
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={1}&radius={2}type=restaurant&fields=name&key={0}'.format(sys.argv[1],sys.argv[3],sys.argv[4])
print(url)