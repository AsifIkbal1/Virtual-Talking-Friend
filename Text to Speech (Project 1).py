import pyttsx3
variable=pyttsx3.init()
a=input("Write your text in here :  ")
variable.say(a)
variable.runAndWait()