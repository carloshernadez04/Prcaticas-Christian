##-----TIPOS DE VARIABLES------##
#int = entero ej. 123
#strig o str = cadena de texto ej. "Hola Mundo" "123"
#booleano o bool = verdadero o falso ej. True o False
#float = numero decimal ej. 12.34
#decimal = numero decimal con mayor precision ej. 12.3456789

##------OPERADORES LOGICOS-----##
# = --> asignacion ej. name = "Christian"
# == --> comparacion de valores ej. 12 == 12
# === --> comparacion de valores y tipos de variable ej. "12" === 12
# > --> mayor que ej. 12 > 12
# < --> menor que ej. 10 < 12
# >= --> mayor o igual que ej. 12 >= 12
# <= --> menor o igual que ej. 10 <= 12
# != --> diferente que ej. 12 != 10
# and, && --> y ej. (edad_usuario >= 18) and (edad_usuario < 31) ==> c1(true) y c2(true) -> true
# or, || --> o ej. (status_user == 'fiebre +40') or (status_user == 'no se puede mover') ==> c1(falsa) , c2(true) -> true 

##-----CONDICIONALES------##
# if --> si ..... else --> sino  .... else if --> sino si
# while --> mientras 
# for --> para 
# switch/case --> 

#input --> entrada de datos


##== IF ELSE ELIF ==##
# name = "Christian"
# age = 16

# if age >= 18:
#     print('eres mayor de edad ', name)
# else:
#     print('aun no eres mayor de edad ', name)

# == WHILE ==##
# condition = True
# while condition:
#     print('Hola dentro del while')

## == FOR ==# #

# for i in range(6):
#     print('Hola en la vuelta ', i + 5)


## === SWCHIT CASO O MATCH CASE EN PY ===##
# age = 18
# match age:
#     case 15:
#         print ('15 años')
#     case 16:
#         print ('16 años')   
#     case 17:
#         print ('17 años')  
#     case 18:
#         print ('18 años')   

# == EJEMPLO TABLAS DE MULTIPLICAR ==##
# limit=10
# tabla_user=0
# print("bienvenido a la calculadora de tablas de multiplicar")
# tabla_user=int(input("ingresa la tabla que deseas saber inutil: "))
# for i in range(1,limit +1):
#     result=tabla_user *i
#     print(tabla_user ," x ",i, " = ",result)
number1=0
number2=0
print("division")
number1=int(input("ingrese un numero "))
number2=int(input("ingrese su segundo numero "))
contador=0
while number2==0:
    print("no se puede dividir")
    number2=int(input("ingrese un numero diferente a 0 "))
    contador=contador+1
    if contador==3:
        print("que no se puede")
        contador=0   

resultado=number1/number2
print(number1, " / ",number2," = ",resultado)

#cosa



