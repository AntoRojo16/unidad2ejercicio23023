from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

    
if __name__=="__main__":
    #nViajero=ViajeroFrecuente(123,"44018004","antonela","rojo",340)
    #print("la cantidad de millas es {}".format(unViajero.cantidadYotaldeMillas()))
    #unViajero.canjearMillas(35)
    #print("la cantidad de millas es {}".format(unViajero.cantidadYotaldeMillas()))
    listaViajero=[]
    archivo=open("Viajeros.csv")
    reader= csv.reader(archivo,delimiter=",")
    bandera=True
    for fila in reader:
        if bandera:
            bandera=not bandera
    
        else:
            numero =fila[0]
            dni =fila[1]
            nom =fila[2]
            ape =fila[3]
            millas =int(fila[4])
            unViajero=ViajeroFrecuente(numero,dni,nom,ape,millas)
            listaViajero.append(unViajero)
    archivo.close()
    for i in range(len(listaViajero)):
        print(listaViajero[i])

    num=int(input("ingrese el numero de viajero >> "))
    i=0
    viajeroNuevo=listaViajero[0]
    numero=int(viajeroNuevo.getNumero())
    print(numero)
    #print(type(numero))
    #print(type(num))
    while ((i<(len(listaViajero)-1))and(num!=numero)):
        i+=1
        viajeroNuevo=listaViajero[i]
        numero=int(viajeroNuevo.getNumero())
        print(numero)
    
        
    print("mostrar cantidad de millas {}:".format(viajeroNuevo.cantidadYotaldeMillas()))

    
    print("Acumular millas")

    

    
    
    