import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import os
import random 
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
#print(voices[0].id)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour  = int(datetime.now().hour)
    if hour>=0  and hour <12:
        speak("Good Morning!")
    
    elif hour>=12  and hour <18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    

    speak("I am Robo 2020.1 Sir. Please tell me how could i help you?")


def takeCommand():
    #it takes microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing.....")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said:{query}\n")
        

        except Exception as e:
           # print(e)
            print("Say that again please.......")
            return "None"
        return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.login('rob1510697@gmail.com','')
    server.sendmail('rob1510697@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
   wishme()
   while True:
       query = takeCommand().lower()
       #Login for executing tasks based on query

       if 'wikipedia' in query:
           speak('Searching Wikipedia....')
           query = query.replace("wikipedia","")
           results =wikipedia.summary(query,sentences =2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
       
       elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        

       elif 'open google' in query:
            webbrowser.open("www.google.com")

       elif 'open my university' in query:
            webbrowser.open("www.cuet.ac.bd")
        

       elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")



       elif 'play music' in query:
            music_dir ='D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            num =random.randint(0,25)
            os.startfile(os.path.join(music_dir,songs[num]))


       elif 'the time' in query:
            strTime =datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        

       elif 'open code editor' in query:
           codepath  = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codepath)
       
       elif 'send email robin' in query:
           try:
               speak("What should i say?")    
               content=takeCommand()
               to = "u1704045@student.cuet.ac.bd"  
               sendEmail(to,content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("Sorry Sir,I am not able to send your email")
        
       elif 'how are you' in query or "and you" in query or 'how is it going' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
        
       elif 'hi' in query or "hello" in query: 
            speak("Hello Sir. How are you?")
        
       elif 'thank you' in query or "thanks" in query: 
            speak("Thank You so much sir.") 
    
  
       elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
    
       elif 'who create you' in query or 'who created you' in query or "who made you" in query or "who has created you" in query: 
            speak("Mr. Rezowanur Rahman Robin Has Created me.") 
        
       elif 'about your creator' in query: 
            speak("Mr. Rezowanur Rahman Robin Has Created me. Mr. Rezowanur Rahman Robin is a student of Computer Science And Engineeing at Chittagong University Of Engineering And Technology.") 

            
       elif 'about my sister' in query: 
            speak("You have only one little sister whose name is Amina Akhter Rakhi. You called her Rakhi.She is in class six now. She is not good at study. Every time she is trying to distrub you. You should punish her.") 

       elif 'about my mother' in query: 
            speak("Your mother name is Salina Akhter Ruba. She is a housewife. ") 
        
       elif 'about my father' in query: 
            speak("Your father name is Mr. Aminur Rahman . He is in Bangladesh Navy. He is an angry man. Be careful of him. ") 

 
       elif "where is" in query:
        listening = True
        query = query.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(query[2])
        speak("Hold on Dante, I will show you where " + query[2] + " is.")
        maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
        os.system(maps_arg)

   
