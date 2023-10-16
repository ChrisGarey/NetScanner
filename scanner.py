import subprocess
import time
import sys
import threading
import argparse

# Function to display blinking dots
def display_blinking_dots():
    while not scan_completed.is_set():
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\b\b\b   \b\b\b")
        sys.stdout.flush()

# Function to print ASCII art with Figlet and Lolcat
def print_ascii_art():
    figlet_command = 'figlet "Cosmo\'s NetScanner" | lolcat'
    subprocess.call(figlet_command, shell=True)

# Print the ASCII art at the beginning
print_ascii_art()

# Ask the user for the target IP address
target_ip = input("Enter the target IP address: ")

# Ask the user for Nmap switches
nmap_switches = input("Enter Nmap switches (e.g., -sV -p 1-65535): ")

# Define the nmap command with the user-provided target IP and switches
nmap_command = f'nmap {nmap_switches} {target_ip}'

# Initialize a threading event to signal when the scan is completed
scan_completed = threading.Event()
print(' ')
print("Initializing Scan. Please wait", end='')

# Start displaying blinking dots
dot_thread = threading.Thread(target=display_blinking_dots)
dot_thread.daemon = True
dot_thread.start()

# Start the nmap scan
nmap_process = subprocess.Popen(nmap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print(' ')
# Initialize variables to count open ports and known services
open_port_count = 0
known_services = set()

# Process the nmap scan output
previous_output = []
for line in nmap_process.stdout:
    if "Host is up" in line:
        # Print the previous output before the IP address line
        for previous_line in previous_output:
            print(previous_line.strip())
        previous_output = [line]
    elif "PORT" in line:
        print(line.strip())  # Print the header
    elif "open" in line:
        open_port_count += 1
        print(line.strip())  # Print open port details
        # Extract the service name (if available)
        parts = line.split()
        if len(parts) >= 3:
            service = parts[2]
            if service != "unknown":
                known_services.add(service)
        if open_port_count % 10 == 0:
            input("Press Enter to continue...")
            # Clear the "Press Enter to continue..." message
            print("\033[A\033[K", end='')
    else:
        previous_output.append(line)

# Close the nmap process
nmap_process.kill()

# Signal that the scan is completed
scan_completed.set()

# Join the dot_thread to stop blinking dots
dot_thread.join()

# Print the scan completion message with open port count and count of known services
known_services_count = len(known_services)
print(f"Scan completed. Open Ports: {open_port_count} | Known Services: {known_services_count if known_services_count > 0 else 'None'}")
