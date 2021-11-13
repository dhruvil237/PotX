import configparser
import sys
from potx import HoneyPot

# Load config
config_filepath = 'potx.ini'
config = configparser.ConfigParser()
config.read(config_filepath)

ports = config.get('default', 'ports', raw=True, fallback="1234")
host = config.get('default', 'host', raw=True, fallback="0.0.0.0")
log_filepath = config.get('default', 'logfile', raw=True, fallback="potx.log")

# Double check ports provided
ports_list = []
try:
    ports_list = ports.split(',')
except Exception as e:
    print('[-] Error parsing ports: %s.\nExiting.', ports)
    sys.exit(1)

# Launch honeypot
honeypot = HoneyPot(host, ports_list, log_filepath)
honeypot.run()
