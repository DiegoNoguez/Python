import secrets
import string

# Genera una clave de 256 bits (32 bytes) en hexadecimal
jwt_secret = secrets.token_hex(32)
print(jwt_secret)

# Alternativa: combinación de letras, dígitos y símbolos (más robusto)
alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?/"
jwt_secret2 = ''.join(secrets.choice(alphabet) for _ in range(64))
print(jwt_secret2)