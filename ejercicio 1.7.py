# ════════════════════════════════════════════════════════════
# EJERCICIO 1.7
# Igual al 1.6 pero con validaciones estrictas:
#   • a y b deben ser números reales y cumplir a < b.
#     Si no, se vuelven a pedir desde cero.
#   • v_ini y v_fin deben ser enteros y cumplir v_ini <= v_fin.
#     Si no, se vuelven a pedir desde cero.
# ════════════════════════════════════════════════════════════


# ════════════════════════════════════════════════════════════
# PASO 1: PEDIR LOS EXTREMOS DEL INTERVALO CON VALIDACIÓN
#
# Usamos un bucle "while True" que solo termina con "break"
# cuando ambos valores son correctos.
# Si el usuario escribe texto en vez de un número, el
# try/except lo atrapa y vuelve a pedir sin caerse.
# ════════════════════════════════════════════════════════════
print("── Definición del conjunto A = (a, b) ──\n")


while True:
    try:
        a = float(input("  Extremo inferior a: "))
        b = float(input("  Extremo superior b: "))
    except ValueError:
                # float() lanzó error: el usuario escribió algo que no es número
        print("  ⚠ Error: ingrese números reales válidos.\n")
        continue   # vuelve al inicio del while sin ejecutar lo de abajo


        # ── VALIDACIÓN: a debe ser estrictamente menor que b ────
    # Si no se cumple, avisamos y repetimos el bucle completo
    # (el usuario debe reingresar AMBOS valores).
    if a >= b:
        print(f"  ⚠ Error: se requiere a < b. ({a} no es menor que {b})\n")
        continue   # vuelve a pedir a y b


    break   # todo correcto → salimos del bucle


print(f"\n  Conjunto definido: A = ({a}, {b})\n")


# ════════════════════════════════════════════════════════════
# PASO 2: PEDIR EL RANGO DE EVALUACIÓN CON VALIDACIÓN
#
# v_ini y v_fin deben ser enteros (sin parte decimal).
# Para verificarlo: convertimos a float, luego comprobamos
# que sea igual a su versión entera con int().
# También exigimos v_ini <= v_fin.
# ════════════════════════════════════════════════════════════
print("── Rango de evaluación (enteros) ──\n")


while True:
    try:
        v_ini_f = float(input("  Valor inicial (entero): "))
        v_fin_f = float(input("  Valor final  (entero): "))
    except ValueError:
        print("  ⚠ Error: ingrese números enteros válidos.\n")
        continue


        # ── VERIFICAR QUE SEAN ENTEROS ───────────────────────────
    # 3.0 == int(3.0) → True   ✔ aceptado
    # 3.5 == int(3.5) → False  ✘ rechazado
    if v_ini_f != int(v_ini_f) or v_fin_f != int(v_fin_f):
        print("  ⚠ Error: ambos valores deben ser enteros (sin decimales).\n")
        continue


    v_ini = int(v_ini_f)   # convertimos a int para usar en range()
    v_fin = int(v_fin_f)


        # ── VERIFICAR v_ini <= v_fin ─────────────────────────────
    if v_ini > v_fin:
        print(f"  ⚠ Error: el valor inicial debe ser ≤ al final. ({v_ini} > {v_fin})\n")
        continue


    break   # todo correcto → salimos del bucle


# ════════════════════════════════════════════════════════════
# PASO 3: EVALUAR CADA ENTERO DEL RANGO
# range(v_ini, v_fin + 1) incluye v_fin gracias al +1.
# ════════════════════════════════════════════════════════════
pertenecen = []   # acumulará los valores que sí pertenecen a A


print(f"\nEvaluando enteros del {v_ini} al {v_fin}:\n")


for x in range(v_ini, v_fin + 1):


        # x ∈ (a, b) si  a < x < b  (extremos excluidos)
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


if pertenecen:
    valores_str = ", ".join(str(v) for v in pertenecen)
    print(f"Pertenecen a A          : {{ {valores_str} }}")
else:
    print("Pertenecen a A          : ninguno")


print("═════════════════════════════════════")