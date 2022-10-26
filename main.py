from userFunctions import Map, Reduce
from documentReader import DocumentReader

texts = DocumentReader("beemovie.pdf")

list = Map(texts)
map = Reduce(list)
while True:
    key = input("Ingrese palabra a buscar en el script en inglés de Bee Movie\n$ ")
    print("Páginas en las que aparece la palabra:")
    try:
        print(map[key])
    except:
        print("La palabra {} no se encuentra en el script".format(key))
    continuar = input("Desea ingresar otra palabra? [y/n]\n$ ")
    if continuar.lower() != 'y':
        continuar = input("Desea ver el índice ordenado? [y/n]\n$ ")
        if continuar.lower() == 'y':
            sorted=sorted(map.keys(), key=lambda x:x.lower())
            for key in sorted:
                print("{0}: {1}".format(key,map[key]))
        else:
            break