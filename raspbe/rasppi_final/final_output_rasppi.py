import speech_recognition as sr
import mmap
import time
import os
import sqlite3
import pywhatkit
import webbrowser
import RPi.GPIO as GPIO
from mm import*
from weather_1 import*
from currency_1 import*
from time_1 import*
from testing_1 import*
conn = sqlite3.connect('/home/Vyshnavi/Desktop/pypy/instance/database.db')
cur = conn.cursor()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def listen_for_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        GPIO.output(18,GPIO.HIGH)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
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
            
    except sr.UnknownValueError:
        return("Sorry, I didn't understand that.")
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except mmap.error as e:
        print("mmap error: {0}".format(e))
        # try increasing the size of the mmap
        fd = os.open("/dev/mem", os.O_RDWR | os.O_SYNC)
        size = mmap.PAGESIZE * 10
        offset = 0x3F000000
        mm = mmap.mmap(fd, size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=offset)
        os.close(fd)
        mm.seek(0)
        mm.write(b'\x00')
        mm.flush()
        mm.close()

while True:
    data=listen_for_speech()
    mapy(data)
    time.sleep(2)
    r = None
    #GPIO.cleanup()
    audio = None
    del r
    del data
