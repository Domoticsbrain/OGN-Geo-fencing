# OGN-Geo-fencing
Geo-fancing code for the OGN platform
This code allows you to receive notifications via bot telegram bot when an aircraft connected to the platform OGN (http://wiki.glidernet.org) enters a pre-established area.


Step 1:
git clone https://github.com/glidernet/python-ogn-client

Step 2:
Downlaod 1 https://github.com/Domoticsbrain/OGN-Geo-fencing/blob/master/test2_github.py
Downlaod 2 https://github.com/Domoticsbrain/OGN-Geo-fencing/blob/master/aerei.csv

Put the two files inside python-ogn-client

Step 3:
Open file test_github.py

Step 4:

Change these parts:

    1.  Send text message
        bot_token = 'YOUR_API'      (You need to create a bot with Botfather and get your API key)
        bot_chatID = 'YOUR_ID'
    
    
    2. if(inRange_square(plane, 46.1368, 46.1796, 8.8374, 8.9057, 210, 1000)): #Your cordinate area
    
    
    
    
    
    
 

