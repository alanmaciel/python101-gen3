# cuadrado = 1

# Checa si 'numero' es estrictamente menos de 10 en condición.
# while cuadrado <= 10:
#     print(cuadrado)    # Este codigo es ejecutado 10 veces
#     cuadrado += 1      # Este codigo es ejecutado 10 veces

cuadrado = 0
contador = 0

while contador < 100:
    cuadrado = contador ** 2
    print(str(contador) + " - " + str(cuadrado))
    contador += 1

print("Fin")           # Este codigo es ejecutado una vez