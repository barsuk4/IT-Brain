import re

def is_valid_ip_address(ip_address):
    pattern = r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b"
    return re.match(pattern, ip_address) is not None

# Приклади перевірки
ip_addresses = ["192.168.0.1", "192.168.270.1", "255.254.192.", "23.257.33.11", "168.119.91.111"]
for ip in ip_addresses:
    if is_valid_ip_address(ip):
        print(f"{ip} - валідна IP-адреса")
    else:
        print(f"{ip} - не валідна IP-адреса")
