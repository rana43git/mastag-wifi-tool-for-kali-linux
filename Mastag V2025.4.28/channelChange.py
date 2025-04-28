from tkinter import *
import subprocess
import os

def Home():
	window.destroy() #close this tkinter GUI
	cmd = "python main.py"
	os.system(cmd)

def ChannelChange():
	cmd0 = "gnome-terminal --command='"'bash -c "'"sudo iwconfig wlan0 channel "
	cmd1 = str(e1.get()) #str() converting e3.get() to string cmd1
	cmd2 = ";sleep 1"'"'"'"
	cmd3 = cmd0+cmd1+cmd2
	os.system(cmd3)

def Clear(): # a function to clear the Entry Widget Content
	e1.delete(0, END)

window = Tk()

window.title('WiFi Channel Changer')
#window.geometry("350x90+10+20")

lbl1 = Label(window, text="Enter WiFi Channel")
lbl1.grid(row=0,column=0)

e1 = Entry(window)
e1.grid(row=0, column=1)

home = Button(window, text='Home', command=Home)
home.grid(row=0, column=2, ipadx=5 ,pady=4) #sticky=window.W,

quit = Button(window, text='Quit', command=window.quit) #window.quit close current window
quit.grid(row=1, column=2, ipadx=11, pady=4) #sticky=window.W,

run = Button(window, text='Run', command=ChannelChange)
run.grid(row=1, column=1, ipadx=30, pady=4) #sticky=window.W,

Clear = Button(window,text="Clear", command=Clear) #button to clear the Entry Widget
Clear.grid(row=1, column=0, ipadx=8, pady=4) #sticky=window.W,

window.mainloop()
