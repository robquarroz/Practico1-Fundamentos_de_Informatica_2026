# ════════════════════════════════════════════════════════════
# EJERCICIO 1.2
# Conjunto A = (0,1) ∪ (2,3)  —  intervalos ABIERTOS.
# Se piden exactamente 7 valores; no hay condición de salida.
# ════════════════════════════════════════════════════════════


# ── LISTAS DE CLASIFICACIÓN ──────────────────────────────────
# Guardamos cada x en la lista que le corresponde para poder
# calcular los promedios separados al final.
en_A    = []  # valores que SÍ pertenecen a A
fuera_A = []  # valores que NO pertenecen a A


# ── BUCLE FOR: repite exactamente 7 veces ────────────────────
# range(1, 8) genera los números 1, 2, 3, 4, 5, 6, 7.
# La variable "i" lleva la cuenta de la vuelta actual
# y la usamos solo para mostrarle al usuario qué turno es.
for i in range(1, 8):


        # ── INGRESO Y CONVERSIÓN ────────────────────────────────
    # input() devuelve texto; float() lo convierte a número real.
    entrada = input(f"  Valor {i}/7  →  x = ") #el mensaje entre parentesis es lo que se muestra en pantalla
    x = float(entrada)   # "0.5" → 0.5  |  "3" → 3.0


        # ── VERIFICACIÓN DE PERTENENCIA ─────────────────────────
    # x ∈ A si cumple al menos UNA condición (unión ∪).
    # < estricto porque los extremos están excluidos.
    #en_A.append(x) me va mandando a la lista vacia los elementos
    if (0 < x < 1) or (2 < x < 3):
        print(f"  ✔ {x} ∈ A\n")
        en_A.append(x)     # agrega x al final de la lista en_A
    else:
        print(f"  ✘ {x} ∉ A\n")
        fuera_A.append(x)  # agrega x al final de la lista fuera_A


# ════════════════════════════════════════════════════════════
# RESULTADOS — se ejecutan una sola vez, al salir del for.
# ════════════════════════════════════════════════════════════
print("\n══════════════ RESUMEN ══════════════")
print(f"Valores ingresados  : 7")
print(f"Pertenecen a A      : {len(en_A)}")    # len() cuenta elementos de la lista
print(f"No pertenecen a A   : {len(fuera_A)}")


# ── PROMEDIO TOTAL ───────────────────────────────────────────
# Unimos ambas listas con + y dividimos entre 7 (siempre hay 7).
prom_total = sum(en_A + fuera_A) / 7
print(f"Promedio total      : {prom_total:.4f}")  # :.4f → 4 decimales


# ── PROMEDIO DE LOS QUE PERTENECEN A A ──────────────────────
# "if en_A:" es True solo si la lista tiene al menos un elemento.
# Evita dividir por cero si ningún valor cayó dentro de A.
# suma(A) me devuelve la suma del conjunto A
#len(en_A) me cuenta cuantos elementos tengo en en_A
if en_A:
    print(f"Promedio ∈ A        : {sum(en_A)/len(en_A):.4f}")
else:
    print("Promedio ∈ A        : sin datos")


# ── PROMEDIO DE LOS QUE NO PERTENECEN A A ───────────────────
# Misma lógica, pero para fuera_A.
if fuera_A:
    print(f"Promedio ∉ A        : {sum(fuera_A)/len(fuera_A):.4f}")
else:
    print("Promedio ∉ A        : sin datos")


print("═════════════════════════════════════")