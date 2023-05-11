#NAHUEL IAIR GALLARDO 1°B
#lista_heroes = [
#    {"ID" : 1 , "codename" : "Power Girl" , "identidad" : "Kara Zor-el" , "origen" : "Krypton", "Habilidades": "volar|Fuerza|Velocidad"},
#   {"ID" : 1 , "codename" : "Power Girl" , "identidad" : "Kara Zor-el" , "origen" : "Krypton", "Habilidades": "volar|Fuerza|Velocidad"},
#   {"ID" : 1 , "codename" : "Power Girl" , "identidad" : "Kara Zor-el" , "origen" : "Krypton", "Habilidades": "volar|Fuerza|Velocidad"}
#]

heroes_info = [
    {
        "Nombre":"Super Girl",
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    {
        "Nombre":"Shazam",
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson",
    },
    {
        "Nombre":"Power Girl",
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    {
        "Nombre":"Wonder Woman",
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
]


for heroe in heroes_info:

    Id = heroe["ID"]
    Codename = heroe["Nombre"]
    Identidad = heroe["Identidad"]
    origen = heroe["Origen"]
    set_habilidades = set(heroe["Habilidades"])
    

#\n es para que en la misma lionea de codigo pueda printear el texto un renglon abajo
    print(f"ID:{heroe['ID']}, Codename: {heroe['Nombre']} \nIdentidad: {heroe['Nombre']}, Origen {heroe['Origen']}\nHabilidades: {set_habilidades}\n--------------------------\n ")


