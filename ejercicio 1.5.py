# ════════════════════════════════════════════════════════════
# EJERCICIO 1.5
# Conjunto A = (0, 3)  —  intervalo ABIERTO.
# Los extremos 0 y 3 NO pertenecen al conjunto.
# El programa evalúa automáticamente los enteros de -1 a 4.
# No se le pide ningún valor al usuario.
# ════════════════════════════════════════════════════════════


# ── LISTA PARA ACUMULAR LOS VALORES QUE SÍ PERTENECEN ───────
# La iremos llenando dentro del bucle para mostrarla al final.
pertenecen = []   # empieza vacía


print("Evaluando valores del -1 al 4:\n")


# ── BUCLE FOR: recorre los enteros de -1 a 4 ─────────────────
# range(-1, 5) genera: -1, 0, 1, 2, 3, 4
# El segundo argumento es EXCLUSIVO, por eso se usa 5 y no 4
# para que el 4 quede incluido en la secuencia.
for x in range(-1, 5):


        # ── VERIFICACIÓN DE PERTENENCIA ─────────────────────────
    # x ∈ (0,3) si y solo si  0 < x < 3.
    # < estricto en ambos lados porque el intervalo es abierto.
    if 0 < x < 3:
        print(f"  x = {x:2}  →  ✔ pertenece a A")
        pertenecen.append(x)   # guarda el valor para el resumen final
    else:
        print(f"  x = {x:2}  →  ✘ no pertenece a A")
        # {x:2} alinea el número ocupando al menos 2 caracteres,
        # así la tabla queda visualmente ordenada


# ════════════════════════════════════════════════════════════
# RESUMEN FINAL
# Mostramos la lista de valores que sí pertenecen a A.
# ════════════════════════════════════════════════════════════
print("\n══════════════ RESUMEN ══════════════")
print(f"Valores evaluados       : -1, 0, 1, 2, 3, 4")
print(f"Cantidad que pertenecen : {len(pertenecen)}")


# Convertimos la lista a string con join() para mostrarla prolija.
# join() une los elementos separándolos con ", ".
valores_str = ", ".join(str(v) for v in pertenecen)
# str(v) convierte cada número a texto antes de unirlos
print(f"Pertenecen a A          : {{ {valores_str} }}")
print("═════════════════════════════════════")