# voc=input("INGRESE SU VOCAL EN MAYUSCULA : ")

# if voc == "A":
#     print("SU VOCAL EN MINUSCULA ES : a ")
# elif voc == "E":
#     print("SU VOCAL EN MINUSCULA ES : e ")
# elif voc == "I":
#     print("SU VOCAL EN MINUSCULA ES : i ")
# elif voc == "O":
#     print("SU VOCAL EN MINUSCULA ES : o ")
# elif voc == "U":
#     print("SU VOCAL EN MINUSCULA ES : u ")
# else:
#     print("NO ES UNA VOCAL")

# voc=input("INGRESE SU VOCAL EN MAYUSCULA : ")

# if voc == "A" or voc == "E" or voc == "I" or voc == "O" or voc == "U":
#     li=["a","e","i","o","u"]
#     print("SU VOCAL ES: ")

#  TALLER DE IF,ELIF,ELSE   28/07/2025

#  1

# nm=int(input("INGRESE UN NUMERO: "))

# if nm >0:
#     print("SU NUMERO ES POSITIVO")
# elif nm == 0:
#     print("SU NUMERO ES CERO")
# elif nm<0 :
#     print("SU NUMERO ES NEGATIVO")
# else:
#     print("NO ES UN NUMERO")

#  2

# nm=int(input("INGRESE UN NUMERO: "))
# nm2=int(input("INGRESE UN NUMERO: "))

# if nm > nm2:
#     print("EL PRIMER NUMERO ES EL MAYOR DE LOS DOS")
# elif nm2 > nm :
#     print("EL SEGUNDO NUMERO ES EL MAYOR DE LOS DOS ")
# else:
#     print("SON NUMEROS IGUALES")

#  3

# nm=int(input("INGRESE UN NUMERO: "))

# if nm %2==0 :
#     print("SU NUMERO ES PAR")
# else:
#     print("SU NUMERO ES IMPAR")

#  4

# nm=int(input("INGRESE UN NUMERO: "))

# if nm>= 10 and nm<=20:
#     print("SU NUMERO ESTA ENTRE 10 A 20")
# else:
#     print("SU NUMERO NO ESTA ENTRE 10 A 20")

#  5

# nm=int(input("INGRESE UN NUMERO: "))
# nm2=int(input("INGRESE UN 2 NUMERO: "))
# nm3=int(input("INGRESE UN 3 NUMERO: "))

# if nm>nm2 and nm>nm3:
#     print("EL PRIMER NUMERO ES EL MAYOR")
# elif nm2>nm and nm2>nm3:
#     print("EL SEGUNDO NUMERO ES EL MAYOR")
# elif nm3>nm and nm3>nm2:
#     print("EL TERCER NUMERO ES EL MAYOR")
# else:
#     print("SON IGUALES")

#  6

# pr=float(input("INGRESE UN PRECIO: "))
 
# if pr >= 100:
#     prf=pr-10/100*pr
#     print(f"SU PRECIO FINAL CON UN 10% DE DESCUENTO ES: ",prf)
# else:
#     print("NO APLICA EL DESCUENTO")

#  7

# edd=int(input("INGRESE SU EDAD: "))

# if edd >= 18:
#     print("PUEDE VOTAR")
# else:
#     print("NO PUEDE VOTAR")

#  8

# pr=float(input("INGRESE UN PRECIO: "))
# vp=input("ERES VIP O NORMAL: ")

# if vp == "VIP":
#     prf=pr-20/100*pr
#     print(F"DADO QUE ERES VIP SE TE APLICA UN DESCUENTO DE 20%: {prf}")
# else:
#     print(F"DADO QUE NO ERES VIP NO SE TE APLICA UN DESCUENTO DE 20%")

#  9

# nm=int(input("INGRESE UN NUMERO: "))
# if nm %5 == 0 and nm %3 == 0:
#     print("EL NUMERO ES MULTIPLO DE 5 Y 3")
# else:
#     print("EL NUMERO NO ES MULTIPLO DE 5 Y 3")

#  10

# nm=int(input("INGRESE UN NUMERO: "))
# nm2=int(input("INGRESE EL NUMERO POR EL CUAL QUIERE SER DIVISIBLE: "))
# nm3=int(input("INGRESE EL  2NUMERO POR EL CUAL QUIERE SER DIVISIBLE: "))

# if nm %nm2==0 and nm %nm3==0:
#     print(F"SI ES DIVISIBLE ENTRE LOS DOS NUMEROS DADOS: {nm}")
# else:
#     print("EL NUMERO NO ES DIVISIBLE ENTRE LOS 2 NUMEROS DADOS")

#  11

# lst=[1,2,3,4,5]
# print(lst)

# if lst[2]>10:
#     print("EL TERCER NUMERO DE LA LISTA ES MAYOR DE 10")
# else:
#     print("EL TERCER NUMERO DE LA LISTA NO ES MAYOR DE 10")

#  12  MALO

# lst=[3,5,7,9]
# print(lst)
# fnd=lst.find(7)
# print(fnd)
# if fnd == 7:
#     print("EL NUMERO 7 SI ESTA EN LA LISTA")
# else:
#     print("EL NUMERO 7 NO ESTA EN LA LISTA")

#  13

# lst=[4,6,2,8]

# sum=lst[0]+lst[1]
# if sum >= 10:
#     print("SUMA ALTA")
# else:
#     print("SUMA BAJA")

#  14

# lst=["ANA","LUIS","PEDRO","MARTA"]
# print(lst)
# if lst[3] == "MARTA":
#     print("NOMBRE CORRECTO")
# else:
#     print("NOMBRE INCORRECTO")

#  15

# lst=["ROJO","AZUL","BLANCO"]
# print(lst)
# if lst[1]=="AZUL":
#     lst.remove(lst[1])
#     lst.insert(1,"NEGRO") 
#     print(lst)

#  16

# tp=(5,6,12,20)
# print(tp)
# if tp[0]>tp[3]:
#     ls=list(tp)
#     ls.sort()
#     print(f"ORDEN ASCENDENTE",ls)
# else:
#     print(f"ORDEN DESCENDENTE:",tp)

#  17

# tup=(25,32,28)
# print(tup)

# if tup[1]>30:
#     print("EDAD MAYOR A 30")
# else:
#     print("EDAD MENOR O IGUAL A 30")

#  18

# tup=(1,2,3)
# if tup[1]==2:
#     ls=list(tup)
#     ls.remove(2)
#     ls.insert(1,10)
#     tup2=tuple(ls)
#     print(tup2)
# else:
#     print("EL 2 NUMERO DE LA TUPLA NO ES 2")

#  19

# tp=(4,5)
# print(tp)
# if tp[1]>5:
#     print("C0ORDENADA ALTA")
# else:
#     print("COORDENADA BAJA")

#  20

tup=(3,4)
print(tup)
tup2=(3,4)
print(tup2)

if tup==tup2:
    print("TUPLAS IGUALES")
else:
    print("LAS TUPLAS NO SON IGUALES")




