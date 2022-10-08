import socket
import whois
import nmap
import subprocess

scanner = nmap.PortScanner()


def printIp (domain) :
    nmapStr=[]
    subDomainList=[]
    limit=0
    n=0
    ip_address = socket.gethostbyname(domain)
    sayIp = f'Domain Name:{domain}\nDomain IP:{ip_address}'

    # SUBLISTER
    command = "subfinder -d "+domain+" -silent -o ./"+domain+"_subdomains.txt"
    fName=domain+"_subdomains.txt"
    subprocess.call(command, shell=True)
    with open(fName,'r') as f:
        for line in f:
            print("\t",line)
            limit=limit+1
            if limit<=5:
                subDomainList.append(line)
            print(subDomainList)


    # NMAP
    res=scanner.scan(hosts=ip_address,arguments="-f");
    oports=res['scan'][ip_address]['tcp'];
    l=len(res['scan'][ip_address]['tcp']);
    for port in oports:
        print("\t",port, oports[port]['name'], oports[port]['state']);
        n=n+1
        if n <=5:
            nmapStr.append(str(port)+" "+str(oports[port]['name'])+" "+str(oports[port]['state']));
    # WHOIS
    w=whois.whois(domain)
    Registerar=str(w['registrar'])
    Creation=str(w['creation_date'])
    Expiration=str(w['expiration_date'])
    Servers=str(w['name_servers'])
    Country=str(w['country'])
    Emails=str(w['emails'])
    basicInfo=f'\nRegisterar:{Registerar}\nCreation Date:{Creation}\nExpiration Date:{Expiration}\nName Server:{Servers}\nCountry:{Country}\nEmails:{Emails}\nNmap:'
    
    return sayIp+basicInfo+str(nmapStr)+"\n"+"SubDomains:"+str(subDomainList)