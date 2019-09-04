# Introduction 
This is a bot that takes a location and radius and returns a list of resturants, it will then do a post request to a url. URL post format is based on microsoft Teams 

# Getting Started
1.	Install python3
2.	Only requirement is pypi.org/projects/requests pip3 install requests --user
3.	google places API project setup on an account, you get a small number of requests free, good for once a day processsing
    Create a project https://console.developers.google.com enable the Places API, and generate the credentials for an API Key
    
googleAPI_Key https://console.developers.google.com
msTeams_Post_URL create a bot that uses incoming post URL
GPS_coordinates in the google maps dropped pin format of xx.xxxxx,-xx.xxxxxx 
Search_Radius in Meters

# Build and Test
python3 GoogleLunchBot.py $(googleAPI_Key) $(msTeams_Post_URL) $(GPS_coordinate) $(Search_Radius).


# Contribute
TODO: 
