import sounddevice as sd
import wavio as wv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from playsound import playsound

window = Tk()
window.title("Recording App")
window.geometry("400x300")
file_name=""
duration_var=StringVar()

def OpenFile():
    global file_name
    file_name = filedialog.askopenfilename()
    messagebox.showinfo("Message", f"{file_name} has been selected")

def TakeRec():
    global file_name
    isValid = False
    file_name = filedialog.asksaveasfilename(defaultextension='.wav',filetypes=[("WAV File",".wav")])
    if not file_name:
        return 0
        
    
    # Sampling frequency
    freq = 44100
    while not (isValid):
        try:
            duration = simpledialog.askfloat("Duration","Enter duration in seconds")
            isValid = True
        except ValueError:
            messagebox.showinfo("Invalid Data Inputted")
        except TypeError:
            messagebox.showinfo("Invalid Data Inputted")

    # Start recorder with the given values of duration and sample frequency
    recording = sd.rec(int(duration * freq), 
                    samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # file with the given sampling frequency
    wv.write(f"{file_name}",recording,freq,sampwidth=2,scale=0.9)
    messagebox.showinfo("Message","Recording Finished")

def PlayRec():
    global file_name
    if not file_name:
        messagebox.showinfo("Message","File not selected")
        return 0
    playsound(file_name)
    file_name = ""
    messagebox.showinfo("Message","Done Playing")
    

Record=Button(window,text="Record",command=TakeRec)
Record.grid(row=1,column=1)

Play=Button(window,text="Play",command=PlayRec)
Play.grid(row=1,column=2)

Open=Button(window,text="Open",command=OpenFile)
Open.grid(row=1,column=3)

window.mainloop()