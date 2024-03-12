def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b
    
while True:
    print("Seleccione la operación")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar")

    if opcion == "5":
        print("Saliendo de la calculadora")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        print("El resultado de la suma es: " , suma(num1, num2))
    elif opcion == "2":
        print("El resultado de la resta es: ", resta(num1, num2))
    elif opcion == "3":
        print("El resultado de la multiplicación es: ", multiplicacion(num1, num2))
    elif opcion == "4":
        if num2 != 0:
            print("El resultado de la división es: ", division(num1, num2))
        else:
            print("Error, no se puede dividir por cero")
    else:
        print("Opción no valida")
