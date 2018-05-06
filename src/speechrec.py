import speech_recognition as sr
from pygame import mixer

r = sr.Recognizer()
r.pause_threshold = 0.7
r.energy_threshold = 400


with sr.Microphone() as source:
    try:
        print('Start speaking')
        audio = r.listen(source, timeout=10)
        message = str(r.recognize_google(audio))
        #mixer.music.load('chime2.wav')
        #mixer.music.play()
        entry1.focus()
        entry1.delete(0, END)
        entry1.insert(0, message)
        words = message.split()
        print(words)
'''        
        for i in range(len(actors)):
            for j in range (len(words)):
                if words[j]==actors[i]:
                    v1[i]=1

        for i in range(len(emotions)):
            for j in range (len(words)):
                if words[j]==emotions[i]:
                    v2[i]=1
                        
        for i in range(len(objects)):
            for j in range (len(words)):
                if words[j]==objects[i]:
                    v3[i]=1

        for i in range(len(actors)):
            print (v1[i])
        for i in range(len(emotions)):
            print (v2[i])
        for i in range(len(objects)):
            print (v3[i])
        mget2
'''                
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')

    except sr.RequestError as e:
        print('Could not request results from Google Speech Recognition Service')

    else:
        pass
