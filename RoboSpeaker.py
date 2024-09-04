import os
import pyttsx3
engine = pyttsx3.init()

if __name__ == "__main__": 
    print("Welcome to RoboSpeaker 1.1. Created by Khushi ")
    while True:
        x = input("Enter what you want to speak:")
        if x =="q":
            os.system("say'bye bye friend'")
            break
        command=f"engine.say{x}"
        engine.runAndWait()
        os.system(command)