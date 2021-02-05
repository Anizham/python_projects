import pyttsx3
import speech_recognition as sr
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query 
def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        command = take_commands()
        if "exit" in command:
            Speak(" Angane aakatte rajave!")
            break
        if "Good morning" in command:
            Speak("Good Morning!")
        if "How are you?" in command:
            Speak("I'm Fine, Thank You.")
        if "Fairfarren!" in command:
            Speak("Fairfarren!")
