import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 28.624430 # Your latitude
MY_LONG = 77.352127 # Your longitude

MY_EMAIL = "frostpie4@gmail.com" # Your Email
MY_PASSWORD = "jdbvlvnvrskfnobj" # Your Password

# is_iss_overhead() function returns bool on the basis, if ISS is above you in the sky or not
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    return (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5)

# is_night() function returns bool if it is night time or not in your place
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, # formats time in 24-hour format
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now() # Current time
    hour_now = time_now.hour # Current hour

    return hour_now <= sunrise or hour_now >= sunset

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:ISS Overhead👆\n\nThe ISS is above you in the sky. Go spot the ISS."
            )