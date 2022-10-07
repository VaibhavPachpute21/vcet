import nmap
import socket
import pyfiglet
import sys
import datetime
import time
import whois

scanner = nmap.PortScanner()

# print(pyfiglet.figlet_format("TuringScanner"))

target=sys.argv[1]
ip_address = socket.gethostbyname(target)

print("*"*50);

print(f"\tTarget Domain: {target}")
print(f"\tIP Address: {ip_address}")

def nmapScan():
	print("\n\tScanner is running....")
	res=scanner.scan(hosts=ip_address,arguments="-f --script=dns-brute -oN ./output/nmap.txt ");
	# print(res)
	# print(res['nmap']['scaninfo']['tcp']["services"])
	oports=res['scan'][ip_address]['tcp'];
	l=len(res['scan'][ip_address]['tcp']);
	for port in oports:
		print("\t",port, oports[port]['name'], oports[port]['state'])
	print("\t",datetime.datetime.now(),"\n")


def findInfoWhois():
	print("\n\tFind basic traget information....")
	w=whois.whois(target)
	md=str(w)
	print(f"""
	Registerar Name  :{w['registrar']}
	Creation Date    :{w['creation_date']}
	Expiration Date  :{w['expiration_date']}
	Name Servers     :{w['name_servers']}
	Country          :{w['country']}
	Emails           :{w['emails']}	
	""")
	a = open('./output/basicInfo.txt', 'w')
	a.write(md)
	a.close()

findInfoWhois()
nmapScan()
# while(True):
#     nmapScan()
#     time.sleep(20)

