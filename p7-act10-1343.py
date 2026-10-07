# Daniel Nieves NC=1343

# ==========================================
# 1. PYTHON CONDITIONS (2 EJEMPLOS)
# ==========================================

# Ejemplo 1: Comparación simple para verificar si un número es positivo
numero = 10
if numero > 0:
    print("El número es positivo.")

# Ejemplo 2: Verificación de mayoría de edad
edad = 18
if edad >= 18:
    print("Acceso permitido: Es mayor de edad.")


# ==========================================
# 2. PYTHON IF...ELIF (2 EJEMPLOS)
# ==========================================

# Ejemplo 1: Clasificación de rangos de notas académicas
nota = 85
if nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")

# Ejemplo 2: Determinación de la etapa de vida según la edad
edad_persona = 15
if edad_persona < 12:
    print("Es un(a) niño(a).")
elif edad_persona < 18:
    print("Es un(a) adolescente.")


# ==========================================
# 3. PYTHON IF...ELSE (2 EJEMPLOS)
# ==========================================

# Ejemplo 1: Comprobar si un número es par o impar
numero_evaluar = 7
if numero_evaluar % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Ejemplo 2: Validar inicio de sesión
usuario_correcto = "admin"
usuario_ingresado = "invitado"

if usuario_ingresado == usuario_correcto:
    print("Bienvenido al sistema.")
else:
    print("Usuario incorrecto. Acceso denegado.")


# ==========================================
# 4. PYTHON FOR LOOPS (2 EJEMPLOS)
# ==========================================

# Ejemplo 1: Recorrer e imprimir los elementos de una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Ejemplo 2: Iterar en un rango de números (1 al 5) y calcular su cuadrado
for i in range(1, 6):
    print(f"El cuadrado de {i} es {i ** 2}")


# ==========================================
# 5. PYTHON WHILE LOOPS (2 EJEMPLOS)
# ==========================================

# Ejemplo 1: Contador regresivo simple
contador = 5
while contador > 0:
    print(f"Cuenta regresiva: {contador}")
    contador -= 1
print("¡Despegue!")

# Ejemplo 2: Suma acumulativa de números hasta alcanzar un límite
suma = 0
numero_actual = 1
while suma < 15:
    suma += numero_actual
    print(f"Sumando {numero_actual}, total acumulado: {suma}")
    numero_actual += 1

print("Daniel Nieves NC=1343")