#Código no hecho por mi
import re

password = input("Ingresa tu contraseña: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[!@#$%^&*()_+=\-]", password)):
    print("✅ Contraseña fuerte.")
else:
    print("❌ Contraseña débil.")