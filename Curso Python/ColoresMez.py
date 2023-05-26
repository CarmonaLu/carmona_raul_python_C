print("Este programa mezcla dos colores.")
#imprime dos opciones 
print("  r. Rojo      a. Azul")
primera = input("  Elija un color (r o a): ")
#si se elige r muestra el siguiente print
if primera == "r":
    print("  a. Azul      v. Verde")
    segunda = input("  Elija otro color (a o v): ")
    if segunda == "a":
        print("La mezcla de Rojo y Azul produce Magenta.")
    else:
        print("La mezcla Rojo y Verde produce Amarillo.")
#si se elige a antes del anterior if hace este ciclo        
else:
    print("  v. Verde    r. Rojo")
    segunda = input("  Elija otro color (v o r): ")
    if segunda == "v":
        print("La mezcla Azul y Verde produce Cian.")
    else:
        print("La mezcla Azul y Rojo produce Magenta.")
print("Hasta la proxima")