import re

##SPLIT

#print(re.split(" ","hola mundo 1c"))


#print(re.split("[a-z ]+","hola mundo 1251c"))
#print(re.split("[0-9]+","hola mundo 1251c"))
#print(re.split("[a-z]|[0-9| ]","hola mundo @@@ 1253 chau "))

##SEARCH
# print(re.search("como","hola como estan?").span())#donde empieza y termina
# print(re.search("como","hola como estan?").start())#donde empieza
# print(re.search("como","hola como estan?").end())#donde termina la coincidencia
# print(re.search("[0-9]+","texto con numeros: 123 y letras: aaa"))#numeros de l cero al nueve donde alla una o mas ocurrencias una al lado de la otra
# print(re.search("[0-9]","texto con numeros: 123 y letras: aaa")) #sin el + solo hace match con la primer ocurrencia
# print(re.search("[0-9]","texto con numeros: 123 y letras: aaa").group())

# texto = "texto con numeros: 123 y letras: aaa"

# span = re.search("[0-9]",texto).span()

# print(span)
# print(texto[span[0]:span[1]])

##FINDALL

# texto = "uno 1 dos 2 tres 3 Cuatro 44 239"
# print(re.findall(" ",texto))
# print(re.findall("[0-9]+",texto))
# print(re.findall("[0-9]",texto))

# print(re.findall("[a-z]+",texto))
# print(re.findall("[a-z]",texto))
# print(re.findall("[a-zA-Z]",texto))#INCLUYE MAYUSCULAS
# print(re.findall("[a-zA-Z]{3,6}",texto))#LOS NUMEROS ENTRE LLAVES SON EL MINJIMO Y EL MAXIMO DE CARARCTERES QUE TIENE QUE TENER 


##SUB : "reemplaza una cosa con otra"


# texto = "abc abc ccc ddd     abc aaa"
# result = re.sub("abc","xyz",texto)
# print(result)

# result = re.sub(r'\s+'," ",texto)
# print(texto)
# print(result)

# texto = 'QUEVEDO || BZRP Music Sessions #52'

# #print(re.split(" || ",texto))

# print(re.split("[\|#]+",texto))

fecha = "2022-02-03 19:20:33"

print(re.split("[0-9]{2}:[0-9]{2}:[0-9]{2}",fecha))
print(re.findall("[0-9]{4}",fecha))
print(re.findall("-[0-9]{2}-",fecha))
print(re.findall("-[0-9]{2}-",fecha))

año = "[0-9]{2,4}"
mes = "[0-9]{1,2}"
dia = "[0-9]{1,2}"

print(re.findall(f"{año}-{mes}-{dia}", fecha))