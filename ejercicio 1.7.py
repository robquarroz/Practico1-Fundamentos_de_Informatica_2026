# ════════════════════════════════════════════════════════════
# EJERCICIO 1.7 — 

# ════════════════════════════════════════════════════════════


# ── PASO 1: PEDIR LOS EXTREMOS DEL INTERVALO ────────────────
print("── Definición del conjunto A = (a, b) ──\n")


datos_validos = False
a = 0
b = 0


while datos_validos == False:   # corre mientras datos_validos sea False


    error_conversion = False
    try:
        a = float(input("  Extremo inferior a: "))
        b = float(input("  Extremo superior b: "))
    except ValueError:
        error_conversion = True


    if error_conversion:
        print("  ⚠ Error: ingrese números reales válidos.\n")
    elif a >= b:
        print(f"  ⚠ Error: se requiere a < b. ({a} no es menor que {b})\n")
    else:
        datos_validos = True   # el while dejará de repetirse


print(f"\n  Conjunto definido: A = ({a}, {b})\n")


# ── PASO 2: PEDIR EL RANGO DE EVALUACIÓN ────────────────────
print("── Rango de evaluación (enteros) ──\n")


rango_valido = False
v_ini = 0
v_fin = 0


while rango_valido == False:   # corre mientras rango_valido sea False


    error_conversion = False
    try:
        v_ini_f = float(input("  Valor inicial (entero): "))
        v_fin_f = float(input("  Valor final  (entero): "))
    except ValueError:
        error_conversion = True


    if error_conversion:
        print("  ⚠ Error: ingrese números enteros válidos.\n")
    elif v_ini_f != int(v_ini_f) or v_fin_f != int(v_fin_f):
        print("  ⚠ Error: ambos valores deben ser enteros (sin decimales).\n")
    elif int(v_ini_f) > int(v_fin_f):
        print(f"  ⚠ Error: el valor inicial debe ser ≤ al final.\n")
    else:
        v_ini = int(v_ini_f)
        v_fin = int(v_fin_f)
        rango_valido = True   # el while dejará de repetirse


# ── PASO 3: EVALUAR CADA ENTERO DEL RANGO ───────────────────
pertenecen = []


print(f"\nEvaluando enteros del {v_ini} al {v_fin}:\n")


for x in range(v_ini, v_fin + 1):
    if a < x < b:
        print(f"  x = {x:4}  →  ✔ pertenece a A")
        pertenecen.append(x)
    else:
        print(f"  x = {x:4}  →  ✘ no pertenece a A")


# ── PASO 4: RESUMEN FINAL ────────────────────────────────────
print("\n══════════════ RESUMEN ══════════════")
print(f"Conjunto A              : ({a}, {b})")
print(f"Rango evaluado          : {v_ini} a {v_fin}")
print(f"Cantidad que pertenecen : {len(pertenecen)}")


if pertenecen:
    valores_str = ", ".join(str(v) for v in pertenecen)
    print(f"Pertenecen a A          : {{ {valores_str} }}")
else:
    print("Pertenecen a A          : ninguno")


print("═════════════════════════════════════")
