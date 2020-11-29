abecedario = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z')
numeros = ('0','1','2','3','4','5','6','7','8','9')

def convertir(lista, letra, n):
    indice = lista.index(letra.lower()) + n
    if indice >= len(lista):
        indice -= len(lista)
    return indice
    

def criptografia(texto, n):
    nuevo_texto = ''
    for letra in texto:
        if letra.lower() not in abecedario and letra not in numeros:
            nuevo_texto += letra
            
        elif letra.lower() in abecedario:
            nuevo_texto += abecedario[convertir(abecedario,letra,n)] if letra.islower() else abecedario[convertir(abecedario,letra,n)].upper()
        else:
            nuevo_texto += numeros[convertir(numeros, letra,n)]

    return nuevo_texto


print (criptografia('Hola, me llamo Nour y tengo 39 años', 3))
print (criptografia('Krñd, oh ññdor Prxu b whpjr 62 dqrv', -3))