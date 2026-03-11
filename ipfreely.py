import socket
from ping3 import ping
import sys

def get_hosts_from_subnet(ip_given):
    ip_split = ip_given.split('/')
    ip = ip_split[0].split('.')
    netmask = int(ip_split[1])
    hosts = []

    if netmask == 32:
        return [ip_split[0]]
    elif netmask >= 24:
        part1 = ip[0]
        part2 = ip[1]
        part3 = ip[2]
        part4_base = int(ip[3]) + 1
        for part4 in range (part4_base, 255):
            hosts.append(f"{part1}.{part2}.{part3}.{part4}")
    elif netmask >= 16:
        part1 = ip[0]
        part2 = ip[1]
        part3_base = int(ip[2])
        for part3 in range(part3_base, 255):
            for part4 in range (1, 255):
                hosts.append(f"{part1}.{part2}.{part3}.{part4}")
    elif netmask >= 8:
        part1 = ip[0]
        part2_base = int(ip[1])
        for part2 in range(part2_base, 255):
            for part3 in range(1, 255):
                for part4 in range(1, 255):
                    hosts.append(f"{part1}.{part2}.{part3}.{part4}")
    else:
        part1_base = int(ip[0])
        for part1 in range(part1_base, 255):
            for part2 in range(1, 255):
                for part3 in range(1, 255):
                    for part4 in range(1, 255):
                        hosts.append(f"{part1}.{part2}.{part3}.{part4}")
    return hosts

def ping_host(ip):
    ping_result = ping(ip, unit='ms', timeout=1)
    return ping_result

def check_port(port, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2) #timeout so we don't hang the script if the port ain't open
    try:
        s.connect((host, int(port)))
        return f"Port {port} is OPEN"
    except:
        return f"Port {port} is CLOSED"

checkPorts = False

try:
    if sys.argv[1] == "-p":
        if "." in sys.argv[2]:
            print("The -p flag was provided with no ports. Skipping port check.")
            checkPorts = False
            subnet = sys.argv[2]
            #subnet = input("gimme a subnet: ") # <- for debugging only!
        else:
            ports = sys.argv[2].split(",")
            checkPorts = True
            try:
                subnet = sys.argv[3]
                #subnet = input("gimme a subnet: ") # <- for debugging only!
            except IndexError:
                print("No subnet was provided.")
                exit()

    else:
        checkPorts = False
        subnet = sys.argv[1]
        #subnet = input("gimme a subnet: ") # <- for debugging only!
except IndexError:
    print("No arguments were provided.")
    exit()
print(f"Pinging all hosts in subnet {subnet}")

hosts = get_hosts_from_subnet(subnet)
timeout_hosts = 0
successful_hosts = 0
failed_hosts = 0
online_hosts = []

if checkPorts:
    for host in hosts:
        ping_result = ping(host)
        if ping_result == None:
            print(f"Host {host}... Timed out.")
            timeout_hosts = timeout_hosts + 1
        elif ping_result == False:
            print(f"Host {host}... Could not connect.")
            failed_hosts = failed_hosts + 1
        else:
            print(f"Host {host}... {ping_result}ms")
            for port in ports:
                port_status = check_port(port, host)
                print(port_status)
            successful_hosts = successful_hosts + 1
            online_hosts.append(host)
else:
    for host in hosts:
        ping_result = ping(host)
        if ping_result == None:
            print(f"Host {host}... Timed out.")
            timeout_hosts = timeout_hosts + 1
        elif ping_result == False:
            print(f"Host {host}... Could not connect.")
            failed_hosts = failed_hosts + 1
        else:
            print(f"Host {host}... {ping_result}ms")
            successful_hosts = successful_hosts + 1
            online_hosts.append(host)

print(f"Results: {successful_hosts} up, {failed_hosts} down, {timeout_hosts} timed out.")
print("Online hosts:")
for host in online_hosts:
    print(host)

