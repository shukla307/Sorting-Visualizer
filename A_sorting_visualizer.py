from tkinter import*
from tkinter import ttk
import random
from bubblesort import bubble_sort
from selectionsort import selection_sort
from insertionsort import insertion_sort
from mergesort import merge_sort
from quicksort import quick_sort
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    speak("I am natasha Sir. welcome to the sorting visualizer made by himanshi and shitiza")
    

wishMe()    

root=Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry('900x600+200+80')
root.config(bg="yellow")

speak("Select a sorting algorithm from the dropdown menu.")
speak("Customize data size, minimum, and maximum values.")
speak("Adjust sorting speed as needed.")
speak("Click  on Generate to create a dataset.")
speak("Click on  Start to visualize the selected sorting algorithm.")


def drawData(data,colorArray):
    
    canvas.delete("all")
    canvas_height=450
    canvas_width=870
    x_width=canvas_width/(len(data)+1)
    offset=10
    spacing_bet_rect=10
    normalised_data=[i/max(data) for i in data]

    for i,height in enumerate(normalised_data):
        x0=i*x_width+offset+spacing_bet_rect
        y0=canvas_height-height*400
        x1=(i+1)*x_width
        y1=canvas_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),font=("new roman",15,"italic bold"),fill="orange")

    root.update_idletasks()

        
def StartAlgorithm():
    

    global data
    if not data:
        speak("no data found")
        return
    if(algo_menu.get()=='Quick Sort'):
        speak("quick sort exicuting")
        quick_sort(data,0,len(data)-1,drawData,speedscale.get())
        drawData(data,['grey' for x in range(len(data))])
    elif algo_menu.get()=='Bubble Sort':
        speak("bubble sort exicuting")
        bubble_sort(data,drawData,speedscale.get())
    elif algo_menu.get()=='Selection Sort':
        speak("selection  sort exicuting")
        selection_sort(data,drawData,speedscale.get())
    elif algo_menu.get()=='Insertion Sort':
        speak("Insertion sort exicuting")
        insertion_sort(data,drawData,speedscale.get())
    elif algo_menu.get()=='Merge Sort':
        speak("merge sort exicuting")
        merge_sort(data,drawData,speedscale.get())
    drawData(data,['pink' for x in range(len(data))])
    



def Generate():
    global data
    print('Selected Algorithm: ',selected_algorithm.get())
    minivalue=int(minvalue.get())
    maxivalue=int(maxvalue.get())
    sizeevalue=int(sizevalue.get())


    data=[]
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue,maxivalue+1))
    drawData(data,['green' for x in range(len(data))])
    
selected_algorithm=StringVar()
#label,...buttons

mainlabel=Label(root,text="Algorithm: ",font=('new roman',16,'italic bold'),bg="pink",width=10,fg='black',relief=GROOVE,bd=5)

mainlabel.place(x=0,y=0)

algo_menu=ttk.Combobox(root,width=15,font=("new roman",19,"italic bold"),textvariable=selected_algorithm,
values=['Bubble Sort','Selection Sort','Insertion Sort','Merge Sort','Quick Sort'])
algo_menu.place(x=145,y=0)
algo_menu.current(0)

random_generate=Button(root,text="Generate",bg="pink",fg="black",font=("arial",12,"italic bold"),relief=SUNKEN, activebackground="white",activeforeground="black",bd=5,width=10, command=Generate)
random_generate.place(x=750,y=60)

sizevaluelabel=Label(root,text="Size:",font=("new roman",12,"italic bold"),bg="pink",width=10,fg="black",height=2,relief=GROOVE,bd=5)
sizevaluelabel.place(x=0,y=60)

sizevalue=Scale(root,from_=0, to=30,resolution=1,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
sizevalue.place(x=120,y=60)


minvaluelabel=Label(root,text="Min Value:",font=("new roman",12,"italic bold"),bg="pink",width=10,fg="black",height=2,relief=GROOVE,bd=5)
minvaluelabel.place(x=250,y=60)

minvalue=Scale(root,from_=0, to=10,resolution=1,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
minvalue.place(x=370,y=60)


maxvaluelabel=Label(root,text="Max Value:",font=("new roman",12,"italic bold"),bg="pink",width=10,fg="black",height=2,relief=GROOVE,bd=5)
maxvaluelabel.place(x=500,y=60)

maxvalue=Scale(root,from_=0, to=100,resolution=1,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
maxvalue.place(x=620,y=60)

start=Button(root,text="Start",bg="pink",fg="black",font=("arial",12,"italic bold"),relief=SUNKEN, activebackground="white",activeforeground="black",bd=5,width=10,command=StartAlgorithm)
start.place(x=750,y=0)

speedlabel=Label(root,text="Speed:",font=("new roman",12,"italic bold"),bg="pink",width=10,fg="black",relief=GROOVE,bd=5)
speedlabel.place(x=400,y=0)

speedscale=Scale(root,from_=0.1,to=5.0,resolution=0.2,length=200,digits=2,orient=HORIZONTAL,font=("arial",14,"italic bold"),bg="white",width=10,fg="black",relief=GROOVE,bd=5)
speedscale.place(x=520,y=0)

canvas=Canvas(root,width=870,height=450,bg="light green")
canvas.place(x=10,y=130)

root.mainloop()





