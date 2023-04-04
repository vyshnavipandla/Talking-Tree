"""In currency_1.py file "request_html" is a module that allows you to easily scrape web pages by making HTTP requests and 
parsing the HTML content.
we define "kurr" function and we passed "query" argument.
try exception method is used ,In try block,query,currency value and currency name are return,
if any error in try block ,error will be handled by exception and its returns some text.
To ask "query" the keyword is "what is the currency value of"."""

from requests_html import*
#from polly import*
s= HTMLSession()
def kurr(query):
    try:
         url= f"https://www.google.com/search?q=+{query}"
         r = s.get(url, headers={'User-Agent' : 'Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})
         currenc_y=(r.html.find('span.DFlfde.SwHCTb',first=True).text)
         currency_name=(r.html.find('span.MWvIVe.nGP2Tb',first=True).text)
	    
         #print(currenc_y,currency_name)
         return f"hmm  i guess currency value of {query} is {currenc_y} {currency_name}"
    except AttributeError:
        return("sorry,please use the proper syntax")
        

#print(cur(" "))
#data=cur("snoopy")
#print(data)


#DFlfde.SwHCTb



