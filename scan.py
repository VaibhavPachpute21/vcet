import socket
import whois

def printIp (domain) :
    ip_address = socket.gethostbyname(domain)
    sayIp = f'Domain Name:{domain}\nDomain IP:{ip_address}'

    w=whois.whois(domain)
    Registerar=str(w['registrar'])
    Creation=str(w['creation_date'])
    Expiration=str(w['expiration_date'])
    Servers=str(w['name_servers'])
    Country=str(w['country'])
    Emails=str(w['emails'])

    basicInfo=f'\nRegisterar:{Registerar}\nCreation Date:{Creation}\nExpiration Date:{Expiration}\nName Server:{Servers}\nCountry:{Country}\nEmails:{Emails}'

    return sayIp+basicInfo