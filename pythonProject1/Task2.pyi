import os

def loadFile(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def validate(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for item in parts:
        if not item.isdigit() or not 0 <= int(item) <= 255:
            return False
    return True

def check_if_private(ip):
    parts = [int(part) for part in ip.split('.')]
    # 10.0.0.0-10.255.255.255
    if parts[0] == 10:
        return True
    # 172.16.0.0-172.31.255.255
    elif parts[0] == 172 and 16 <= parts[1] <= 31:
        return True
    # 192.168.0.0-192.168.255.255
    elif parts[0] == 192 and parts[1] == 168:
        return True
    return False

def process(data):
    private_ips = []
    public_ips = []
    unique_domains = set()
    unique_ips = set()

    for line in data:
        line = line.strip()
        if not line:
            continue
        parts = line.replace(',', ' ').replace('\t', ' ').split()
        if len(parts) < 2:
            continue

        ip, domain = parts[0], parts[1]

        if validate(ip):
            unique_ips.add(ip)
            unique_domains.add(domain)
            if check_if_private(ip):
                private_ips.append(f"{ip} - {domain}")
            else:
                public_ips.append(f"{ip} - {domain}")

    return private_ips, public_ips, unique_domains, unique_ips

def display(private_ips, public_ips, unique_domains, unique_ips):
    print("Private IP Addresses:")
    for ip in private_ips:
        print(ip)
    print("\nPublic IP Addresses:")
    for ip in public_ips:
        print(ip)
    print("\nUnique Domains:")
    for domain in unique_domains:
        print(domain)
    print("\nUnique IP Addresses:")
    for ip in unique_ips:
        print(ip)


filename = "ip.txt"
data = load_file(filename)
if data is not None:
    private_ips, public_ips, unique_domains, unique_ips = process(data)
    display(private_ips, public_ips, unique_domains, unique_ips)





