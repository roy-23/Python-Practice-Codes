import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

''' (Microsoft speech API page)   We use sapi5 to get the voices
Our windows gives us an API so that we can get voices...There are inbuilt voices in windows '''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:
        speak('Good morning ')
    elif hour>=12 and hour <18:
        speak('Good afternoon ')
    else :
        speak('Good evening')

    speak('How you doin! ')


'''Its takes microphone input from the user
and returns string output'''
def takeCommand():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        rec.pause_threshold = 1
        rec.energy_threshold =300
        audio = rec.listen(source)
    
    try:
        print('Recognizing.....')
        query =rec.recognize_google(audio,language='en-in')
        print(f'Me : {query}\n')
    except Exception as e:
        # print(e)
        print('Say that again please...')
        return 'None'
    
    return query 

if __name__ == '__main__':
    
    wish()
    listen = True
    while listen:
        query = takeCommand().lower()

    ## LOGIC FOR EXECUTING TASKS BASED ON QUERY ##

        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query =query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("Acoording to wikipedia")
            print(results)
            speak(results)
        elif 'how are you' in query:
            speak('I  am great. How can I help you ? ')
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open('google.com')
        elif 'open stack overflow' in query:
            speak('Opening Stack Overflow')
            webbrowser.open('stackoverflow.com')
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f'The time is {time}')
            print(time)
     
        
        else:
            speak('Have a nice day')
            listen = False