#Calcular el mayor de dos números ingresados por teclado usando un operador
#ternario

while True:
    try:
        numero_uno = int(input("Ingresa el primer número: "))

        numero_dos = int(input("Ingresa el segundo número: "))
    except ValueError:
        print("Intente nuevamente. Uno de los números es incorrecto. Solo se admiten números")
    else:
        if numero_uno == numero_dos:
            print(f"Los números son iguales")
        else:
            resultado =(f"El primer número ({numero_uno}) es mayor que el segundo ({numero_dos})" if numero_uno > numero_dos else f"El segundo número ({numero_dos}) es mayor que el primero ({numero_uno})")
            print(resultado)
        break



#Buscar una palabra en una lista ingresada por teclado usando args y un operador
#ternario

def buscar_lista(*palabras):
    
    palabra_a_encontrar = input("¿Qué palabra quiere encontrar?: ")
    buscando_la_palabra = any(elemento == palabra_a_encontrar for elemento in palabras)
    
    print(f"La palabra {palabra_a_encontrar} fue encontrada" if buscando_la_palabra else "No se encontró la palabra")
    

buscar_lista(3, "Maria","Stray Kids",8, 23, True)


#Determinar si un número es par o impar

def par_impar(*num):
    
    for i in num:
        try:
            print(f"El número {i} es par" if i % 2 == 0 else f"El número {i} es impar")
            
        except TypeError:
            print(f"'{i}' no es un número")
    
    #otra manera de resolver en vez del try-except
    for i in num:
        if isinstance(i, int) or isinstance(i, float):
            print(f"El número {i} es par" if i % 2 == 0 else f"El número {i} es impar")
        else:
            print(f"'{i}' no es un número")

par_impar(8,2,3,6,11,15,"hola")


#Calcular el promedio de una lista de números usando args y un operador ternario

def calcular_promedio(*notas):
    
    if len(notas) == 0:
        print("No se puede calcular el promedio porque no hay notas")
        return
    
    suma_total = sum(notas)
    
    promedio = suma_total/ len(notas)
    
    print(f"El alumno se encuentra aprobado. Su nota es de {promedio}" if promedio >= 4 else f"El alumno se encuentra desaprobado. Su nota es de {promedio}")
    

calcular_promedio(5,3,4,1,6)


#Imprimir un mensaje de error si no se pasan suficientes argumentos

def numero_maximo_minimo(*numeros):
    
    if len(numeros) == 0:
        print("No se puede encontrar el número máximo. La lista está vacía.")
        return
    
    maximo = max(numeros)
    minimo = min(numeros)
    
    print(f"El número máximo es: {maximo} y el número mínimo es: {minimo}")

numero_maximo_minimo(2,30,99,5,15,23)