import re

log_apache = """
192.168.1.10 - - [14/May/2026:08:15:23 -0600] "GET /index.html HTTP/1.1" 200 1543
10.0.0.25 - - [14/May/2026:08:16:02 -0600] "POST /login HTTP/1.1" 302 621
172.16.5.44 - - [14/May/2026:08:17:10 -0600] "GET /images/logo.png HTTP/1.1" 200 8321
203.0.113.55 - - [14/May/2026:08:18:41 -0600] "GET /admin HTTP/1.1" 403 721
198.51.100.17 - - [14/May/2026:08:19:05 -0600] "GET /phpmyadmin HTTP/1.1" 404 512
192.168.1.10 - - [14/May/2026:08:20:18 -0600] "GET /dashboard HTTP/1.1" 200 4123
10.0.0.25 - - [14/May/2026:08:21:33 -0600] "POST /auth HTTP/1.1" 401 312
66.249.66.1 - - [14/May/2026:08:22:44 -0600] "GET /robots.txt HTTP/1.1" 200 88
185.220.101.42 - - [14/May/2026:08:23:10 -0600] "GET /wp-login.php HTTP/1.1" 404 421
45.33.32.156 - - [14/May/2026:08:24:01 -0600] "GET /backup.zip HTTP/1.1" 403 128
"""

# Expresión regular para detectar direcciones IPv4
patron_ip = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
# \b((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b
# Buscar todas las IPs
ips = re.findall(patron_ip, log_apache)

print("IPs encontradas:")
for ip in ips:
    print(ip)

print("\nTotal de IPs encontradas:", len(ips))

# IPs únicas
ips_unicas = set(ips)

print("\nIPs únicas:")
for ip in ips_unicas:
    print(ip)

print("\nTotal de IPs únicas:", len(ips_unicas))