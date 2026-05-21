import re
from collections import Counter

REGLAS = {
    "SQL Injection": {
        "regex": r"('|%27)\s*(OR|AND)\s*('|%27)?\d+=\d+|UNION\s+SELECT|--",
        "severidad": "Alta"
    },
    "Path Traversal": {
        "regex": r"\.\./|\.\.\\|etc/passwd",
        "severidad": "Alta"
    },
    "XSS": {
        "regex": r"<script>|javascript:|onerror=",
        "severidad": "Alta"
    },
    "Acceso a admin": {
        "regex": r"/admin|/wp-admin|/administrator",
        "severidad": "Media"
    },
    "Login fallido": {
        "regex": r"POST\s+/login.*\"\s+401",
        "severidad": "Media"
    }
}

patron_log = re.compile(
    r'(?P<ip>\b(?:\d{1,3}\.){3}\d{1,3}\b).*'
    r'\[(?P<fecha>.*?)\].*'
    r'"(?P<metodo>GET|POST|PUT|DELETE)\s+(?P<url>\S+).*"\s+'
    r'(?P<codigo>\d{3})'
)

archivo_log = "miniSIEM/logs/access.log"

eventos = []
alertas = []
contador_ips = Counter()
contador_codigos = Counter()

with open(archivo_log, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        resultado = patron_log.search(linea)

        if resultado:
            evento = resultado.groupdict()
            eventos.append(evento)

            ip = evento["ip"]
            codigo = evento["codigo"]

            contador_ips[ip] += 1
            contador_codigos[codigo] += 1

            for nombre_regla, datos in REGLAS.items():
                if re.search(datos["regex"], linea, re.IGNORECASE):
                    alertas.append({
                        "ip": ip,
                        "fecha": evento["fecha"],
                        "regla": nombre_regla,
                        "severidad": datos["severidad"],
                        "linea": linea
                    })

print("===== MINI SIEM REPORT =====")
print(f"Total de eventos analizados: {len(eventos)}")
print("\nTop IPs:")
for ip, total in contador_ips.most_common(5):
    print(f"{ip}: {total} eventos")

print("\nCódigos HTTP:")
for codigo, total in contador_codigos.items():
    print(f"{codigo}: {total}")

print("\nAlertas:")
for alerta in alertas:
    print(f"[{alerta['severidad']}] {alerta['regla']} - IP: {alerta['ip']} - {alerta['fecha']}")