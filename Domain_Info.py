import whois

domain = input("Input your domain : ")
domain_info = whois.whois(domain)

for key,value in domain_info.items():
    print(key,":", value)
