import re

# ==========================
# DATASET DE EJEMPLO
# ==========================

datos = [
    {
        "nombre": "Jorge Torres",
        "telefono": "8123456789",
        "email": "jorge@email.com"
    },
    {
        "nombre": "Ana Lopez",
        "telefono": "(81) 2345-6789",  # DATOS SINTETICOS
        "email": "ana@email.com"
    },
    {
        "nombre": "Carlos###",
        "telefono": "+52 81 1234 5678",
        "email": "carlos@test"
    },
    {
        "nombre": "Maria!!!",
        "telefono": "81-9999-1111",
        "email": "maria@gmail.com"
    },
    {
        "nombre": "Pedro@@@",
        "telefono": "SIN TELEFONO",
        "email": "pedro@@mail.com"
    }
]

mensajes = [
    "Cliente ID: 12345",
    "Usuario 9988 activo",
    "Ref=556677"
]

textos = [
    "Mi correo es jorge@email.com",
    "Contacto: soporte@test.org",
    "Sin email registrado"
]

transacciones = [
    "Pago con tarjeta 4111111111111111",
    "Sin tarjeta registrada",
    "Visa 4012888888881881"
]

codigos_postales = [
    "64000",
    "ABC12",
    "123456",
    "88730"
]

# ==========================
# EXPRESIONES REGULARES
# ==========================

patron_email_validacion = r"^[\w\.-]+@[\w\.-]+\.\w+$"
patron_no_numeros = r"\D"
patron_telefono_10 = r"^\d{10}$"
patron_nombre_limpio = r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]"
patron_numeros = r"\d+"
patron_email_busqueda = r"[\w\.-]+@[\w\.-]+\.\w+"
patron_visa = r"\b4[0-9]{12}(?:[0-9]{3})?\b"
patron_cp = r"^\d{5}$"

# ==========================
# 1. LIMPIEZA Y VALIDACIÓN
# ==========================

print("=" * 60)
print("LIMPIEZA Y VALIDACIÓN DE DATASET")
print("=" * 60)

for registro in datos:
    nombre_original = registro["nombre"]
    telefono_original = registro["telefono"]
    email = registro["email"]

    # Limpiar nombre
    nombre_limpio = re.sub(patron_nombre_limpio, "", nombre_original)

    # Limpiar teléfono
    telefono_limpio = re.sub(patron_no_numeros, "", telefono_original)

    # Validar email
    email_valido = re.fullmatch(patron_email_validacion, email)

    # Validar teléfono
    telefono_valido = re.fullmatch(patron_telefono_10, telefono_limpio)

    print(f"\nRegistro original:")
    print(f"Nombre: {nombre_original}")
    print(f"Teléfono: {telefono_original}")
    print(f"Email: {email}")

    print(f"\nRegistro limpio:")
    print(f"Nombre limpio: {nombre_limpio}")
    print(f"Teléfono limpio: {telefono_limpio}")

    print(f"Email válido: {'SI' if email_valido else 'NO'}")
    print(f"Teléfono válido: {'SI' if telefono_valido else 'NO'}")

# ==========================
# 2. EXTRAER NÚMEROS
# ==========================

print("\n" + "=" * 60)
print("EXTRACCIÓN DE NÚMEROS")
print("=" * 60)

for mensaje in mensajes:
    numeros = re.findall(patron_numeros, mensaje)
    print(f"{mensaje} -> {numeros}")

# ==========================
# 3. BÚSQUEDA DE EMAILS
# ==========================

print("\n" + "=" * 60)
print("BÚSQUEDA DE EMAILS EN TEXTO")
print("=" * 60)

for texto in textos:
    encontrado = re.search(patron_email_busqueda, texto)

    if encontrado:
        print(f"{texto} -> Email encontrado: {encontrado.group()}")
    else:
        print(f"{texto} -> No se encontró email")

# ==========================
# 4. DETECCIÓN DE TARJETAS VISA
# ==========================

print("\n" + "=" * 60)
print("DETECCIÓN DE TARJETAS VISA")
print("=" * 60)

for transaccion in transacciones:
    match = re.search(patron_visa, transaccion)

    if match:
        print(f"{transaccion} -> Tarjeta detectada: {match.group()}")
    else:
        print(f"{transaccion} -> Sin tarjeta detectada")

# ==========================
# 5. VALIDACIÓN DE CÓDIGOS POSTALES
# ==========================

print("\n" + "=" * 60)
print("VALIDACIÓN DE CÓDIGOS POSTALES")
print("=" * 60)

for cp in codigos_postales:
    valido = re.fullmatch(patron_cp, cp)

    if valido:
        print(f"{cp} -> Código postal válido")
    else:
        print(f"{cp} -> Código postal inválido")

# ==========================
# RESUMEN FINAL
# ==========================

print("\n" + "=" * 60)
print("RESUMEN DE EXPRESIONES REGULARES USADAS")
print("=" * 60)

print(f"Validación email:         {patron_email_validacion}")
print(f"Eliminar no números:      {patron_no_numeros}")
print(f"Teléfono 10 dígitos:      {patron_telefono_10}")
print(f"Limpieza nombres:         {patron_nombre_limpio}")
print(f"Extracción números:       {patron_numeros}")
print(f"Búsqueda email:           {patron_email_busqueda}")
print(f"Detección Visa:           {patron_visa}")
print(f"Código postal México:     {patron_cp}")