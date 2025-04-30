import winrm
from Commons.utils import *

config = load_config()
machine = config["machine"]
hostname = machine['hostname']
username = machine['username']
password=machine['password']


# Create a session
s = winrm.Session(f'http://{hostname}:5985/wsman', auth=(username, password))

# Contents of requirements.txt
with open('/Users/ravina/PycharmProjects/BAClientAutomationProject/requirements.txt', 'r') as file:
    requirements_content = file.read()

# PowerShell script to install packages from the above content
ps_script = f"""
$requirements = @"
{requirements_content}
"@
if (!(Test-Path -Path "C:\\Temp")) {{
    New-Item -ItemType Directory -Path "C:\\Temp"
}}
$requirements | Out-File -FilePath "C:\\Temp\\requirements.txt" -Encoding ASCII
Write-Output "Installing packages from requirements.txt..."
pip install --requirement C:\\Temp\\requirements.txt -qqq
Write-Output "Installed packages successfully."
"""

#r = s.run_ps(ps_script)
#print(r.std_out.decode())
#print(r.std_err.decode())


# Path to your script on your Mac
#local_script_path = '/Users/ravina/PycharmProjects/BAClientAutomationProject/main.py'
local_script_path = '/Users/ravina/PycharmProjects/BAClientAutomationProject/Scripts/install_package.py'


# Read the contents of the Python script
with open(local_script_path, 'r') as file:
    script_content = file.read()


# PowerShell script to run the Python code directly
ps_script = f"""
$python_code = @"
{script_content}
"@
$python_code | python
"""

# Run the PowerShell script remotely
r = s.run_ps(ps_script)

# Print the output
print("Standard Output:")
print(r.std_out.decode())

print("Standard Error:")
print(r.std_err.decode())




