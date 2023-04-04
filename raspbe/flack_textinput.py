import sqlite3
import RPi.GPIO as GPIO
from openai_1 import*
from weather_1 import*
from currency_1 import*
from time_1 import*
from polly_mmap import*
conn = sqlite3.connect('/home/Vyshnavi/Desktop/pypy/instance/database.db')
cur = conn.cursor()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
def flack_text(text):
        text=text.lower()
        print("You said:", text)
        cur.execute("SELECT Answer FROM user WHERE Question=?", (text,))
        result = cur.fetchone()
        if result is not None:
            sample=result[0]
            print(sample)
            GPIO.output(18, GPIO.LOW)
            return sample
        elif 'show me the images of' in text:
            text=text.replace('show me the images of'," ")
            webbrowser.open("https://www.google.com/search?q="+text+"&tbm=isch")
            GPIO.output(18, GPIO.LOW)
            return "As you wish"
        elif 'play' in text:
            text=text.replace('play'," ")
            pywhatkit.playonyt(text)
            GPIO.output(18, GPIO.LOW)
            return "As you wish"
        elif 'come back' in text:
            os.system("killall chromium-browser")
            GPIO.output(18, GPIO.LOW)
            return "As you wish"
        elif 'what is the weather' in text:
            weather=text.replace("what is the weather"," ")
            GPIO.output(18, GPIO.LOW)
            return(weath(weather))
        elif 'what is the currency value' in text:
            cur1=text.replace("what is the currency value"," ")
            GPIO.output(18, GPIO.LOW)
            return(kurr(cur1))
        elif 'what is the time' in text:
            GPIO.output(18, GPIO.LOW)
            return(tyme(text))
        else:
            GPIO.output(18, GPIO.LOW)
            return(intel(text))
#sample=flack_text("what is your name")
#mapy(sample)
cur.close()
conn.close()
