# CREATING A PORT SCANNER USING SOCKET 

import socket
import sys
import time
import threading

usage = "python Port_Scanner.py TARGET START_PORT END_PORT"

print("-"*70)
print("Python Simple Port Scanner")
print("-"*70)

# Corrected variable name
start_time = time.time() 

if (len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    # Corrected function to resolve hostname to IP
    target = socket.gethostbyname(sys.argv[1]) 

except socket.gaierror:
    print("Name resolution error: Could not find host.")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target", target)


def scan_port(port):
    # This print statement can be noisy for large port ranges, you can comment it out if you wish
    # print("Scanning port:", port) 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))
    if (not conn):
        # Corrected f-string formatting
        print(f"[+] Port {port} is OPEN") 
    s.close()


for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()

# NOTE: The script will print the elapsed time immediately because threading
# starts the scans in the background. The actual scan may take longer.
end_time = time.time()
# Corrected variable name reference
print("Time elapsed:", end_time - start_time, 's')