"""In weather_1.py file user asks the weather condition in some location with the keyword " what is the weather" 
we import "request_html" module and we define "weath" function ,passed the "location"{city name} argument.
in try block its returns the temparature,humidity,wind speed of the location.
If any error occurs it will be handled by the exception."""

from requests_html import*
s= HTMLSession()
def weath(location):
	try:
		url= f"https://www.google.com/search?q=current+weather+in+{location}"
		r= s.get(url, headers={'User-Agent' : 'Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})
		temp=(r.html.find('span#wob_tm.wob_t.q8U8x',first=True).text)
		humid=(r.html.find('span#wob_hm',first=True).text)
		wind=(r.html.find('span#wob_ws.wob_t',first=True).text)
		return(f"The weather {location} is generally typical, with an average temperature of around {temp}°C and a moderate level of humidity {humid}, while the wind speed is {wind}")
		#return weather
	
	except AttributeError:
		return("The attribute my_attribute does not exist on my_object")

    

