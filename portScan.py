# Import the socket module to handle network connections
import socket


# Define the main scanning function
def scan_ports(host, start_port, end_port):
# Print the target being scanned
    print(f"Scanning {host} from port {start_port} to {end_port}...\n")
    open_ports = [] # List to store open ports

# Loop through the range of ports specified
    for port in range(start_port, end_port + 1):
 # Create a TCP socket (IPv4 + TCP stream)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout so it doesn’t hang on closed ports
            s.settimeout(0.7) 

            # Attempt to connect to the target host and port
            result = s.connect_ex((host, port))

             # connect_ex returns 0 if connection is successful (port is open)
            if result == 0:
                print(f"✅ Port {port} is OPEN")
                open_ports.append(port)
            else:
                print(f"❌ Port {port} is CLOSED")

   # Print scan completion message
    print("\nScan complete.")

    # Return list of open ports (could be saved to a file later)
    return open_ports


if __name__ == "__main__":
     # Prompt user for the target host
    target_host = input("Enter the host IP : ")

    # Prompt user for the port range to scan
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))

     # Call the scan function
    scan_ports(target_host, start, end)