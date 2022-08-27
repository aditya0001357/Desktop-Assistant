import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import smtplib

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice', voice[0].id)

# takes input text and speaks it
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



#Takes microphone input from the user, and returns string output ---reverse of the above function
def takeCommand():
    r = sr.Recognizer()#check out Recognizer and get some basic details
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12:
        speak("Good Morning!")
    elif hour > 12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    
    speak("I am Jarvis, How may I help you")



#for it to work, the less secure apps should be enabled in the sending email address.
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sender's email adres", "pasword")
    server.sendmail("sender's email adres", to, content)
    server.close()




if __name__ == "__main__":
     
    wishMe()

    while True:
        query = takeCommand().lower() # converts the text obtained from speec into lower case.
                                      # Helpful when we use for searching any string.

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2) # gets only 2 sentences info from wiki.
            speak("According to wikipedia...")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open stackoverflow' in query :
                webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = '' # url of the file
            songs = os.list(music_dir) #all files in the given directoriy will be returned in the form of a list 
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"Sir, the time is : {strTime}")


        elif 'open code' in query:
            codePath = "" #url of the vscode application
            os.startfile(codePath)


        elif 'send an email' or 'create an email' in query:
            try:
                speak("Please speak out the email content, sir")
                content = takeCommand()
                speak("Who should I send this email to ?")
                emailAdr=takeCommand()
                sendEmail(emailAdr, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, the email coudn't be sent!")

        elif 'quit jarvis' in query:
            exit