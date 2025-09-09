import pyttsx3
import os
import webbrowser
import speech_recognition as sr
import time

# from transformers import pipeline
import pywhatkit as kit

# Initialize TTS engine
engine = pyttsx3.init('sapi5')


# modle ke voice ki speed 
rate = engine.getProperty('rate')
print(f"Default rate :- {rate}")
engine.setProperty('rate' , 195)

# for volume 
volume = engine.getProperty('volume')
print(f"original volume :- {volume}")
engine.setProperty('volume' , 1)

# for male/female
voices = engine.getProperty('voices')
for i, v in enumerate(voices):
    print(f"{i} -> {v.id}")
    engine.setProperty('voice' , voices[1].id)     # mostly 0=male, 1=female


engine.startLoop(False)


# yaha modle ko ready kiya hai bolne ke liye
def speak(text):
    
    engine.say(text)
    engine.iterate()  
    

    
recognizer = sr.Recognizer()



def chatbot_response(query):
    query = query.lower()

    if "who are you" in query:
        return "I am your personal AI voice assistant!"
    
    elif "joke" in query:
        return "Why don’t scientists trust atoms? Because they make up everything!"
    
    elif "your name" in query:
        return "My name is Jarvis, your AI helper."
    
    else:
        return "Sorry, I don’t know that yet. But I'm learning!"



def process_command(command):
    command = command.lower()

    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
        print(" Opening YouTube...")

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
        print(" Opening Google...")

    elif "facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
        print(" Opening Facebook...")

    elif "notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")
        print("Opening Notepad...")
        
    elif "open" in command:
        site = command.replace("open" , "").strip()
        if "." not in site:
            site = site + '.com'
        url = f"https://www." + site
        webbrowser.open(url)
        speak(f"opening {site}")
        
    elif "search" in command:
        query = command.replace("search" , "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")      
        speak(f"Searching on google about {query}")

    elif "movie" in command:
        movie_path = r"C:\Users\sunny\Downloads\Prmovies-Rab_Ne_Bana_Di_Jodi.mp4"     # apna path daalo
        os.startfile(movie_path)
        speak("Playing movie")
        print("🎵 Playing movie...")
        
    elif "play" in command:
        song = command.replace("play" , "").strip()
        print(f"playing {song} on youtube...")
        speak(f"playing {song} on youtube...")
        kit.playonyt(song)
        
    elif "who are you" in command or "your name" in command or "joke" in command:
        response = chatbot_response(command)
        print("🤖:", response)
        speak(response)

        
    elif "exit" in command or "stop" in command or "bye" in command:
        speak("okay sir, Goodbye , Meet you soon")
        engine.iterate()   # 🟢 wait until "Goodbye" finishes
        time.sleep(3)
        engine.endLoop()
        return False

    else:
        print("❓ Sorry, I don't understand that command.")
        speak("Sorry, I don't understand that command.")
        
    return True
    
    
    
# process_command("google")
# speak("2354544852")
   

    
speak("Voice assistant started. Say something...")
while True:
     with sr.Microphone() as source:
        print("listening...")
        audio = recognizer.listen(source)
        
        try:
           command = recognizer.recognize_google(audio)
           print("you said :- " , command)
           
           
           if not process_command(command):
                break  
           
        except sr.UnknownValueError:
            print("Firse bol samhj nhi ayaa...")
        except sr.RequestError:
            print("chech your internet connection...")
    
            

       