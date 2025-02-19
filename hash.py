import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from pathlib import Path

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# Register Chrome browser path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if Path(chrome_path).exists():
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Hash. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300  # Adding energy threshold to better detect speech
        r.dynamic_energy_threshold = True  # Enable dynamic energy threshold
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def open_application(app_name):
    app_paths = {
        'chrome': [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ],
        'notepad': r"C:\Windows\system32\notepad.exe",
        'calculator': r"C:\Windows\System32\calc.exe",
        'paint': r"C:\Windows\System32\mspaint.exe",
        'cmd': r"C:\Windows\System32\cmd.exe",
        'vscode': r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        # Add more applications as needed
    }
    
    try:
        if app_name in app_paths:
            # Handle multiple possible paths (like Chrome)
            if isinstance(app_paths[app_name], list):
                for path in app_paths[app_name]:
                    if Path(path).exists():
                        os.startfile(path)
                        speak(f"Opening {app_name}")
                        return
                speak(f"Could not find {app_name} in any of the expected locations")
            else:
                # Handle single path applications
                if Path(app_paths[app_name]).exists():
                    os.startfile(app_paths[app_name])
                    speak(f"Opening {app_name}")
                else:
                    speak(f"Could not find {app_name} at the expected location")
        else:
            speak(f"Sorry, I don't have the path for {app_name}")
    except Exception as e:
        speak(f"Error opening {app_name}")
        print(e)

def search_chrome(query):
    try:
        # Remove the "search" keyword if present
        search_query = query.replace("search", "").strip()
        # Create the Google search URL
        search_url = f"https://www.google.com/search?q={search_query}"
        # Try to use Chrome, fall back to default browser if Chrome is not available
        try:
            webbrowser.get('chrome').open(search_url)
        except webbrowser.Error:
            webbrowser.open(search_url)
        speak(f"Searching for {search_query}")
    except Exception as e:
        print(f"Error during search: {e}")
        speak("Sorry, I encountered an error while searching")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for this query. Please be more specific.")
                print("Possible matches:", e.options[:5])  # Show first 5 options
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information about that on Wikipedia.")
            except Exception as e:
                speak("Sorry, there was an error while searching Wikipedia.")
                print(e)

        elif 'search' in query:
            search_chrome(query)

        elif 'open' in query:
            # Extract the application name after "open"
            app_name = query.replace("open", "").strip()
            
            # Handle special cases for websites
            if 'youtube' in app_name:
                try:
                    webbrowser.get('chrome').open("https://www.youtube.com")
                except webbrowser.Error:
                    webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube")
            elif 'google' in app_name:
                try:
                    webbrowser.get('chrome').open("https://www.google.com")
                except webbrowser.Error:
                    webbrowser.open("https://www.google.com")
                speak("Opening Google")
            elif 'stackoverflow' in app_name:
                try:
                    webbrowser.get('chrome').open("https://stackoverflow.com")
                except webbrowser.Error:
                    webbrowser.open("https://stackoverflow.com")
                speak("Opening Stack Overflow")
            else:
                open_application(app_name)

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'email to' in query:
            # Extract the recipient email
            to = query.split("to")[1].strip()
            try:
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")    

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            exit()
