hola_mundo = "Hola, Mundo!"

# for ch in hola_mundo:   
#   print(ch)

longitud = 0      # inicializa la variable longitud

# cuenta cuantos caracteres son en hola_mundo usando un ciclo
for ch in hola_mundo:
  longitud += 1  # suma 1 a longitud cada iteracion

print(longitud)
print(len(hola_mundo) == longitud)