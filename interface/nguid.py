import tkinter as tk
import socket
import nmap
import socket
import pyfiglet
import sys
import datetime
import time
import whois

# Top level window
frame = tk.Tk()
frame.title("TuringScanner")
frame.geometry('400x600')
# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
	inp = inputtxt.get(1.0, "end-1c")
	target=inp
	ip_address = socket.gethostbyname(target)
	lbl.config(text = "Provided Input: "+ip_address)
	findInfoWhois();

def findInfoWhois():
	inp = inputtxt.get(1.0, "end-1c")
	target=inp
	print("\n\tFind basic traget information....")
	w=whois.whois(target)
	registrar=str(w['registrar'])
	creation_date=str(w['creation_date'])
	expiration_date=str(w['expiration_date'])
	name_servers=str(w['name_servers'])
	country=str(w['country'])
	emails=str(w['emails'])
	lbl.config(text = "Registerar:"+registrar+"\nCreation Date:"+creation_date+
		               "Expiration Date:"+expiration_date+"\nName Servers:"+name_servers+"\nCountry:"+country+"\nEmails:"+emails)


# TextBox Creation
inputtxt = tk.Text(frame,
				height = 5,
				width = 20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Print",
						command = printInput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lb12=tk.Label(frame,text="")

lbl.pack(pady=20, anchor="w")
lb12.pack(pady=20, anchor="w")
frame.mainloop()
