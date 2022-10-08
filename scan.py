import socket
import whois

def printIp (domain) :
    ip_address = socket.gethostbyname(domain)
    sayIp = f'Domain Name:{domain}\nDomain IP:{ip_address}'
    w=whois.whois(domain)
    return sayIp+str(w)