"""
Panchang API example (Python)
Tithi, nakshatra, yoga, karana, rahu kaal, abhijit muhurta in one call.
Docs: https://roxyapi.com/api-reference
"""

import os
from roxy_sdk import create_roxy

roxy = create_roxy(os.environ["ROXY_API_KEY"])

# Step 1: geocode the city - never hardcode coordinates
loc = roxy.location.search_cities(q="New Delhi")
city = loc["cities"][0]
latitude, longitude, timezone = city["latitude"], city["longitude"], city["timezone"]

# Step 2: detailed panchang for that location
panchang = roxy.vedic_astrology.get_detailed_panchang(
    date="2026-05-03",
    latitude=latitude,
    longitude=longitude,
    timezone=timezone,
)

print("Date:", panchang["date"])
print("Vara:", panchang["vara"]["name"], "(lord:", panchang["vara"]["lord"] + ")")
tithi = panchang["tithi"]
print("Tithi:", tithi["number"], tithi["name"], tithi["paksha"], "paksha")
nakshatra = panchang["nakshatra"]
print("Nakshatra:", nakshatra["name"], "pada", nakshatra["pada"], "(lord:", nakshatra["lord"] + ")")
print("Yoga:", panchang["yoga"]["name"])
print("Karana:", panchang["karana"]["name"])
print("Sunrise:", panchang["sunrise"])
print("Sunset:", panchang["sunset"])
rahu = panchang["rahuKaal"]
print("Rahu Kaal:", rahu["start"], "to", rahu["end"])
abhijit = panchang.get("abhijitMuhurta")
if abhijit:
    print("Abhijit Muhurta:", abhijit["start"], "to", abhijit["end"])
else:
    print("Abhijit Muhurta: null (Wednesday)")
print("Chandrabalam favorable rashis:", ", ".join(panchang["chandrabalam"]["favorableRashis"]))
