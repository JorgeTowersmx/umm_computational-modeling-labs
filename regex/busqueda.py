import re

texto = "Mi correo es jtorresb@email.com"

busqueda = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", texto)

print(texto)
print(busqueda)