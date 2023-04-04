from requests_html import*
s= HTMLSession()
def tyme(query):
    try:
         url= f"https://www.google.com/search?q=+{query}"
         r = s.get(url, headers={'User-Agent' : 'Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})
         #currenc_y=(r.html.find('div.gsrt.vk_bk.FzvWSb.YwPhnf',first=True).text)
         tym_city=(r.html.find('div.vk_gy.vk_sh',first=True).text)
         if 'Feedback' in tym_city:
            tym_city=tym_city.replace("Feedback"," ")
            return(tym_city)
         #return f"hmm  i guess currency value of {query} is {currenc_y} {currency_name}"
    except AttributeError:
        return("sorry,please use the proper syntax")
#tyme("what is the time in kuwait")
        

