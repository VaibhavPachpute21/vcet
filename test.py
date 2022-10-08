# import whois

# w=whois.whois('vcet.edu.in')


# print(w)
# print(f"""
# 	registerar:{w['registrar']}
# 	{w['creation_date']}
# 	{w['expiration_date']}
# 	{w['name_servers']}
# 	{w['country']}
# 	{w['emails']}
# 	""")

# with open('output.txt') as f:
#     for line in f:
#         print("\t",line)

# import subprocess
# d="vcet.edu.in";

# command = "subfinder -d "+d+" -silent"
# print(command)
# subprocess.call(command, shell=True)

import os

for filename in os.listdir("vcet.ac.in"):
   with open(os.path.join("vcet.ac.in", filename), 'r') as f:
       text = f.read()
       print(text)

