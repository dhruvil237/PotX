# PotX
Honeypot for TCP network connections

# Installation
pip install PotX

This project has been hosted on pypi --> https://pypi.org/project/PotX/

# Initializing honeypot
Using python –m potx command on user’s machine
The ports assigned to honeypot from .ini file are 7774, 7775, 7776

# Checking for active ports
netstat –q command is used to display available ports
Here presence of ports 7774, 7775, 7776 signifies that our honeypot is active

# Hacking attempts
On the honeypot port considering it as open but the access was denied and connection closed

# Attempts stored in log file
With information about date, timestamp, accessed port, adversary’s IP, message passed
