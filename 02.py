import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import sys

# Initialize text-to-speech engine
def speak(text):
    print(f"Jarvis: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        # Fallback if pyttsx3 is not configured locally
        pass

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Could you repeat?")
            return "none"
        except sr.RequestError:
            speak("Network error.")
            return "none"
        except Exception as e:
            return "none"

def execute_task(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        # Standard action example
        webbrowser.open("https://wikipedia.org")
        
    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("google.com")
        
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")
        
    elif 'shutdown' in query:
        speak("Shutting down the system")
        # Works on Windows systems
        # os.system("shutdown /s /t 1")
        
    elif 'exit' in query or 'stop' in query:
        speak("Goodbye, Sir.")
        sys.exit()

# Main driver loop
if __name__ == "__main__":
    speak("Jarvis initialized. How can I help you today?")
    # In an actual local environment, you would use a loop:
    # while True:
    #     query = listen_command()
    #     if query != "none":
    #         execute_task(query)
