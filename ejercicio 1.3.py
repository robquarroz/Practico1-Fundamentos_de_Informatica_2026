# ════════════════════════════════════════════════════════════
# FUNCIÓN DE PERTENENCIA
# Recibe un número x y devuelve True si pertenece a A, False si no.
# Los paréntesis ( ) en (0,1) y (2,3) son ABIERTOS, por eso usamos
# < y no <=. Los extremos 0, 1, 2 y 3 quedan excluidos.
# ════════════════════════════════════════════════════════════
def pertenece_a_A(x): #defino la funcion pertenece para solamente hacerlo de una vez
    return (0 < x < 1) or (2 < x < 3)
    # "or" implementa la unión ∪: basta con que se cumpla UNA de las dos condiciones


# ════════════════════════════════════════════════════════════
# LISTAS DE CLASIFICACIÓN
# Guardaremos cada x en la lista que corresponda para poder
# calcular promedios separados al final.
# ════════════════════════════════════════════════════════════
en_A    = []  # acumula los x que SÍ pertenecen a A
fuera_A = []  # acumula los x que NO pertenecen a A


print("Ingrese valores de x (escriba -1 para terminar):\n")


# ════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL
# "while True" corre indefinidamente; solo se detiene cuando
# el usuario escribe -1, que activa el "break".
# ════════════════════════════════════════════════════════════
while True:


    entrada = input("  x = ")  # leemos lo que escribe el usuario (siempre llega como texto)


        # ── VALIDACIÓN: convertir texto → número real ────────────
    # Si el usuario escribe letras o caracteres inválidos,
    # float() lanza un error. El try/except lo atrapa sin
    # que el programa se caiga, y pide ingresar de nuevo.
    try:
        x = float(entrada)       # convierte "3.5" → 3.5, "abc" → error
    except ValueError:
        print("  ⚠ Valor inválido. Ingrese un número real.\n")
        continue               # vuelve al inicio del while sin ejecutar el resto


        # ── CONDICIÓN DE SALIDA ──────────────────────────────────
    # Si el usuario ingresó exactamente -1, terminamos el bucle.
    if x == -1:
        break                  # sale del while y pasa al bloque de resultados


        # ── CLASIFICACIÓN DEL VALOR ──────────────────────────────
    # Llamamos a nuestra función y según el resultado
    # mostramos un mensaje y guardamos x en la lista correcta.
    if pertenece_a_A(x):
        print(f"  ✔ {x} ∈ A\n")
        en_A.append(x)         # agrega x al final de la lista en_A
    else:
        print(f"  ✘ {x} ∉ A\n")
        fuera_A.append(x)     # agrega x al final de la lista fuera_A


# ════════════════════════════════════════════════════════════
# CÁLCULO Y MUESTRA DE RESULTADOS
# Se ejecuta una sola vez, después de que el bucle terminó.
# ════════════════════════════════════════════════════════════
total = len(en_A) + len(fuera_A)  # cantidad total de valores ingresados


print("\n══════════════ RESUMEN ══════════════")
print(f"Valores ingresados : {total}")
print(f"Pertenecen a A     : {len(en_A)}")
print(f"No pertenecen a A  : {len(fuera_A)}")


# ── PROMEDIO TOTAL ───────────────────────────────────────────
# Combinamos ambas listas con + para obtener todos los valores,
# y verificamos que haya al menos uno antes de dividir.
if total > 0:
    prom_total = sum(en_A + fuera_A) / total
    print(f"Promedio total     : {prom_total:.4f}")  # :.4f → 4 decimales


# ── PROMEDIO DE LOS QUE PERTENECEN A A ──────────────────────
# "if en_A:" es verdadero solo si la lista tiene al menos un elemento.
# Evita la división por cero si nadie ingresó un valor en A.
if en_A:
    print(f"Promedio ∈ A       : {sum(en_A)/len(en_A):.4f}")
else:
    print("Promedio ∈ A       : sin datos")


# ── PROMEDIO DE LOS QUE NO PERTENECEN A A ───────────────────
# Misma lógica que arriba pero para la lista fuera_A.
if fuera_A:
    print(f"Promedio ∉ A       : {sum(fuera_A)/len(fuera_A):.4f}")
else:
    print("Promedio ∉ A       : sin datos")


print("═════════════════════════════════════")