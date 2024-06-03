import requests
import subprocess

# Fetching the data
response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt").text

# Splitting the response into lines and filtering out comment lines
lines = response.splitlines()
ip_addresses = [line.strip() for line in lines if not line.startswith("#") and line.strip()]

# Adding firewall rules for each IP address
for ip in ip_addresses:
    print("Adding Rule to block:", ip)
    rule = f"netsh advfirewall firewall add rule name='BadIP' dir=out action=block remoteip={ip}"
    subprocess.run(["Powershell", "-Command", rule])

# Displaying firewall rules
print("Firewall rules added successfully.")
subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule", "name='BadIP'"])
