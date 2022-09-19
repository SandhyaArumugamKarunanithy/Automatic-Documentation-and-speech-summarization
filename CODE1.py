#!/usr/bin/env python3

import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
# recognize speech using Sphinx
try:
    print("(you are offline not connected to internet) thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("offline could not understand audio")
except sr.RequestError as e:
    print("offline error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("we think you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("we could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
