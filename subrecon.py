import os
import subprocess 
import pyfiglet  


def create_banner():
    banner_text = pyfiglet.figlet_format("SubRecon", font="slant")
    print(banner_text)
    
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

def save_output(filename, output):
    with open(filename, 'w') as f:
        f.write(output)

def recon(target):
    create_banner()
    print(f"Running recon on: {target}")
    

    print("Finding subdomains with Subfinder...")
    subdomains = run_command(f"subfinder -d {target} --silent ")
    save_output("subdomains888.txt", subdomains.decode())

    print("Running findomin...")
    findomain = run_command(f"findomain -t {target} " )
    save_output("findomain888.txt", findomain.decode())

    print("Finding assets with assetfinder...")
    assets = run_command(f"assetfinder -subs-only {target} " )
    save_output("assets888.txt", assets.decode())
    
    sort = run_command(f" cat subdomain888.txt findomain888.txt assest888.txt >> main888.txt")
    
    uniq = run_command(f" sort main888.txt | uniq -i > domain888.txt")
    
    print("Finding Status-code with httpx-toolkit...")
    httpx = run_command(f"httpx-toolkit -l domain888.txt -sc 200 -mc'200, 300'")
    save_output("httpx.txt", httpx.decode())    
    
    dell = run_command(f" rm -rf findomain888.txt assets888.txt subdomains888.txt domain888.txt main888.txt ")

    
    print("Running dnsrecon...\n")
    dnsrecon_result = run_command(f"dnsrecon -d {target}")
    save_output("dnsrecon_result.txt", dnsrecon_result.decode())
    print(" THANK YOU \n")
    
   
if __name__ == "__main__":
    target = input("Enter the target for scan: ")
    recon(target)
