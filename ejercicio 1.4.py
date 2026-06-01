# ════════════════════════════════════════════════════════════
# EJERCICIO 1.4
# Conjunto A = (0,4) ∪ {7}
#   • (0,4) es un intervalo ABIERTO → los extremos 0 y 4 no pertenecen.
#   • {7}   es un conjunto unitario → solo el número 7 exacto pertenece.
# ════════════════════════════════════════════════════════════


# ── PASO 1: PEDIR EL VALOR AL USUARIO ───────────────────────
# input() siempre devuelve texto; float() lo convierte a número real.
entrada = input("Ingrese un número real x: ")
x = float(entrada)   # "2.5" → 2.5  |  "7" → 7.0  |  "4" → 4.0


# ════════════════════════════════════════════════════════════
# PASO 2: ¿PERTENECE x A A?
# x ∈ A si cumple UNA de estas condiciones:
#   a) está en el intervalo abierto (0,4):  0 < x < 4
#   b) es exactamente el valor 7:           x == 7
# ════════════════════════════════════════════════════════════
pertenece = (0 < x < 4) or (x == 7)
# guarda True o False; lo usamos abajo para mostrar el mensaje


# ════════════════════════════════════════════════════════════
# PASO 3: ¿ES x PUNTO DE ACUMULACIÓN DE A?
#
# Un punto p es punto de acumulación si en CUALQUIER entorno
# (p-ε, p+ε), por pequeño que sea ε, siempre existe algún
# punto de A distinto de p.
#
# Para A = (0,4) ∪ {7} los puntos de acumulación son:
#   • Todo el intervalo CERRADO [0,4]: incluye los extremos
#     0 y 4 porque cualquier vecindad suya toca el interior (0,4).
#   • El 7 aislado NO es punto de acumulación: existe un entorno
#     (6.5, 7.5) que no contiene ningún otro punto de A.
#
# Conclusión: x es punto de acumulación ⟺  0 ≤ x ≤ 4
# ════════════════════════════════════════════════════════════
es_acumulacion = (0 <= x <= 4)
# <= incluye los extremos 0 y 4, que sí son puntos de acumulación


# ════════════════════════════════════════════════════════════
# PASO 4: MOSTRAR LOS RESULTADOS
# Imprimimos ambas respuestas con mensajes claros.
# ════════════════════════════════════════════════════════════
print("\n══════════════ RESULTADO ════════════")


# — Pertenencia ──────────────────────────────────────────────
if pertenece:
    print(f"  Pertenencia : ✔ {x} ∈ A")
else:
    print(f"  Pertenencia : ✘ {x} ∉ A")


# — Punto de acumulación ─────────────────────────────────────
if es_acumulacion:
    print(f"  Acumulación : ✔ {x} ES punto de acumulación de A")
else:
    print(f"  Acumulación : ✘ {x} NO es punto de acumulación de A")


print("═════════════════════════════════════")