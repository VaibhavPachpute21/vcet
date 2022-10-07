main(){
domain=""

figlet TuringScanner

read -p "Enter Domain to Scan: " A
# read  A


python3 Scanner.py ${A}

echo "Checking for Subdomains...."
echo " "
subfinder -d vcet.edu.in  -silent -o ./output/subfinder.txt 
# subfinder -d ${A} -silent -a $A"_subfinder".txt &> /dev/null


}

main