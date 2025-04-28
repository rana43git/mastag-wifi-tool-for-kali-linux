from tkinter import *
import subprocess
import os

    #>ifconfig wlan0mon down
    #>macchanger -m <user defined> wlan0mon
    #>ifconfig wlan0mon up

def Home():
	window.destroy() #close this tkinter GUI
	cmd = "python main.py"
	os.system(cmd)

def Run():
	cmd0 = "gnome-terminal --command='"'bash -c "'"sudo ifconfig "+devicelist.get()+" down; sudo macchanger -m "
	cmd1 = str(e1.get()) #str() converting int chanNum to string cmd
	cmd2 = " "+devicelist.get()+";sudo ifconfig "+devicelist.get()+" up" #" wlan0mon; ifconfig wlan0mon up"
	cmd3 = "; sleep 5"'"'"'"
	cmd4 = cmd0+cmd1+cmd2+cmd3
	os.system(cmd4)

def Clear(): # a function to clear the Entry Widget Content
	e1.delete(0, END)

window = Tk()

window.title('Manual MAC Changer')

icon = PhotoImage(file='icon.png') # Use your PNG file here
window.iconphoto(True, icon)

#if you remove this or modify OptionMenue you may need to change cmd 2 string value
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
device.grid(row=0, column=1, pady=2)#, columnspan=3
##################################################

lbl1 = Label(window, text="Enter Manual MAC")
lbl1.grid(row=1,column=0)

e1 = Entry(window, width=20)
#e1.insert(0,"a1:a2:a3:a4:a5:a6")
e1.grid(row=1, column=1)

home = Button(window, text='Home', command=Home)
home.grid(row=1, column=2, ipadx=5 ,pady=4) #sticky=window.W,

quit = Button(window, text='Quit', command=window.quit) #window.quit close current window
quit.grid(row=2, column=2, ipadx=11, pady=4) #sticky=window.W,

run = Button(window, text='Run', command=Run)
run.grid(row=3, column=1, ipadx=30, pady=4) #sticky=window.W,

clear = Button(window,text="Clear", command=Clear) #button to clear the Entry Widget
clear.grid(row=3, column=2, ipadx=8, pady=4) #sticky=window.W,

window.mainloop()
