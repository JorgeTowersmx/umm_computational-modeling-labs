import re

RFC_REGEX = re.compile(r"^[A-Z&Ñ]{3,4}\d{6}[A-Z0-9]{3}$", re.IGNORECASE)
CP_REGEX = re.compile(r"^\d{5}$")

# Lista de usos de factura comunes del SAT. Agrega o modifica según tu catálogo.
USOS_FACTURA_VALIDOS = {
    "G01",  # Adquisición de mercancías
    "G02",  # Devoluciones, descuentos o bonificaciones
    "G03",  # Gastos en general
    "I01",  # Construcciones
    "I02",  # Mobiliario y equipo de oficina por inversiones
    "I03",  # Equipo de transporte
    "I04",  # Equipo de computo y accesorios
    "I05",  # Dados, troqueles, moldes, matrices y herramental
    "I06",  # Comunicaciones telefónicas
    "I07",  # Comunicaciones satelitales
    "I08",  # Otra maquinaria y equipo
    "P01",  # Por definir
}


def validar_rfc(rfc: str) -> bool:
    """Valida un RFC mexicano con formato simplificado."""
    if not isinstance(rfc, str):
        return False
    return bool(RFC_REGEX.fullmatch(rfc.strip()))


def validar_uso_factura(uso: str) -> bool:
    """Valida que el uso de la factura esté en el catálogo permitido."""
    if not isinstance(uso, str):
        return False
    return uso.strip().upper() in USOS_FACTURA_VALIDOS


def validar_cp(cp: str) -> bool:
    """Valida que el código postal tenga 5 dígitos."""
    if not isinstance(cp, str):
        return False
    return bool(CP_REGEX.fullmatch(cp.strip()))


def validar_formulario(data: dict) -> dict:
    """Valida los campos esperados de un formulario de ventas."""
    errores = {}

    rfc = data.get("RFC", "")
    uso = data.get("uso_factura", "")
    cp = data.get("CP", "")

    if not validar_rfc(rfc):
        errores["RFC"] = (
            "RFC inválido. Debe tener 3 o 4 letras seguidas de 6 dígitos de fecha "
            "y 3 caracteres de homoclave." 
        )

    if not validar_uso_factura(uso):
        errores["uso_factura"] = (
            "Uso de factura inválido. Debe ser uno de: "
            + ", ".join(sorted(USOS_FACTURA_VALIDOS))
        )

    if not validar_cp(cp):
        errores["CP"] = "Código postal inválido. Debe contener exactamente 5 dígitos."

    return errores


if __name__ == "__main__":
    ejemplo = {
        "RFC": "GODE561231GR8",
        "uso_factura": "G03",
        "CP": "64000",
    }

    errores = validar_formulario(ejemplo)

    if errores:
        print("El formulario contiene errores:")
        for campo, mensaje in errores.items():
            print(f"- {campo}: {mensaje}")
    else:
        print("El formulario es válido.")
