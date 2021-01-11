import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning Arjav")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon Arjav")
    else:
         speak("Good Evening Arjav")
    speak("I am jarvis , How may i help you ?")
            
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  
        r.pause_threshold = 1
        audio = r.listen(source) 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e :
        speak("I am sorry , say that again please")
        return "None"
    return query                 




if __name__ == "__main__":
    
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching wikipedea')
            query = query.replace("wikipedea","")
            result = wikipedia.summary(query,sentences = 2)
            speak("According to wikipidia")
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open('google.com')
            
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'open whatsapp' in query:
            webbrowser.open('whatsappweb.com')
        elif 'open my online class' in query:
            webbrowser.open('gmail.com')   
        elif 'play music' in query:
            #link dalni hai
            speak("meko bata toh ganne kaha save hai bsdk")
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'open code' in query:
            speak('add path')
        elif 'thank you jarvis' in query:
            speak("its my pleasure sir!!")    
        elif 'jarvis say' in query:
            answer = query.replace("jarvis say ", " ")
            speak(answer)     
        elif 'jarvis se' in query:
            answer = query.replace("jarvis se ", " ")
            speak(answer)     
        elif 'jarvis text my girlfriend' in query:
            speak('Sorry sir but you dont have any girlfriend')     
        elif 'jarvis who are you' in query:
            speak("I am an Virtual assistance designed by Arjav Sethi ,i am under devlopment and  will do many things later")
   
           
                
     
