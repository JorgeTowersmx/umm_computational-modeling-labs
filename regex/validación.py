import re

texto = "64700"

print(re.search(r"\d{5}", texto))
print(re.fullmatch(r"\d{5}", texto))