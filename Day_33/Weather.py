import requests
from datetime import datetime

def getcurrentweather(parameters={}):
    out = {
        "sunrise": "",
        "sunset": ""
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    out["sunrise"] = sunrise
    out["sunset"] = sunset
    return out

def darknessisok(location=(0.0,0.0)):
    time = getcurrentweather(parameters={"lat": location[0], "lng": location[1], "formatted": "0"})
    ok = False

    sunrise_hour = int(time.get("sunrise").split("T")[1].split(":")[0])
    sunset_hour = int(time.get("sunset").split("T")[1].split(":")[0])
    time_now_hour = datetime.now().hour
    if sunrise_hour + 5 <= time_now_hour >= sunset_hour + 3:
        ok = True

    return ok

