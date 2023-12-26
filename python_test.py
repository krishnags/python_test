# Sample Python code to retrieve system information on Linux

import os

def get_system_info():
    """Retrieve and print basic system information."""
    try:
        # Get hostname
        hostname = os.uname().nodename
        
        # Get CPU information
        with open('/proc/cpuinfo', 'r') as file:
            cpu_info = file.read().splitlines()
            cpu_model = [line.split(':')[-1].strip() for line in cpu_info if 'model name' in line][0]
        
        # Get memory information
        with open('/proc/meminfo', 'r') as file:
            mem_info = file.read().splitlines()
            total_memory = [line.split(':')[1].strip() for line in mem_info if 'MemTotal' in line][0]
            total_memory = f"{int(total_memory.split()[0]) // 1024} MB"  # Convert to MB
        
        # Print system information
        print(f"Hostname: {hostname}")
        print(f"CPU Model: {cpu_model}")
        print(f"Total Memory: {total_memory}")
        
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def main():
    get_system_info()

if __name__ == '__main__':
    main()
