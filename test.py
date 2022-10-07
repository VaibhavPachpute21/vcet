import nmap


scanner = nmap.PortScanner()
res=scanner.scan(hosts='vcet.edu.in',arguments="--script=dns-brute");

print(res)

