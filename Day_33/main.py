from Location import getmyloc
import requests
from datetime import datetime
from Weather import darknessisok
from Location import tolarablediffernce
from Location import getissloc
from Sender import sendmail

#mods - remote = automatic --> 0
#       user = input -- > 1

program_mode = 0

if program_mode == 0:
    #first - Get the current loc
    loc = getmyloc()
    MY_LAT = loc.get("lat")
    MY_LONG = loc.get("lon")
    my_position = (MY_LAT,MY_LONG)

    #second - Get the darkness
    we_can_see_anything = darknessisok(location=my_position)

    #third - Get the current position of iss
    iss_position = getissloc()

    #fourth - Check the difference between us and the iss
    iss_is_over_head = tolarablediffernce(iss_location=iss_position,my_location=my_position)

    #fifth - Check is everything good
    if we_can_see_anything and iss_is_over_head:
        sendmail()

    elif we_can_see_anything == False:
        print(f"Currently you can't see not much uppon the cloud, 'cause the current time is: \n{datetime.now()}")

    elif iss_is_over_head == False:
        print(f"The Internation Space Station 'ISS' not near to you.\nThe current location of iss is: \nLangtitude: {iss_position[0]}\nLongtitude:{iss_position[1]}")

elif program_mode == 1:
    #zero - Ask the user for his/her geo loc datas
    correct = False
    user_lat = ''
    user_lon = ''
    while not correct:
        user_lat = input("Type your Latitude here: ")
        user_lon = input("Type your Longitude here: ")
        lat_is_ok = False
        lon_is_ok = False
        alpha_index = []
        for char in user_lat:
            if char.isalpha():
                alpha_index.append(True)
        for char in user_lon:
            if char.isalpha():
                alpha_index.append(True)
        if True in alpha_index:
            correct = False
        else:
            correct = True

    #first - Get the current loc
    loc = getmyloc()
    MY_LAT = loc.get("lat")
    MY_LON = loc.get("lon")
    my_position = (MY_LAT,MY_LON)

    #second - Get the darkness
    we_can_see_anything = darknessisok(location=my_position)

    #third - Get the current position of iss
    iss_position = getissloc()

    #fourth - Check the difference between us and the iss
    iss_is_over_head = tolarablediffernce(iss_location=iss_position,my_location=my_position)

    #fifth - Check is everything good
    if we_can_see_anything and iss_is_over_head:
        sendmail()

    elif we_can_see_anything == False:
        print(f"Currently you can't see not much uppon the cloud, 'cause the current time is: \n{datetime.now()}")

    elif iss_is_over_head == False:
        print(f"The Internation Space Station 'ISS' not near to you.\nThe current location of iss is: \nLangtitude: {iss_position[0]}\nLongtitude:{iss_position[1]}")