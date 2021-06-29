import pygeoip
import requests


def getmyloc():
    ip = {
        "lat": '',
        "lon": ''
    }
    gip = pygeoip.GeoIP('GeoLiteCity.dat')
    my_public_ip = requests.get('https://api.ipify.org').text
    res = gip.record_by_addr(my_public_ip)
    ip['lat'] = res['latitude']
    ip['lon'] = res['longitude']

    return ip

def getissloc():
    loc = []

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    ISS_LON = response.json()["iss_position"]["longitude"]
    ISS_LAN = response.json()["iss_position"]["latitude"]
    loc.append(ISS_LAN)
    loc.append(ISS_LON)
    loc = tuple(loc)

    return loc

def tolarablediffernce(iss_location=(0.0,0.0),my_location=(3.4,11.0)):
    tolarable_differnce = (2, 2)
    ml = tuple(map(lambda i,j: i-j,my_location,tolarable_differnce))
    if ml[0] <= float(iss_location[0]) <= ml[1] and ml[0] <= float(iss_location[1]) <= ml[1]:
        return True
    else:
        return False
