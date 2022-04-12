import requests, os, sys, ctypes, json, datetime, getpass
from colorama import Fore

def banner():
    print(f"""
                        {Fore.RED}Dev By Tahg{Fore.RESET}
██╗██████╗░░░░░░░░██╗░░░░░░░██╗██╗░░██╗░█████╗░██╗░██████╗
██║██╔══██╗░░░░░░░██║░░██╗░░██║██║░░██║██╔══██╗██║██╔════╝
██║██████╔╝█████╗░╚██╗████╗██╔╝███████║██║░░██║██║╚█████╗░
██║██╔═══╝░╚════╝░░████╔═████║░██╔══██║██║░░██║██║░╚═══██╗
██║██║░░░░░░░░░░░░░╚██╔╝░╚██╔╝░██║░░██║╚█████╔╝██║██████╔╝
╚═╝╚═╝░░░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░╚════╝░╚═╝╚═════╝░
    {Fore.RED}GitHub: {Fore.BLUE}https://github.com/T4hg/ {Fore.RESET}
    """)

def whois():
    prefix = f"{Fore.RED}IP {Fore.BLUE}Whois {Fore.GREEN}· {Fore.WHITE}"
    system_prefix = f"{Fore.RED}$ {Fore.GREEN}"
    domain = input(prefix + "Domain (EXAMPLE: example.es): ")

    config = open("config.json", "r")
    config_load = json.load(config)
    key = config_load.get('key')

    try:
        os.mkdir(rf"C:\Users\{getpass.getuser()}\Documents\IpWhois-APP")
    except:
        pass
    file = open(rf"C:\Users\{getpass.getuser()}\Documents\IpWhois-APP\{domain}.json", 'w+')
    response = requests.get(f"https://api.ip2whois.com/v2?key={key}&domain={domain}&format=json").text
    file.write(response)
    file.close()
    file1 = open(rf"C:\Users\{getpass.getuser()}\Documents\IpWhois-APP\{domain}.json", 'r')
    whois = json.load(file1)
    print(f"""
    {Fore.GREEN}Details:
    {Fore.RED}Domain: {Fore.WHITE}{whois.get('domain')}
    {Fore.RED}Domain ID: {Fore.WHITE}{whois.get('domain_id')}
    {Fore.RED}Status: {Fore.WHITE}{whois.get('status')}
    {Fore.RED}Create Date: {Fore.WHITE}{whois.get('create_date')}
    {Fore.RED}Update Date: {Fore.WHITE}{whois.get('update_date')}
    {Fore.RED}Expire Date: {Fore.WHITE}{whois.get('expire_date')}
    {Fore.RED}Domain Age: {Fore.WHITE}{whois.get('domain_age')}
    {Fore.RED}Whois Server: {Fore.WHITE}{whois.get('whois_server')}

    {Fore.GREEN}Registrar:
    {Fore.RED}Iana ID: {Fore.WHITE}{whois['registrar'].get('iana_id')}
    {Fore.RED}Name: {Fore.WHITE}{whois['registrar'].get('name')}
    {Fore.RED}Url: {Fore.WHITE}{whois['registrar'].get('url')}

    {Fore.GREEN}Registrant:
    {Fore.RED}Name: {Fore.WHITE}{whois['registrant'].get('name')}
    {Fore.RED}Organization: {Fore.WHITE}{whois['registrant'].get('organization')}
    {Fore.RED}Street Address: {Fore.WHITE}{whois['registrant'].get('street_address')}
    {Fore.RED}City: {Fore.WHITE}{whois['registrant'].get('city')}
    {Fore.RED}Region: {Fore.WHITE}{whois['registrant'].get('region')}
    {Fore.RED}Zip Code: {Fore.WHITE}{whois['registrant'].get('zip_code')}
    {Fore.RED}Country: {Fore.WHITE}{whois['registrant'].get('country')}
    {Fore.RED}Phone: {Fore.WHITE}{whois['registrant'].get('phone')}
    {Fore.RED}Fax: {Fore.WHITE}{whois['registrant'].get('fax')}
    {Fore.RED}Email: {Fore.WHITE}{whois['registrant'].get('email')}

    {Fore.GREEN}Admin:
    {Fore.RED}Name: {Fore.WHITE}{whois['admin'].get('name')}
    {Fore.RED}Organization: {Fore.WHITE}{whois['admin'].get('organization')}
    {Fore.RED}Street Address: {Fore.WHITE}{whois['admin'].get('street_address')}
    {Fore.RED}City: {Fore.WHITE}{whois['admin'].get('city')}
    {Fore.RED}Region: {Fore.WHITE}{whois['admin'].get('region')}
    {Fore.RED}Zip Code: {Fore.WHITE}{whois['admin'].get('zip_code')}
    {Fore.RED}Country: {Fore.WHITE}{whois['admin'].get('country')}
    {Fore.RED}Phone: {Fore.WHITE}{whois['admin'].get('phone')}
    {Fore.RED}Fax: {Fore.WHITE}{whois['admin'].get('fax')}
    {Fore.RED}Email: {Fore.WHITE}{whois['admin'].get('email')}

    {Fore.GREEN}Tech:
    {Fore.RED}Name: {Fore.WHITE}{whois['tech'].get('name')}
    {Fore.RED}Organization: {Fore.WHITE}{whois['tech'].get('organization')}
    {Fore.RED}Street Address: {Fore.WHITE}{whois['tech'].get('street_address')}
    {Fore.RED}City: {Fore.WHITE}{whois['tech'].get('city')}
    {Fore.RED}Region: {Fore.WHITE}{whois['tech'].get('region')}
    {Fore.RED}Zip Code: {Fore.WHITE}{whois['tech'].get('zip_code')}
    {Fore.RED}Country: {Fore.WHITE}{whois['tech'].get('country')}
    {Fore.RED}Phone: {Fore.WHITE}{whois['tech'].get('phone')}
    {Fore.RED}Fax: {Fore.WHITE}{whois['tech'].get('fax')}
    {Fore.RED}Email: {Fore.WHITE}{whois['tech'].get('email')}

    {Fore.GREEN}Billing:
    {Fore.RED}Name: {Fore.WHITE}{whois['billing'].get('name')}
    {Fore.RED}Organization: {Fore.WHITE}{whois['billing'].get('organization')}
    {Fore.RED}Street Address: {Fore.WHITE}{whois['billing'].get('street_address')}
    {Fore.RED}City: {Fore.WHITE}{whois['billing'].get('city')}
    {Fore.RED}Region: {Fore.WHITE}{whois['billing'].get('region')}
    {Fore.RED}Zip Code: {Fore.WHITE}{whois['billing'].get('zip_code')}
    {Fore.RED}Country: {Fore.WHITE}{whois['billing'].get('country')}
    {Fore.RED}Phone: {Fore.WHITE}{whois['billing'].get('phone')}
    {Fore.RED}Fax: {Fore.WHITE}{whois['billing'].get('fax')}
    {Fore.RED}Email: {Fore.WHITE}{whois['billing'].get('email')}
    """)
    d = datetime.datetime.now()
    file_txt = open("Registry.txt", "a+")
    file_txt.write(f"{d}\nKey: {key}\nDomain: {domain}\n\n")
    file_txt.close()
    file1.close()
    print(f"""
    {Fore.GREEN}If you like the app, don't forget to give it a {Fore.YELLOW}star {Fore.GREEN}on GitHub

    {Fore.WHITE}ENTER TO BACK""")
    input()
    whois()

if __name__ == '__main__':
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"IpWhois | Developed by Tahg - GitHub: https://github.com/T4hg/")
    banner()
    whois()