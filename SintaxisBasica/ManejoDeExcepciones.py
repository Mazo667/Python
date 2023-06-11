try:    #Intenta ejecutar el codigo
    miArchivo = open('/home/maximiliano/Documentos/texto.txt')

except FileNotFoundError:   #Haz esto para manejar determinado error
    print("Lo siento el archivo no existe")

else:   #Esto se ejecutara si el bloque try se ejecuta sin errores
    contenido = miArchivo.read()
    print(contenido)

finally:    #Este bloque se ejecutara siempre
    miArchivo.close()
