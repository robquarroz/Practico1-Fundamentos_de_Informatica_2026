# ════════════════════════════════════════════════════════════
# EJERCICIO 1.6
# El conjunto A = (a, b) se construye con los extremos que
# ingresa el usuario. Luego se evalúan los enteros dentro
# de un rango también definido por el usuario.
# ════════════════════════════════════════════════════════════


# ── PASO 1: DEFINIR EL INTERVALO A = (a, b) ─────────────────
# El usuario ingresa los extremos; los convertimos a float
# para admitir valores decimales como 1.5 o -3.7.
print("── Definición del conjunto A = (a, b) ──\n")
a = float(input("  Extremo inferior a: "))
b = float(input("  Extremo superior b: "))


# ── VALIDACIÓN: a debe ser menor que b ──────────────────────
# Si el usuario los ingresó al revés, los intercambiamos
# automáticamente en lugar de dar error.
if a > b:
    a, b = b, a   # intercambio simultáneo: Python permite esto en una línea
    print(f"  (Se intercambiaron los extremos: a={a}, b={b})\n")


print(f"\n  Conjunto definido: A = ({a}, {b})\n")


# ── PASO 2: DEFINIR EL RANGO DE EVALUACIÓN ──────────────────
# El usuario elige desde qué entero hasta qué entero evaluar.
# int() convierte a número entero porque range() lo requiere.
print("── Rango de evaluación ──\n")
v_ini = int(float(input("  Valor inicial: ")))
v_fin = int(float(input("  Valor final  : ")))
# float() primero por si escribe "2.0"; int() lo redondea a 2


# ── VALIDACIÓN: v_ini debe ser menor que v_fin ───────────────
if v_ini > v_fin:
    v_ini, v_fin = v_fin, v_ini   # mismo truco de intercambio
    print(f"  (Se intercambiaron: inicio={v_ini}, fin={v_fin})\n")


# ── PASO 3: EVALUAR CADA ENTERO DEL RANGO ───────────────────
# range(v_ini, v_fin + 1) incluye v_fin gracias al +1,
# ya que el límite superior de range() es siempre exclusivo.
pertenecen = []   # acumulará los valores que sí pertenecen a A


print(f"\nEvaluando enteros del {v_ini} al {v_fin}:\n")


for x in range(v_ini, v_fin + 1):


        # ── VERIFICACIÓN DE PERTENENCIA ─────────────────────────
    # x ∈ (a, b) si  a < x < b.
    # Los extremos a y b quedan excluidos (intervalo abierto).
    if a < x < b:
        print(f"  x = {x:4}  →  ✔ pertenece a A")
        pertenecen.append(x)
    else:
        print(f"  x = {x:4}  →  ✘ no pertenece a A")


# ════════════════════════════════════════════════════════════
# PASO 4: RESUMEN FINAL
# ════════════════════════════════════════════════════════════
print("\n══════════════ RESUMEN ══════════════")
print(f"Conjunto A              : ({a}, {b})")
print(f"Rango evaluado          : {v_ini} a {v_fin}")
print(f"Cantidad que pertenecen : {len(pertenecen)}")


# join() une los elementos de la lista como texto separado por ", "
# Si la lista está vacía mostramos un mensaje alternativo.
if pertenecen:
    valores_str = ", ".join(str(v) for v in pertenecen)
    print(f"Pertenecen a A          : {{ {valores_str} }}")
else:
    print("Pertenecen a A          : ninguno")


print("═════════════════════════════════════")