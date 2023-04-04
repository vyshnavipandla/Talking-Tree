from requests_html import*
from polly import*
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
#weath("snoopy")

    
#weath("newyork")
#print(weath("newyork"))

#polly(w)
