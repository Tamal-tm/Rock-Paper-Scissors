import smtplib
import speech_recognition as sr
from email.message import EmailMessage #To, from and Subject of the Message
import pyttsx3

listener=sr.Recognizer()
tts=pyttsx3.Engine()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()

def mic():
    with sr.Microphone() as source:
        print('Program is listening.')
        voice=listener.listen(source)
        data=listener.recognize_google(voice)
        print(data)
        return data.lower()

dict={"jojo":"tamalmallick23@gmail.com"} # Easy pronunciation name

def send_mail(receiver,subject,body):
    server=smtplib.SMTP("smtp.gmail.com",587) # port nnumber
    server.starttls()
    server.login("mrinalmallick40@gmail.com","eoik btmk euay gbrk") # Created an app password through security. Can delete this. 
    # server.sendmail("mrinalmallick40@gmail.com","tamalmallick23@gmail.com",data) 
    email =EmailMessage()
    email["From"]="mrinalmallick40@gmail.com"
    email["To"]=receiver
    email["Subject"]=subject
    email.set_content(body)
    server.send_message(email)

def main_code():
    talking_tom("To whom do you want to send this email?")
    name=mic()
    receiver=dict[name]
    talking_tom("Speak the subject of the email")
    subject=mic()
    talking_tom("Speak the message of the email")
    body=mic()
    send_mail(receiver,subject,body)
    print('Your email has been sent!') 

main_code()