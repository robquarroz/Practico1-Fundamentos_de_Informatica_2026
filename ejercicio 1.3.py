# ════════════════════════════════════════════════════════════
# EJERCICIO 1.3 —
# Conjunto A = (0,1) ∪ (2,3)
# El usuario ingresa valores hasta escribir -1.
# En vez de "while True + break", usamos una bandera llamada
# "seguir" que arranca en True y se pone en False cuando
# el usuario escribe -1, deteniendo el bucle.
# ════════════════════════════════════════════════════════════


# ── LISTAS DE CLASIFICACIÓN ──────────────────────────────────
en_A    = []  # valores que SÍ pertenecen a A
fuera_A = []  # valores que NO pertenecen a A


# ── BANDERA DE CONTROL ───────────────────────────────────────
# "seguir" arranca en True porque queremos que el bucle
# empiece a ejecutarse. Se pondrá en False solo cuando
# el usuario ingrese -1.
seguir = True


print("Ingrese valores de x (escriba -1 para terminar):\n")


# ── BUCLE PRINCIPAL ──────────────────────────────────────────
# El while corre mientras "seguir" sea True.
# Cuando el usuario escribe -1, seguir pasa a False
# y el while no vuelve a repetirse.
while seguir == True:


        # ── INGRESO Y VALIDACIÓN ────────────────────────────────
    # Si el usuario escribe texto, float() falla.
    # El try/except lo atrapa y usa error = True para
    # registrarlo sin caerse el programa.
    error = False
    try:
        x = float(input("  x = "))
    except ValueError:
        error = True


        # ── DECISIÓN SEGÚN EL VALOR INGRESADO ───────────────────
    # Tres casos posibles, evaluados en orden:
    #   1) hubo error de conversión → avisar
    #   2) el usuario escribió -1   → poner seguir en False
    #   3) es un número válido      → clasificar
    if error:
        print("  ⚠ Valor inválido. Ingrese un número real.\n")


    elif x == -1:
        seguir = False   # el while no volverá a repetirse


    elif (0 < x < 1) or (2 < x < 3):
        print(f"  ✔ {x} ∈ A\n")
        en_A.append(x)      # guarda el valor en la lista de pertenecientes


    else:
        print(f"  ✘ {x} ∉ A\n")
        fuera_A.append(x)   # guarda el valor en la lista de no pertenecientes


# ════════════════════════════════════════════════════════════
# RESULTADOS — se ejecutan una sola vez, al salir del while.
# ════════════════════════════════════════════════════════════
total = len(en_A) + len(fuera_A)


print("\n══════════════ RESUMEN ══════════════")
print(f"Valores ingresados : {total}")
print(f"Pertenecen a A     : {len(en_A)}")
print(f"No pertenecen a A  : {len(fuera_A)}")


# ── PROMEDIO TOTAL ───────────────────────────────────────────
# Verificamos que haya al menos un valor antes de dividir.
if total > 0:
    prom_total = sum(en_A + fuera_A) / total
    print(f"Promedio total     : {prom_total:.4f}")


# ── PROMEDIO DE LOS QUE PERTENECEN A A ──────────────────────
if en_A:
    print(f"Promedio ∈ A       : {sum(en_A)/len(en_A):.4f}")
else:
    print("Promedio ∈ A       : sin datos")


# ── PROMEDIO DE LOS QUE NO PERTENECEN A A ───────────────────
if fuera_A:
    print(f"Promedio ∉ A       : {sum(fuera_A)/len(fuera_A):.4f}")
else:
    print("Promedio ∉ A       : sin datos")


print("═════════════════════════════════════")