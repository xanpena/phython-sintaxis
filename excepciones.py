def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def producto(num1, num2):
    return num1*num2

def division(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Error"

while True:
    try:
        op1=(int(input("Introduce el primer número: ")))
        op2=(int(input("Introduce el segundo número: ")))

        try:    
            operacion=input("Introduce la operación a realizar (suma, resta, producto, division): ")
        except NameError:
            print("Operación no permitida")

    except ValueError:
        print("Valor no permitido")
        

if operacion=="suma":
    print(suma(op1, op2))

elif operacion=="resta":
    print(resta(op1, op2))

elif operacion=="producto":
    print(producto(op1, op2))

elif operacion=="division":
    print(division(op1, op2))

else:
    print("Operación no contemplada")