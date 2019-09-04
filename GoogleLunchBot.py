import time
import requests
import json
import random
import sys
#arg1=google api key
#arg2= ms teams post url
#arg3=gps coords
#arg4=distance radius in meters

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={1}&radius={2}&type=restaurant&fields=name&key={0}'.format(sys.argv[1],sys.argv[3],sys.argv[4])
headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36'}
r = requests.Session()
gplaces = r.get(url, verify=False, headers=headers)
print(gplaces.status_code)
if "next_page_token" in gplaces.json():
    nextpagetoken = gplaces.json()['next_page_token'] 
    time.sleep(5)
else:
    nextpagetoken = None
pageresults = gplaces.json()['results']

while nextpagetoken is not None:
    print('started a while loop')
    nextpageurl = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={0}&pagetoken={1}'.format(sys.argv[1],nextpagetoken)
    nextpagetoken = None
    gplaces = r.get(nextpageurl, verify=False, headers=headers)
    if "next_page_token" in gplaces.json():
        nextpagetoken = gplaces.json()['next_page_token'] 
        print('got nextpage')
        time.sleep(5) #there must be a timeout or google wont return the next page
    else:
        nextpagetoken = None
        print('didnt find a nextpage')

    for place in gplaces.json()['results']: #iterate the new places and add one by one to the fist page results
        pageresults.append(place)
        print('appending the pageresults {0}'.format(place['name']))

rand=random.randint(0,len(pageresults))
print(rand)
suggestion = 'Rating:{0} located at <a href="https://www.google.com/maps/place/?q=place_id:{1}">{2}</a>'.format(pageresults[rand]['rating'],pageresults[rand]['place_id'],pageresults[rand]['vicinity'])
teamsLunchBot = '{0}'.format(sys.argv[2])
payload={
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "ff0000",
    "title": format(pageresults[rand]['name']),
    "text":suggestion
}
print(suggestion)
#teams_response = r.post(teamsLunchBot, verify=False, headers=headers, json=payload)

#for place in pageresults:
#    place['name']
#
#
# {
#    "geometry": {
#       "location": {
#          "lat": 41.449036,
#          "lng": -81.49701
#       },
#       "viewport": {
#          "northeast": {
#             "lat": 41.45052,
#             "lng": -81.49565
#          },
#          "southwest": {
#             "lat": 41.447823,
#             "lng": -81.49835
#          }
#       }
#    },
#    "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
#    "id": "9edf867eafcd7bc58f2544d0671a2c95e2f874e6",
#    "name": "Olive Garden Italian Restaurant",
#    "opening_hours": {
#       "open_now": true
#    },
#    "photos": [
#       {
#          "height": 1000,
#          "html_attributions": [
#             "<a href=\"https://maps.google.com/maps/contrib/108247685945935817043/photos\">Olive Garden Italian Restaurant<\/a>"
#          ],
#          "photo_reference": "CmRaAAAAZSADjgR_1aePryk-U9LNhY3nYFWWn22q6oxIxijJkJe8qtQk_AJTuNEDvVyMddi0uTvfIfxf8pwT3HBDkHej9O5913oZ2AKp39K_iCQbQI-ya91Sxk-brJ_hxaPlggXwEhBskc4yH5rdPumdrVw661IjGhTa8sX1R3GZ0bUDuGjieGvH04NrYA",
#          "width": 1000
#       }
#    ],
#    "place_id": "ChIJAxCSUrQCMYgRbCbiE0s1mzk",
#    "plus_code": {
#       "compound_code": "CGX3+J5 Beachwood, Ohio, United States",
#       "global_code": "86HWCGX3+J5"
#    },
#    "price_level": 2,
#    "rating": 3.8,
#    "reference": "ChIJAxCSUrQCMYgRbCbiE0s1mzk",
#    "scope": "GOOGLE",
#    "types": [
#       "meal_takeaway",
#       "bar",
#       "restaurant",
#       "food",
#       "point_of_interest",
#       "establishment"
#    ],
#    "user_ratings_total": 2215,
#    "vicinity": "26000 Harvard Road, Beachwood"
# }