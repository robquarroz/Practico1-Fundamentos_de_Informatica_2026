# EJERCICIO 1.1
# Conjunto A = (0,1) ∪ (2,3)
# Los paréntesis indican intervalos ABIERTOS: los extremos
# 0, 1, 2 y 3 NO pertenecen al conjunto.


# ── PASO 1: PEDIR EL VALOR AL USUARIO ───────────────────────
# input() siempre devuelve texto (string), por eso enseguida
# lo convertimos a número real con float().
entrada = input("Ingrese un número real x: ")
x = float(entrada)   # convierte "3.5" → 3.5  |  "0.7" → 0.7


# ── PASO 2: VERIFICAR PERTENENCIA ───────────────────────────
# x pertenece a A si cumple AL MENOS UNA de estas condiciones:
#   • está en (0,1):  0 < x < 1
#   • está en (2,3):  2 < x < 3
# El "or" representa la unión ∪ entre los dos intervalos.
# Usamos < (estricto) y no <= porque los extremos están excluidos.
pertenece = (0 < x < 1) or (2 < x < 3)
# la variable "pertenece" guarda True o False según el resultado


# ── PASO 3: MOSTRAR EL MENSAJE ──────────────────────────────
# Según el valor de "pertenece" imprimimos el mensaje correcto.
# Las f-strings (f"...") permiten insertar el valor de x
# directamente dentro del texto con {x}.
if pertenece:
    print(f"✔ {x} ∈ A  →  el valor SÍ pertenece al conjunto A.")
else:
    print(f"✘ {x} ∉ A  →  el valor NO pertenece al conjunto A.")