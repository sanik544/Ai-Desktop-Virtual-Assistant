import datetime
import text_to_speech
import speech_to_text
import webbrowser
import weather
import os
from weather import Weather



def Action(data):   
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is Virtual Assistant")  
        return "my name is Virtual Assistant"

    elif "hello" in user_data or "hye" in user_data or "hay" in user_data: 
        text_to_speech.text_to_speech("Hey sir, how can I help you!")  
        return "Hey sir, how can I help you!" 

    elif "how are you" in user_data:
        text_to_speech.text_to_speech("I am doing great these days sir") 
        return "I am doing great these days sir"   

    elif "thanku" in user_data or "thank" in user_data:
        text_to_speech.text_to_speech("It's my pleasure sir to stay with you")
        return "It's my pleasure sir to stay with you"      

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning sir, I think you might need some help")
        return "Good morning sir, I think you might need some help"   

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        text_to_speech.text_to_speech(Time)
        return Time 

    elif "shutdown" in user_data or "quit" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"  

    elif "play music" in user_data or "song" in user_data:
        webbrowser.open("https://gaana.com/")   
        text_to_speech.text_to_speech("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"

    elif 'open google' in user_data:
        webbrowser.open('https://google.com/')
        text_to_speech.text_to_speech("Google opened")  
        return "Google opened"

    elif 'open youtube' in user_data:
        webbrowser.open('https://youtube.com/')
        text_to_speech.text_to_speech("YouTube opened") 
        return "YouTube opened"    
    
    
    elif 'weather' in user_data:
        ans = weather.get_weather()
        text_to_speech.text_to_speech(ans)
        return ans
 

    
   
    
    elif 'open whatsapp' in user_data:
        webbrowser.open('https://web.whatsapp.com/')
        text_to_speech.text_to_speech("WhatsApp opened") 
        return "WhatsApp opened" 
    
    elif 'open instagram' in user_data:
        webbrowser.open('https://www.instagram.com/')
        text_to_speech.text_to_speech("Instagram opened") 
        return "Instagram opened" 
    
    elif 'open mail' in user_data:
        webbrowser.open('https://mail.google.com/')
        text_to_speech.text_to_speech("Mail opened") 
        return "Mail opened"
    
    elif 'open linkedin' in user_data:
        webbrowser.open('https://www.linkedin.com/login')
        text_to_speech.text_to_speech("linkdin opened") 
        return "linkedin opened"
    
    
    
    


    elif "play game" in user_data or "pong" in user_data:
        os.system("python game.py")
        text_to_speech.text_to_speech("Starting Pong game") 
        return "Starting Pong game..."
 
    
    
    
    
    else:
        text_to_speech.text_to_speech("I'm unable to understand!")
        return "I'm unable to understand!"