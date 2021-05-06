# Pablo Sanchez
# Python version 2.7.16
# Weather API


# The wind direction and wind chill in Fahrenheit for the New York, La Guardia Airport.
# NOTE: replaced Wind Chill with Wind Speed as Wind Chill is no longer available.

import pywapi
import pprint

pp = pprint.PrettyPrinter(indent=4)
weather = pywapi.get_weather_from_noaa('KLGA')
loc1 = 'New York, La Guardia Airport'
loc2 = 'Bartlesville Municipal Airport'

print('Weather details for ' + loc1 + '.')
pp.pprint('Wind Direction: ' + weather['wind_dir'])
pp.pprint('Wind Speed: ' + weather['wind_mph'])
print ('-'*50)

# The longitude, latitude, and dew point in Fahrenheit for Bartlesville Municipal Airport.

weather = pywapi.get_weather_from_noaa('KBVO')
print('Weather details for ' + loc2 + '.')
pp.pprint('Latitude: ' + weather['latitude'])
pp.pprint('Longitude: ' + weather['longitude'])
pp.pprint('Dew Point: ' + weather['dewpoint_f'])