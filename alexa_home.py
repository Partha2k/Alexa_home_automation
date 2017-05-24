
# ==========Smart Home Automation powered by Alexa Created by Parthasarathi Das=========== 
# =======importing necessary libraries ===========

import logging
import RPi.GPIO as GPIO
import time
from flask import Flask
from flask_ask import Ask, question, statement, session

# =======initializing Board Pins and server settings=========
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setwarnings(False)

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

# ======creating intent handler functions=========

@ask.launch

def enter_home():
    return question("Welcome to Cygnus Home Automation powered by Amazon Alexa. How can I be in your service?")

@ask.intent("LightOnIntent")

def light_on():
    if GPIO.input(18) == True:
       return question("The Light is turned on already. Do you want me to Turn it off?")
    else:
       GPIO.output(18, True)
       return question("The Light is now turned ON. Do you want me to do anything else?")

@ask.intent("LightOffIntent")

def light_off():
    GPIO.output(18, False)
    return question("The light has been turned off. Do you want me to do anything else?")


@ask.intent("FanOnIntent")

def fan_on():
    if GPIO.input(17) == True:
       return question("The Fan is up and running already. Do you want me to Turn it off?")
    else:
       GPIO.output(17, True)
       return question("The Fan is now up and running. Do you want me to do anything else?")

@ask.intent("FanOffIntent")

def fan_off():
    GPIO.output(17, False)
    return question("The Fan has been turned off. Do you want me to do anything else?")


@ask.intent("ACOnIntent")

def ac_on():
    if GPIO.input(22) == True:
       return question("The Air Conditioner is up and running already. Do you want me to Turn it off?")
    else:
       GPIO.output(22, True)
       return question("The Air Conditioner is now turned ON. Do you want me to do anything else?")

@ask.intent("ACOffIntent")

def ac_off():
    GPIO.output(22, False)
    return question("The Air Conditioner has been turned off. Do you want me to do anything else?")


@ask.intent("MusicOnIntent")

def music_on():
    if GPIO.input(23) == True:
       return question("The music system is playing its beats already. Do you want me to Turn it off?")
    else:
       GPIO.output(23, True)
       return question("The music system is now online. Do you want me to do anything else?")

@ask.intent("MusicOffIntent")

def music_off():
    GPIO.output(23, False)
    return question("The music system has been turned off. Do you want me to do anything else?")

@ask.intent("WhoIntent")

def creator_skill():
    return statement("This skill is created by Mister Das.")

@ask.intent("AMAZON.StopIntent")

def stop():
    return statement("Shutting down Now.")

@ask.session_ended

def session_ended():
    return "{}",200

# ======== setting server host and port =========

if __name__ == '__main__':

     app.run(host='0.0.0.0',port=80, debug =True)

GPIO.cleanup() 


