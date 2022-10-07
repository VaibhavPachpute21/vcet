main(){
domain=""

figlet TuringScanner

read -p "Enter Domain to Scan: " A
# read  A

python3 Scanner.py ${A}

subfinder -d ${A} -silent


}

main