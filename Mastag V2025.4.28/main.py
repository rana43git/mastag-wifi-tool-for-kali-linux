from tkinter import *
import subprocess
import os

window=Tk()

window.title('Mastag Home 3.0 @2025')

icon = PhotoImage(file='icon.png') # Use your PNG file here
window.iconphoto(True, icon)

option = os.listdir('/sys/class/net/') #Global Variable
devicelist = StringVar() #Global Variable

device = OptionMenu(window, devicelist, *option) #Global Widgets

def AdapterRefresh():
    new_option = os.listdir('/sys/class/net/')  # Get current adapters
    
    # Compare with the old options
    if 'old_option' not in globals():
        globals()['old_option'] = []  # Initialize old_option globally
    
    global old_option
    if old_option != new_option:
        old_option = new_option  # Update old_option
        
        # Clear existing values
        device['menu'].delete(0, 'end')
        
        # Add new values
        for j in new_option:
            device['menu'].add_command(label=j, command=lambda v=j: devicelist.set(v))
        devicelist.set("Select Adapter")
    
    # Refresh device widgets after 1 sec
    window.after(1000, AdapterRefresh)


def Command1():
	cmd = "python iwconfig.py"
	os.system(cmd)

def Command2():
	#cmd = "python startmon.py"
	cmd="gnome-terminal --command='"'bash -c "'"sudo airmon-ng check kill;sudo systemctl start NetworkManager;sudo airmon-ng start "+devicelist.get()+"; sleep 1"'"'"'"
	
	os.system(cmd)

def Command3():
	#cmd = "python stopmon.py"
	cmd="gnome-terminal --command='"'bash -c "'"sudo airmon-ng check kill;sudo systemctl start NetworkManager;sudo airmon-ng stop "+devicelist.get()+"; sleep 1"'"'"'"
	#cmd="gnome-terminal --command='"'bash -c "'"sudo airmon-ng check kill;sudo systemctl start NetworkManager;sudo airmon-ng stop wlan0; sleep 1"'"'"'"
	
	os.system(cmd)

def Command4():
	cmd = "gnome-terminal --command='"'bash -c "'"sudo airodump-ng "+devicelist.get()+"; sleep 60"'"'"'"
	os.system(cmd)


def Command5():
	cmd = "gnome-terminal --command='"'bash -c "'"sudo wash -i "+devicelist.get()+"; sleep 60"'"'"'"
	os.system(cmd)


def Command6():
	window.destroy() #close this tkinter GUI
	cmd = "python manualMAC.py"
	os.system(cmd)


def Command7():
	cmd="gnome-terminal --command='"'bash -c "'"sudo ifconfig "+devicelist.get()+" down; sleep 0.1"'"'"'"
	os.system(cmd)

	cmd="gnome-terminal --command='"'bash -c "'"sudo macchanger -r "+devicelist.get()+"; sleep 10"'"'"'"
	os.system(cmd)

	cmd="gnome-terminal --command='"'bash -c "'"sudo ifconfig "+devicelist.get()+" up; sleep 0.1"'"'"'"
	os.system(cmd)


def Command8():
	window.destroy() #close this tkinter GUI
	cmd = "python bullyCustomWPS.py"
	os.system(cmd)


def Command9():
	window.destroy() #close this tkinter GUI
	cmd = "python reaverCustomWPS.py"
	os.system(cmd)


def Command10():
	window.destroy() #close this tkinter GUI
	cmd = "python jammingWiFiofAPofClient.py"
	os.system(cmd)

def Command11():
	window.destroy() #close this tkinter GUI
	cmd = "python jammingWiFiofAP.py"
	os.system(cmd)

def Command12():
	cmd = cmd="gnome-terminal --command='"'bash -c "'"sudo wifite; sleep 600"'"'"'"
	os.system(cmd)

def Command13():
	window.destroy() #close this tkinter GUI

##################################################change
#option = os.listdir('/sys/class/net/')
#
#devicelist = StringVar()
#
#for i in range(len(option)):
#	if (option[i] == 'wlan0mon'):
#		devicelist.set('wlan0mon')
#		break
#	else:
#		devicelist.set("Select Adapter")
#devicelist.get()	#this is used to get dropdown menu seleted item's string
AdapterRefresh()
#device = OptionMenu(window, devicelist, *option)
#device.config(width=42)
device.grid(row=0, column=1, pady=2, columnspan=2)
##################################################

button1 = Button(window, text='Show WiFi Adapter', command=Command1, width=44)
button1.grid(row=1, column=1, pady=2, columnspan=2)

button2 = Button(window, text='Start Monitor Mode', command=Command2, width=20)
button2.grid(row=2, column=1, pady=2)

button3 = Button(window, text='Stop Monitor Mode', command=Command3, width=20)
button3.grid(row=2, column=2, pady=2)

button4 = Button(window, text='Scan All WiFI', command=Command4, width=20)
button4.grid(row=3, column=1, pady=2)

button5 = Button(window, text='Scan WPS WiFi', command=Command5, width=20)
button5.grid(row=3, column=2, pady=2)

button6 = Button(window, text='Manual Mac', command=Command6, width=20)
button6.grid(row=4, column=1, pady=2)

button7 = Button(window, text='Random MAC', command=Command7, width=20)
button7.grid(row=4, column=2, pady=2)

button8 = Button(window, text='Bully WPS', command=Command8, width=20)
button8.grid(row=5, column=1, pady=2)

button9 = Button(window, text='Reaver WPS', command=Command9, width=20)
button9.grid(row=5, column=2, pady=2)

button10 = Button(window, text='Jamming WiFi Client', command=Command10, width=20)
button10.grid(row=6, column=1, pady=2)

button11 = Button(window, text='Jamming WiFi AP', command=Command11, width=20)
button11.grid(row=6, column=2, pady=2)

button12 = Button(window, text='Wifite', command=Command12, width=44)
button12.grid(row=7, column=1, padx=2, columnspan=2)

button13 = Button(window, text='Exit', command=Command13, width=44)
button13.grid(row=8, column=1, padx=2, columnspan=2)

window.mainloop()
