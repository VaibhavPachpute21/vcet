import tkinter as tk
import socket
import nmap
import socket
import pyfiglet
import sys
import datetime
import time
import whois
import subprocess

# Top level window
frame = tk.Tk()
frame.title("TuringScanner")
frame.geometry('400x600')
# Function for getting Input
# from textbox and printing it
# at label widget
target=''

def printInput():
	inp = inputtxt.get(1.0, "end-1c")
	target=inp
	ip_address = str(socket.gethostbyname(target))
	print(ip_address)

	olbl1.config(text ="Domain Name: "+target+ "\n Domain IP: "+ ip_address )
	findInfoWhois();

def findInfoWhois():
	print("\n\tFind basic traget information....")
	hlbl2.config(text ="Finding Basic Taget Information...." )
	w=whois.whois(target)
	print(w)
	registrar=str(w['registrar'])
	creation_date=str(w['creation_date'])
	expiration_date=str(w['expiration_date'])
	name_servers=str(w['name_servers'])
	country=str(w['country'])
	emails=str(w['emails'])
	olbl2.config(text ="Registerar: "+registrar+" \n Creation Date: "+creation_date+
		               "\n Expiration Date: "+expiration_date+"\n Name Servers: "+name_servers+"\n Country: "+country+"\n Emails: "+emails)
	# subfindeR();


def subfindeR():
	command = "subfinder -d "+target+" -silent -o ./subfinder.txt "
	subprocess.call(command, shell=True)
	with open('subfinder.txt') as f:
		for line in f:
			print("\t subfindeR:",line)


# TextBox Creation
inputtxt = tk.Text(frame,height = 2,	width = 20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,text = "Scan",command = printInput)
printButton.pack()

#Heading Label
hlbl1=tk.Label(frame,text="")
hlbl2=tk.Label(frame,text="")
# Label Creation
olbl1 = tk.Label(frame, text = "")
olbl2=tk.Label(frame,text="")

olbl1.pack()
olbl2.pack()

hlbl1.pack()
hlbl2.pack()

frame.mainloop()
