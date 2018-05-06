# All the imports in this section
#----------------------------------------------------------------------------------------------------------------------#
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import os, sys, subprocess
from subprocess import call
import cv2, csv
import video_emotion_color_demo_rahul as veg
import numpy
import speech_recognition as sr
import videoplayer2 as vdo
from pygame import mixer
import table1 as tab


#import keras_and_nn_uncommented as andopr
#import video_trial #as vt
#----------------------------------------------------------------------------------------------------------------------#

# INITIALIZATIONS :

    
actorslist = ['amitabhbachchan', 'salmankhan', 'shahrukhkhan', 'aamirkhan']
objectslist = ['table','hat','tie','chair']
emotionslist= ['happy','sad','surprise','fear','contempt','angry','disgust']

actors = ['Amitabh', 'Salman', 'Shahrukh', 'Aamir',]
objects = ['Table','Hat','Tie','Chair']
emotions= ['Happy','Sad','Surprise','Fear','Contempt','Anger','Disgust']

var=[0]*4
emo=[0]*7
var1=[0]*4

v1=[0]*4
v2=[0]*7
v3=[0]*4

actor = []
objec = []
emotion = []
frame_no = []

def init():
    actor.clear()
    objec.clear()
    emotion.clear()
    frame_no.clear()
    


#----------------------------------------------------------------------------------------------------------------------#
# Initialize an instance

win = tk.Tk()

# Window Title

win.title("Face Recognition and Emotion Analysis")
#img = PhotoImage(file='C:\\Users\\ASUS\\Desktop\\Face Recognition\\trial1\\Face Detection and Emotion Analysis\\src\\faceicon.gif')
#win.tk.call('wm', 'iconphoto', win._w, img)

#style = ttk.Style()
#style.theme_use('vista')

win.resizable(0,0)
win.minsize(300,300)
win.geometry("500x500")

#photo = PhotoImage(file='C:\\Users\\ASUS\\Desktop\\Face Recognition\\trial1\\Face Detection and Emotion Analysis\\src\\microphone.png').subsample(8,8)
label1 = ttk.Label(win, text='Query:')
label1.place(x=10,y=10)
#label1.grid(row=0, column=0)
entry1 = ttk.Entry(win, width=40)
entry1.place(x=50,y=10)

#voice_button = Button(win, image=photo, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
#MyButton6.grid(row=0, column=5)


#entry1.grid(row=0, column=1, columnspan=4)

#Button Click Event Function
def clickMe():
    win.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Videos","*.mp4"),("all files","*.*")))
    print (win.filename)
    veg.func(win.filename)
    #os.system('python video_emotion_gender_demo.py '+win.filename)
    #subprocess.call(['python', 'video_emotion_gender_demo.py', win.filename])

def opencsv():
    win.csvname =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv","*.csv"),("all files","*.*")))
    #print (win.csvname)
    
    
def exit():
    win.destroy()

menu = Menu(win)
win.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
#subMenu.add_command(label="New Project", command=donothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)

editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
#editmenu.add_command(label="Redo", command=donothing)    


# Adding a Button
action = Button (win, text="Search for a file", command=clickMe)
action.place(x=50,y=50)
action.config(width=18,height=5)

action = Button (win, text="Metadata", command=opencsv)
action.place(x=250,y=50)
action.config(width=18,height=5)


def mget():
    init()
    print('Processing')
    for i in range (0,4):
        v1[i]=var[i].get()
    for i in range (0,7):
        v2[i]=emo[i].get()
    for i in range (0,4):
        v3[i]=var1[i].get()
    mget2()

def mget2():
    init()
    print(actors)
    print(v1)
    print("\n")
 
    print(emotions)
    print(v2)
    print("\n")
    
    print(objects)
    print(v3)
    print("\n")

    aa=[[],[],[],[],[]]
    a_set=[[],[],[],[],[]]
    bb=[[],[],[],[],[],[],[],[],[]]
    b_set=[[],[],[],[],[],[],[],[],[]]
    cc=[[],[],[],[],[]]
    c_set=[[],[],[],[],[]]
  
    
# Creates the actor list as per the users choice
    for i in range (0,4):
        if(v1[i]==1):
            actor.append(actorslist[i])

    for i in range (0,7):
        if(v2[i]==1):
            emotion.append(emotionslist[i])

    for i in range (0,4):
        if(v3[i]==1):
            objec.append(objectslist[i])
            

#Store frame numbers of the entered Actors, Emotions and Objects.
            
    with open(win.csvname, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            for element in row[4].split(" "):
                #print('Entering for loop')
                for p in range(len(actor)):
                    if row[4] == actor[p]:
                        aa[p].append(row[1])
                        #print(p,aa[p],actor[p])

    with open(win.csvname, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            for element in row[2].split(","):
                #print('Entering for loop')
                for p in range(len(emotion)):
                    if row[2] == emotion[p]:
                        bb[p].append(row[1])
                        #print(p,aa[p],actor[p])

    with open(win.csvname, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            for element in row[7].split(","):
                #print('Entering for loop')
                for p in range(len(objec)):
                    if row[7] == objec[p]:
                        cc[p].append(row[1])
                        #print(p,aa[p],actor[p])    

#Convert the frames into a set of frames and find out their intersection.

    for i in range (len(actor)):
        a_set[i] = set(aa[i])

    for i in range (len(emotion)):
        b_set[i] = set(bb[i])

    for i in range (len(objec)):
        c_set[i] = set(cc[i])

    frame_no=a_set[0]
    for i in range (len(actor)):
        #print(a_set[i])
        frame_no= frame_no.intersection(a_set[i])

    for i in range (len(emotion)):
        #print(b_set[i])
        frame_no= frame_no.intersection(b_set[i])
    
    for i in range (len(objec)):
        #print(c_set[i])
        frame_no= frame_no.intersection(c_set[i])

    frame_no=list(frame_no)
    print(frame_no)
##    import tkinter as tk
##    from tkinter import ttk

    class Begueradj(tk.Frame):
        '''
        classdocs
        '''  
        def __init__(self, parent):
            '''
            Constructor
            '''
            tk.Frame.__init__(self, parent)
            self.parent=parent
            self.initialize_user_interface()

        def initialize_user_interface(self):
            """Draw a user interface allowing the user to type
            items and insert them into the treeview
            """
            self.parent.title("Matching Frames")       
            self.parent.grid_rowconfigure(0,weight=1)
            self.parent.grid_columnconfigure(0,weight=1)
            self.parent.config(background="lavender")

            # Set the treeview
            self.tree = ttk.Treeview( self.parent, columns=('Serial number', 'Frame number'))
            self.tree.heading('#1', text='Serial number')
            self.tree.heading('#2', text='Frame number')
            self.tree.column('#1', stretch=tk.YES)
            self.tree.column('#2', stretch=tk.YES)
            self.tree.grid(row=4, columnspan=4, sticky='nsew')
            self.insert_data(frame_no)
            self.tree.bind('<ButtonRelease-1>', self.select_item)
            self.treeview = self.tree
            # Initialize the counter
            self.i = 0


        def insert_data(self,frame_no):
           for p in range(len(frame_no)):
             self.tree.insert('', 'end', values=(p,frame_no[p]))

        def select_item(self, a):   # added self and a (event)
            test_str_library = self.tree.item(self.tree.selection())# gets all the values of the selected row
            #print ('The test_str = ', type(test_str_library), test_str_library,  '\n')  # prints a dictionay of the selected row
            item = self.tree.selection()[0] # which row did you click on
            #print ('item clicked ', item) # variable that represents the row you clicked on
            fra=self.tree.item(item)['values'][1]
            print (self.tree.item(item)['values'][1]) # prints the first value of the values (the id value)
            cap = cv2.VideoCapture('joined-all.mp4')
            vdo.vpl(fra)

    def main():
        root=tk.Tk()
        d=Begueradj(root)
        root.mainloop()

    if __name__=="__main__":
        main()
    
    #vdo.vpl(tab.table.main.d.self.tree.item(item)['values'][1])
    
#------------------------------------------------------------------------------------------------------------------#
    
##    cap = cv2.VideoCapture('joined-all.mp4')
##    for p in range(len(frame_no)):
##        vdo.vpl(fra)
##        print("Video number "+ str(p+1) +" has ended.")
##
        
##        print(" Entering the for loop")
##        cap.set(1, float(frame_no[p]))
##        
##        print(" The frame with the required actor and the object is : " + frame_no[p])
##        ret, frame = cap.read()
##        cv2.imshow('window_name', frame)
##        while True:
##            ch = 0xFF & cv2.waitKey(1)
##            if ch == 27:
##                break 

def buttonQuery():
    init()
    words = entry1.get().split()
    print(words)
    for i in range(len(actors)):
        for j in range (len(words)):
            if words[j]==actors[i]:
                v1[i]=1

    for i in range(len(emotionslist)):
        for j in range (len(words)):
            if words[j]==emotionslist[i]:
                v2[i]=1
                            
    for i in range(len(objectslist)):
        for j in range (len(words)):
            if words[j]==objectslist[i]:
                v3[i]=1

    for i in range(len(actors)):
        print (v1[i])
    for i in range(len(emotionslist)):
        print (v2[i])
    for i in range(len(objectslist)):
        print (v3[i])
    mget2()

def buttonClick():
    #mixer.init()
    #mixer.music.load('chime1.wav')
    #mixer.music.play()
    init()
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
            mget2()
                    
        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')

        else:
            pass

#---------------------------------------------------------------------------------------------------#
# Actors

actors_label = tk.Label(win, text="Actors", font = "8")
actors_label.pack()
actors_label.place(x=35,y=160)
#actors_label.config(width=7,height=1)

var[0] = IntVar()
act_check1 = ttk.Checkbutton(win, text = 'Amitabh Bacchan', state = ACTIVE, variable = var[0])
act_check1.pack()
act_check1.place(x=40,y=200)

var[1] = IntVar()
act_check2 = ttk.Checkbutton(win, text = 'Salman Khan', state = ACTIVE, variable = var[1])
act_check2.pack()
act_check2.place(x=40,y=220)

var[2] = IntVar()
act_check3 = ttk.Checkbutton(win, text = 'Shah Rukh Khan', state = ACTIVE, variable = var[2])
act_check3.pack()
act_check3.place(x=40,y=240)

var[3] = IntVar()
act_check4 = ttk.Checkbutton(win, text = 'Aamir Khan', state = ACTIVE, variable = var[3])
act_check4.pack()
act_check4.place(x=40,y=260)

#---------------------------------------------------------------------------------------------------#
# Emotions


emotion_label = tk.Label(win, text="Emotions", font = "8")
emotion_label.pack()
emotion_label.place(x=190,y=160)

emo[0] = IntVar()
emo_check1 = ttk.Checkbutton(win, text = 'Happy', state = ACTIVE, variable = emo[0])
emo_check1.pack()
emo_check1.place(x=200,y=200)

emo[1] = IntVar()
emo_check2 = ttk.Checkbutton(win, text = 'Sad', state = ACTIVE, variable = emo[1])
emo_check2.pack()
emo_check2.place(x=200,y=220)

emo[2] = IntVar()
emo_check3 = ttk.Checkbutton(win, text = 'Surprise', state = ACTIVE, variable = emo[2])
emo_check3.pack()
emo_check3.place(x=200,y=240)

emo[3] = IntVar()
emo_check4 = ttk.Checkbutton(win, text = 'Fear', state = ACTIVE, variable = emo[3])
emo_check4.pack()
emo_check4.place(x=200,y=260)

emo[4] = IntVar()
emo_check5 = ttk.Checkbutton(win, text = 'Contempt', state = ACTIVE, variable = emo[4])
emo_check5.pack()
emo_check5.place(x=200,y=280)

emo[5] = IntVar()
emo_check6 = ttk.Checkbutton(win, text = 'Anger', state = ACTIVE, variable = emo[5])
emo_check6.pack()
emo_check6.place(x=200,y=300)

emo[6] = IntVar()
emo_check7 = ttk.Checkbutton(win, text = 'Disgust', state = ACTIVE, variable = emo[6])
emo_check7.pack()
emo_check7.place(x=200,y=320)


#---------------------------------------------------------------------------------------------------#
#Objects



objects_label = tk.Label(win, text="Objects", font = "8")
objects_label.pack()
objects_label.place(x=340,y=160)
#objects_label.config(width=7,height=1)


var1[0] = IntVar()
obj_check1 = ttk.Checkbutton(win, text = 'Table', state = ACTIVE, variable = var1[0])
obj_check1.pack()
obj_check1.place(x=350,y=200)

var1[1] = IntVar()
obj_check2 = ttk.Checkbutton(win, text = 'Hat', state = ACTIVE, variable = var1[1])
obj_check2.pack()
obj_check2.place(x=350,y=220)


var1[2] = IntVar()
obj_check3 = ttk.Checkbutton(win, text = 'Tie', state = ACTIVE, variable = var1[2])
obj_check3.pack()
obj_check3.place(x=350,y=240)

var1[3] = IntVar()
obj_check4 = ttk.Checkbutton(win, text = 'Chair', state = ACTIVE, variable = var1[3])
obj_check4.pack()
obj_check4.place(x=350,y=260)

#---------------------------------------------------------------------------------------------------#

voice_button = Button(win, text = "Voice Input", command = buttonClick)
voice_button.place(x=390,y=10)

voice_button = Button(win, text = "Search", command = buttonQuery)
voice_button.place(x=320,y=10)

action = Button (win, text="Process", command=mget)
action.place(x=200,y=365)
action.config(width=10,height=2)

action = Button (win, text="EXIT", command=exit)
action.place(x=200,y=420)
action.config(width=10,height=2)

#-----------------------------------------------------------------------------------------------------#

win.mainloop()

