import datetime                                                            # Importing datetime library to check current date and time.
import pywhatkit                                                           # Importing pywhatkit library to send messages on whatsapp.
import urllib.request                                                      # Importing url library to open thingspeak url and to fedge data.
import pyttsx3                                                             # Importing pyttsx3 library to make our assistant to speak.
import re                                                                  # Importing regex library to cut some lines from the data and to convert it into usefull information.
import time                                                                # Importing time library to give delay time when needed.
import os                                                                  # Importing os library to shut down google crome when it is not in use.

engine = pyttsx3.init('sapi5')                                             # Setting up voice type, speech rate and other necessary things related to speech.
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)
engine.setProperty('voice',voices[0].id)

browserExe = "chrome.exe" 

def speak(audio):                                                          # Defining a speak function to make our work easy in upcoming lines of code.
    engine.say(audio)
    engine.runAndWait()

speak("Hello sir my name is fire detecting assistant. Sir my task is to detect fire in the house. Sir if in case there will be fire then I will alert you by speaking and I will also send you what's app message. Sir you can trust on me.") # Introduction line to be spoken.

if __name__=="__main__":

    while True:
        
        time.sleep(30)
        data = urllib.request.urlopen("https://api.thingspeak.com/channels/1352966/feeds.json?api_key=AHVZEZVDEN0J433Q&results=1")   # Requesting for url to get open. 
        data =repr(data.read())                                                                                                      # Making the data coming from the url to read.
                                                                                                        
        
        find1 = data.find("field1", 200)                                     # Finding the field1 or sensor1 value from the raw data.
        find1 = find1 + 9  
        
        find2 = data.find("field2", 200)                                     # Finding the field2 or sensor2 value from the raw data.
        find2 = find2 + 9

        find3 = data.find("field3", 200)                                     # Finding the field2 or sensor2 value from the raw data.
        find3 = find3 + 9

        find4 = data.find("field4", 200)                                     # Finding the field2 or sensor2 value from the raw data.
        find4 = find4 + 9

        flame1 = data[find1:]                                                # Making the field1 value or sensor1 value to be readable.
        flamesensor1 = flame1[:1]

        flame2 = data[find2:]                                                # Making the field2 value or sensor2 value to be readable.
        flamesensor2 = flame2[:1]

        flame3 = data[find3:]                                                # Making the field3 value or sensor3 value to be readable.
        flamesensor3 = flame3[:1]

        flame4 = data[find4:]                                                # Making the field4 value or sensor4 value to be readable. 
        flamesensor4 = flame4[:1]

        now = datetime.datetime.now()                                        # Reading date and time. 
        print("Today's Date and Time:" + now.strftime("%y-%m-%d %H:%M:%S"))  # Printing today's date and time.
        hour = now.strftime("%H")                                            # Fetching hours value from date and time.
        minutes = now.strftime("%M")                                         # Fetching minutes value.
        min2 = int(minutes) + 2                                              # Adding 2 in minutes value.
        time.sleep(2)                    

            

        print("Flame sensor 1 value :" + flamesensor1)                       # Printing sensor value 1. 
        print("Flame sensor 2 value :" + flamesensor2)                       # Printing sensor value 2.
        print("Flame sensor 3 value :" + flamesensor3)                       # Printing sensor value 3.
        print("Flame sensor 4 value :" + flamesensor4)                       # Printing sensor value 4.

        

        if int(flamesensor1) == 0 and int(flamesensor2) == 1 and int(flamesensor3) == 1 and int(flamesensor4) == 1:         # Checking sensor's value if sensor 1 value is 0 then it will execute the following lines.    
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room one. I am sending you details on your whatsapp number")                                                                       # It will first speak this line.
            time.sleep(1)
            print("Hello my I am your fire detecting assistant speaking. I have detected fire at your home. Fire is right now in room 1 only. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")  # Then it will print this statement
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my I am your fire detecting assistant speaking. I have detected fire at your home. Fire is right now in room 1 only. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on. ", int(hour) , int(min2)) # Now our assistant will send the given message to the specified number.
            time.sleep(5)
            browserExe = "chrome.exe"                         
            os.system("taskkill /f /im "+browserExe)                                                                         # Once the message will be send then it will automatically close the google crome.
            
            
        elif int(flamesensor1) == 1 and int(flamesensor2) == 0 and int(flamesensor3) == 1 and int(flamesensor4) == 1:        # Checking sensor's value if sensor 2 value is 0 then it will execute the following lines.
            speak("Danger. danger.Sir its your fire detecting assistant speaking. Sir i have detected fire in room two. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 2 only. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 2 only. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on. ", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 


        elif int(flamesensor1) == 1 and int(flamesensor2) == 1 and int(flamesensor3) == 0 and int(flamesensor4) == 1:         # Checking sensor's value if sensor 3 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room three. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 3 only. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 3 only. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        
        elif int(flamesensor1) == 1 and int(flamesensor2) == 1 and int(flamesensor3) == 1 and int(flamesensor4) == 0:         # Checking sensor's value if sensor 4 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room four. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 4 only. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 4 only. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 0 and int(flamesensor2) == 0 and int(flamesensor3) == 1 and int(flamesensor4) == 1:          # Checking sensor's value if sensor 1 and sensor 2 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room one and room two. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1 and room 2. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1 and room 2. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 0 and int(flamesensor2) == 1 and int(flamesensor3) == 0 and int(flamesensor4) == 1:         # Checking sensor's value if sensor 1 and sensor 3 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room one and room three. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1 and room 3. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1 and room 3. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 0 and int(flamesensor2) == 1 and int(flamesensor3) == 1 and int(flamesensor4) == 0:          # Checking sensor's value if sensor 1 and sensor 4 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room one and room four. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 1 and int(flamesensor2) == 0 and int(flamesensor3) == 0 and int(flamesensor4) == 1:          # Checking sensor's value if sensor 2 and sensor 3 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room two and room three. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 2 and room 3. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 2 and room 3. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 1 and int(flamesensor2) == 0 and int(flamesensor3) == 1 and int(flamesensor4) == 0:          # Checking sensor's value if sensor 2 and sensor 4 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room two and room four. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 2 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 2 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 1 and int(flamesensor2) == 1 and int(flamesensor3) == 0 and int(flamesensor4) == 0:         # Checking sensor's value if sensor 3 and sensor 4 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room three and room four. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 3 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 3 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 0 and int(flamesensor2) == 0 and int(flamesensor3) == 0 and int(flamesensor4) == 1:        # Checking sensor's value if sensor 1, sensor 2 and sensor 3 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room one, room two and room three. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1, room 2 and room 3. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1, room 2 and room 3. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 0 and int(flamesensor2) == 1 and int(flamesensor3) == 0 and int(flamesensor4) == 0:        # Checking sensor's value if sensor 1, sensor 3 and sensor 4 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room one, room three and room four. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1, room 3 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1, room 3 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 1 and int(flamesensor2) == 0 and int(flamesensor3) == 0 and int(flamesensor4) == 0:         # Checking sensor's value if sensor 2, sensor 3 and sensor 4 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room two, room three and room four. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 2, room 3 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 2, room 3 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 0 and int(flamesensor2) == 0 and int(flamesensor3) == 1 and int(flamesensor4) == 0:         # Checking sensor's value if sensor 1, sensor 2 and sensor 4 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in room one, room two and room four. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1, room 2 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is right now in room 1, room 2 and room 4. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe) 

        elif int(flamesensor1) == 0 and int(flamesensor2) == 0 and int(flamesensor3) == 0 and int(flamesensor4) == 0:        # Checking sensor's value if sensor 1, sensor 2, sensor 3 and sensor 4 value is 0 then it will execute the following lines.
            speak("Danger. danger. Sir its your fire detecting assistant speaking. Sir i have detected fire in all the rooms. I am sending you details on your whatsapp number")
            time.sleep(1)
            print("Hello my name is Automation. I have detected fire at your home. Fire is in all the rooms. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.")
            time.sleep(1)
            pywhatkit.sendwhatmsg("Your whatsapp number","Hello my name is Automation. I have detected fire at your home. Fire is in all the rooms. Please call Fire Fighters. Number of fire fighters is :- 101 and please also call your neighbours so that they can have a look what is going on.", int(hour) , int(min2))
            time.sleep(5)
            browserExe = "chrome.exe" 
            os.system("taskkill /f /im "+browserExe)    



