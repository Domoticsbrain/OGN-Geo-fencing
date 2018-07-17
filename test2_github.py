from ogn.client import AprsClient
from ogn.parser import parse, ParseError
import csv
import requests

def inRange_square(s, minLat, maxLat, minLon, maxLon, minAlt, maxAlt):
    if s.get('longitude', 0) < minLon or s['longitude'] > maxLon or s['latitude'] < minLat or s['latitude']>maxLat or s['altitude']<minAlt or s['altitude']>maxAlt :
        
        return False
    
    return True

def bot_sendtext(bot_message):
    
    ### Send text message
    bot_token = 'YOUR_API'
    bot_chatID = 'YOUR_ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    
    requests.get(send_text)


if __name__=="__main__":
    mydict = {}
    reader = csv.reader(open("aerei.csv", "r"))
    for rows in reader:
        k = rows[0].strip('"\'')
        v = rows[1].strip('"\'')
        mydict[k] = v

def processPlane(plane):
    if(inRange_square(plane, #minLAT, #maxLat, #minLon, #maxLon, #minAlt, #maxAlt)): #Your cordinate area
    
        print("The plane is in range")
        ground_speed = round(plane.get('ground_speed', 0.0), 0)
        altitude = round(plane.get('altitude', 0.0), 0)
        print(mydict.get(plane.get('name')[3:]), (f"{ground_speed}"), (f"{altitude}"))
        message = f"{mydict[plane['name'][3:]]} {ground_speed} {altitude}"
        bot_sendtext(message)
    else:
        
        'odd'
   
def process_beacon(raw_message):
   try:
       beacon = parse(raw_message)
       #print('Received  {raw_message}'.format(**beacon))
       processPlane(beacon)
   except ParseError as e:
       #print('Error, {}'.format(e.message))
       print( raw_message )

   
client = AprsClient(aprs_user='N0CALL')
client.connect()
   
try:
    client.run(callback=process_beacon, autoreconnect=True)
except KeyboardInterrupt:
    print('\nStop ogn gateway')
    client.disconnect()


   

