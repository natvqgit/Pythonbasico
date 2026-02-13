#Loops

mi_lista = [1, 2, 3, 4, 5]

for i in mi_lista:
    print("Mi numero es:", i)

resultado = 0
for i in mi_lista:
    resultado += i 

print(f"El resultado de la suma es:, {resultado}")

for i in range (2, 9):
    print(i)

mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for i in mi_lista_2:
    if i != "lunes":
        print(f"feliz", (i))

#While loop
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i) 
    if i ==4:
        break

else:
    print("i es ahora mayor o igual a 5")

# Practica 2 
# Dada la lista mi_lista_2 = ["lunes, martes, miercoles, jueves, viernes"]
# Imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas 
# Pista: Usalo los dos tipos loop while y for en el mismo programa para lograrlo
# Resultado: 
# martes
# miercoles
#jueves 
#viernes
#martes
#miercoles
#jueves 
#viernes
#martes
#miercoles
#jueves 
#viernes

# Practica 2
mi_lista_2 = ["lunes, martes, miercoles, jueves, viernes"]
contador = 0
while contador < 3:
    for dias in mi_lista_2:   
        palabra = ""              
        
        for letra in dias:    
            if letra != "," and letra != " ":
                palabra += letra
            else:
                if palabra != "" and palabra != "lunes":
                    print(palabra)
                palabra = ""
        
        if palabra != "" and palabra != "lunes":
            print(palabra)
    
    contador += 1
