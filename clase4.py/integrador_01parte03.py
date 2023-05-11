from data_stark import lista

def extraer_iniciales(lista:list,clave:str):
#imprime el nombre del heroe solo con sus iniciales
#recibe una lista y una calve
    iniciales = ""
    iniciales_lista = []
    for clave in lista:
        nombre_heroe = clave['nombre'].replace("-"," ").replace("the"," ").split()  #[nombre_1 , nombre_2]
        #nombre_0 = nombre_heroe[0].strip()
        for parte in nombre_heroe:
            parte.strip()
            inicial = parte[0].capitalize()
            iniciales  += inicial + "."
        iniciales_lista.append(iniciales)
        iniciales = ""
    print(iniciales_lista)
            

        # if(len(nombre_heroe)== 1):
        #     nombre_0 = nombre_heroe[0]
        #     nombre_0 = nombre_0[0:1].capitalize()
        #     inicial_nombre_1 = nombre_0
        #     print(inicial_nombre_1)
        #     lista_iniciales.append(nombre_0)

        # elif(len(nombre_heroe) > 1):
        #     inicial = nombre_heroe[0]
        #     inicial = inicial[0:1].capitalize()
        #     incial_2 = nombre_heroe[1]
        #     incial_2 = incial_2[0:1].capitalize()
        #     inicial_nombre_2 = f"{inicial}.{incial_2}"
        #     lista_iniciales.append(inicial_nombre_2)
        #     print(inicial_nombre_2)

    
    
    


        
#def definir_iniciales_nombre():


def definir_iniciales_nombre(lista:list,clave:str):
    lista_iniciales = extraer_iniciales(lista,"nombre")
    heroe = {}
    for letras in lista_iniciales:
        for heroe in lista:
            
            letras = heroe['iniciales']
    
    print(heroe['nombre'])
      #  print(heroe["iniciales"])
    
    

    

# iniciales = extraer_iniciales(lista,"nombre")
# for letras in iniciales:
#     print(letras)

extraer_iniciales(lista,"nombre")





