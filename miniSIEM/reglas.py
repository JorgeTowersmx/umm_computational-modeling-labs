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