# encoding: UTF-8
# Blanca Flor Calderón Vázquez
#Tarea 8_Cadenas


def acumularDatos(listaDeNumerosEnteros):
    acumulador=0
    nuevaLista=list()
    for i in listaDeNumerosEnteros:
        c +=listaDeNumerosEnteros[i]
        nuevaLista.append(c)
    return nuevaLista
def removerPriemroYUltimo(lista):
    nuevaLista=list()
    for  i in lista:
        if i!=0 and i!=-1:
            numero=lista[i]
            nuevaLista.append(numero)
    return nuevaLista
def verificarOrden(lista):
    nuevaLista=list(lista)
    nuevaLista.sort()
    if nuevaLista==lista:
        return True
    else:
        return False
def comprobarAnagramas(listaA,listaB):
    c=0
    b=len(ListaA)
    for i in listaB:
        letra=listaB[i]
        while letra in ListaA==True:
            c +=1
    if c==b:
        return True
    else:
        return False
def verificarDuplicados(lista):
    for i in lista:
        dato=lista[i]
        duplicado=lista.count(dato)
        if duplicado>1:
            return True
    return False
def eliminarDuplicados(lista):
    for i in lista:
        dato=lista[i]
        duplicado=lista.count(dato)
        if duplicado>1:
            lista.remove(dato)
            lista.append(dato)
    return lista
def main():
listanumerica=int(input("ingresa tus numeros"))
listacadena=input("infresa tus letras")
listacadena1=input("infresa tus letras")
listaA=list(listanumerica)
lsitaB=list(listacadena)
lsitaC=list(listacadena1)
prueba1=acumularDatos(listaA)
prueba2=removerPriemroYUltimo(lsitaA)
prueba3=verificarOrden(listaA)
prueba4=comprobarAnagramas(lsitaB,listaC)
prueba5=verificarDuplicados(listaA)
prueba6=eliminarDuplicados(listaA)

print(prueba1,prueba2,prueba3,prueba4,prueba5,prueba6)
    


main()
   
        
        
        
