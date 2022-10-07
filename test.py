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

with open('output.txt') as f:
    for line in f:
        print("\t",line)