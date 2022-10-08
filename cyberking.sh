#! /bin/bash




echo "-----------------------------------------"
figlet TuringScanner

echo "------------------------------------------------"
echo " ---* A Reconaissance and Vulnerability scanner Tool *---"
echo ""
echo "" 
echo ""

recon(){
DOMAIN=""
Wordlist=""
read -p "Type Traget domain: " DOMAIN
# read -p "Wordlist (optional) : " Wordlist  

echo "Your domain  ===   ${DOMAIN}"

 
 
Dname=${DOMAIN}

echo "dname is ${Dname} "
mkdir $Dname
cd $Dname

echo ""

echo "Whois is running "	
sudo whois  ${DOMAIN}   | tee -a $Dname"_whois.txt" &> /dev/null 
echo "Whois is done " 

echo ""

echo "Nmap is running ......"
sudo  nmap -F $DOMAIN  | tee -a $Dname"_nmap.txt" &> /dev/null
echo "nmap is done"

echo ""

echo "Sublister is running....."
sudo sublist3r -d $DOMAIN | tee -a $Dname"_sublister".txt &> /dev/null
echo "sublister is done"

echo ""

echo "Subfinder is running....."
sudo subfinder -d $DOMAIN -nW -silent | tee -a $Dname"_subfinder".txt &> /dev/null
echo "subfinder is done"

echo ""


echo "Dirb is running ....."
sudo dirb https://www.${DOMAIN} | tee -a $Dname"_dirb".txt &> /dev/null
echo "Dirb is done"

echo ""

echo " Script Complete "
}

scan(){
echo ""
DOMAIN=""
echo ""
read -p "Type Traget domain: " DOMAIN
echo ""
Dname=${DOMAIN%.*}
echo ""

cd scanning
Dname=${DOMAIN%.*}
mkdir $Dname 
cd $Dname

mkdir 

echo "Nikto is running ... "
sudo nikto -h ${DOMAIN} | tee -a $Dname"_nikto".txt &> /dev/null
echo "Nikto is done"

echo ""

echo "Nuclei is Running ..."
sudo nuclei -u ${DOMAIN} | tee -a $Dname"_nuclei".txt &> /dev/null
echo "Nuclei is done"

echo ""



}


main(){
A=""
echo "Select Any One : "
echo ""
echo "1. Recon"
echo "2. Scanning"
echo ""
read  A

if [[ $A = "1" ]]; then 
    echo "you chose 1st option "
    recon
elif [[ $A = "2" ]]; then
    echo "you choose 2nd option "
    scan
else 
    echo "Wrong input ,  Try again !! "
fi 
echo ""
}

main