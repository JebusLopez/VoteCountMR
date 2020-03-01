import random
postulados = ['Enrique_Alfaro_Ramirez', 'Carlos_Lomeli_Bolaños', 'Miguel_Castro_Reynoso',
          'Miguel_Angel_Martinez Espinosa', 'Salvador_Cosio_Gaona', 'Martha_Rosa_Araiza_Soltero']
n = input("Numero de votos a generar:")
if n.isdigit():
    file = open(n + "_votos.txt","w+")
    for i in range(int(n)):
        file.write(''.join(random.choice(postulados)) + "\n")
    file.close
    print("El archivo ha sido generado")
else:
    print("este no es un numero")
