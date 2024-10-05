import webbrowser as wb
import pyttsx3 as tts
import speech_recognition as sr
import random as r
import pywhatkit as wk

#sr funnction works here!
# r=sr.Recognizer()
# mic = sr.Microphone(device_index=1)
# with mic as source:
#     r.adjust_for_ambient_noise(source, duration=1)
#     print("Listening...")
#     r.pause_threshold=2
#     audio =r.listen(source, phrase_time_limit=5)
#     user_input= r.recognize_google(audio,language='eng-in').lower()
#     print("Your Command :",user_input)
 
 #tts function works here!   
engine = tts.init()
voice =engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

while True:
    #takes text as user_input!
    user_input= input("Enter command : ").lower()
    if(user_input == 'exit'):
        print("see you soon...")
        speak("Bye sir!, See you soon")
        break 

    def execute_browser():
        if ("open youtube" in user_input):
            wb.open("http://www.youtube.com")
            print("Executing...")
            speak("sir, Executing... your command")
        elif("open google" in user_input):
            wb.open("http://www.Google.com")
            print("Executing...")
            speak("opening google, sir")
        elif(user_input == 'hi'or 'hi jarvis' in user_input):
            print("Hi Sahil!")
            speak("Hi Sir, what would you like me to do.")
        elif("open spotify" in user_input):
            wb.open(f"http://www.spotify.com")
            print("opening spotify...")
            speak("you have good taste of music by the way sir")
        elif("open chat gpt" in user_input):
            wb.open("https://chat.openai.com/chat")
            print("getting Chat GPT...")
            speak("its very difficult to say, he's good but, not better as me sir ")
        elif("open edge" in user_input):
            wb.get('Microsoft Edge')
        elif("open mail"in user_input or "open gmail" in user_input or "show my mails" in user_input):
            wb.open("https://mail.google.com/")
            print("Getting your Mails")
            speak("sir, getting your mails")
        else:
            string = ["sorry sir, Command not recognized by the system","oops! , really very sorry sir ","I will work on this thing, sir",
                    "soon i will get it, sir"]
            say = r.choice(string)
            print(say)    
            speak(say)
            
    def search():
        if('on youtube' in user_input):
            print("Searching on Youtube")
            speak("Searching on Youtube, sir")
            searchh = user_input
            for i in searchh:
                if("search"in searchh and "on youtube" in searchh):
                    search= searchh.replace("search","").replace("on youtube","")
                    wb.open(f"https://www.youtube.com/results?search_query={search}")
                break
        elif('on google' in user_input):    
    
            print("Searching on google")
            speak("Searching on google, sir")
            searchh = user_input
            for i in searchh:
                search = searchh.replace("search","").replace("on google","")
                wb.open(f"https://www.google.com/search?q={search}")
                break

    def basic_chat():
        if('joke' in user_input):
            string = ["sir, it's harder for me to make you laugh!",
                    "My sense of humour is bad, so no jokes sir"
                    ]
            say = r.choice(string)
            print(say)    
            speak(say)
        elif("story" in user_input):
            print('Getting a story.')
            speak('you are already making a story on your life sir') 
        elif("are you" in user_input):
            print("JARVIS here!")
            speak("I am Jarvis, Ready to make your things done") 
    def core():
        if('system' in user_input):
            print('Verifying Identity')
            speak("please confirm your identity")
            password=input("Enter Access Code : ")
            if(password == 'karan'):
                print("Access Granted")
                speak("Access Granted")
                speak("Sir,Shuting down in 5, 4. 3, 2. 1")
                wk.shutdown(7)
            else:
                print("Access Denied")
                speak("access denied")    
    def execute_play():
        if('on youtube' in user_input):
            for i in user_input:
             ip1=user_input.replace('play','').replace('on youtube','')
             print("Playing...")
             speak(f"playing {ip1} on youtube sir!")
             wk.playonyt(ip1)
             break
                    
    if('open' in user_input or 'hi' in user_input):
        execute_browser()
    elif("search" in user_input):
        search()
    elif('tell' in user_input or 'say' in user_input or 'who' in user_input):
        basic_chat()
    elif('play' in user_input):
        execute_play()
    elif('shutdown' in user_input):
        core()
    else:
        string = ["sorry sir, Command not recognized by the system","oops! , really very sorry sir ","I will work on this thing, sir"]
        say = r.choice(string)
        print(say,"Main error")    
        speak(say)