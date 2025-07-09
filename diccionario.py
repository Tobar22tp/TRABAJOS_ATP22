# auto= {
# "marca" : "ford",
# "modelo" : "mustang",
# "año" : 2022

# print(auto["modelo"])

# auto["año"]=2023
# print(auto)

# del auto["modelo"]
# print(auto)

#---------------------------TALLER1------------------------------
# l1=[]
# c1=float(input("PON TU NOTA NUMERO 1: "))
# c2=float(input("PON TU NOTA NUMERO 2: "))
# c3=float(input("PON TU NOTA NUMERO 3: "))

# tn=3
# suma=c1+c2+c3
# prom=suma/tn

# l1.append(c1)
# l1.append(c2)
# l1.append(c3)

# print(f"LA SUMA TOTAL DE LAS NOTAS FUE: {suma}, Y EL PROMEDIO DE NOTAS ES: {prom}")

#---------------------------TALLER2------------------------------

# frutas={"uvas": 2000,
#         "pera": 1000,
#         "manzana": 3000
# }
# print(frutas)
# p=float(input("AUMENTO EN (%): "))
# frutas["uvas"]+=frutas["uvas"]*(p/100)
# frutas["pera"]+=frutas["pera"]*(p/100)
# frutas["manzana"]+=frutas["manzana"]*(p/100)

# print(frutas)

#---------------------------TALLER3------------------------------

# t1=float(input("INGRESE TEMPERATURA NUMERO 1 EN CELCIUS: "))
# t2=float(input("INGRESE TEMPERATURA NUMERO 2 EN CELCIUS: "))
# t3=float(input("INGRESE TEMPERATURA NUMERO 3 EN CELCIUS: "))
# t4=float(input("INGRESE TEMPERATURA NUMERO 4 EN CELCIUS: "))
# t5=float(input("INGRESE TEMPERATURA NUMERO 5 EN CELCIUS: "))

# cel=(t1,t2,t3,t4,t5)

# f1=t1*9/5+32
# f2=t2*9/5+32
# f3=t3*9/5+32
# f4=t4*9/5+32
# f5=t5*9/5+32

# fah=(f1,f2,f3,f4,f5)

# print("TEMPERATURAS EN CELSIUS: ",cel)
# print("TEMPERATURAS EN FAHRENHEINT: ",fah)

#---------------------------TALLER4------------------------------

# l=[]
# ed=int(input("INGRESA LA EDAD NUMERO 1: "))
# ed2=int(input("INGRESA LA EDAD NUMERO 2: "))
# ed3=int(input("INGRESA LA EDAD NUMERO 3: "))
# ed4=int(input("INGRESA LA EDAD NUMERO 4: "))
# ed5=int(input("INGRESA LA EDAD NUMERO 5: "))

# l.append(ed)
# l.append(ed2)
# l.append(ed3)
# l.append(ed4)
# l.append(ed5)

# te=5
# suma=ed+ed2+ed3+ed4+ed5
# prom=te/suma
# max=max(l)
# min=min(l)
# print(F"LA SUMA DE LAS EDADES ES: {suma}, Y EL PROMEDIO ES: {prom}, LA EDAD MAX ES: {max} Y LA MIN ES: {min}")

#---------------------------TALLER5------------------------------

# frutas1={
#     "piña": 2000,
#     "pitaya": 4000,
#     "uva": 3000
# }
# pedido=int(input("CUANTOS KILOS QUIERES DE LA PIÑA: "))
# pedido2=int(input("CUANTOS KILOS QUIERES DE LA PITAYA: "))
# pedido3=int(input("CUANTOS KILOS QUIERES DE LA UVA: "))

# xk=[(frutas1["piña"]*(pedido))+(frutas1["pitaya"]*(pedido2))+(frutas1["uva"]*(pedido3))]
# print(f"EL TOTAL DE PRECIO POR KILO DE ESTA LISTA: {frutas1}, ES: {xk}")

#---------------------------TALLER6------------------------------

# lista=[]
# n1=int(input("INGRESE EL NUMERO 1: "))
# n2=int(input("INGRESE EL NUMERO 2: "))
# n3=int(input("INGRESE EL NUMERO 3: "))
# n4=int(input("INGRESE EL NUMERO 4: "))
# n5=int(input("INGRESE EL NUMERO 5: "))

# lista.append(n1)
# lista.append(n2)
# lista.append(n3)
# lista.append(n4)
# lista.append(n5)

# tupla=tuple(lista)
# suma=lista[0]+lista[1]+lista[2]+lista[3]+lista[4]
# print(f"LA SUMA ENTRE LOS NUMEROS AGREGADOS ALA TUPLA ES: {suma}")

#---------------------------TALLER7------------------------------

# l2=[]
# diccionario= {
# input("INGRESE NOMBRE DE LA 1 FRUTA: "),
# int(input("INGRESE LA CANTIDAD DE KILOS DE LA FRUTA 1: ")),
# int(input("INGRESE EL PRECIO DE LA FRUTA 1: ")),
# }
# diccionario2={
# input("INGRESE NOMBRE DE LA 2 FRUTA: "),
# int(input("INGRESE LA CANTIDAD DE KILOS DE LA FRUTA 2: ")),
# int(input("INGRESE EL PRECIO DE LA FRUTA 2: ")),
# }
# diccionario3={
# input("INGRESE NOMBRE DE LA 3 FRUTA: "),
# int(input("INGRESE LA CANTIDAD DE KILOS DE LA FRUTA 3: ")),
# int(input("INGRESE EL PRECIO DE LA FRUTA 3: ")),
# }

# l2.append(diccionario)
# l2.append(diccionario2)
# l2.append(diccionario3)

#---------------------------TALLER8------------------------------

# lista=[5000,2000,1000,4000,3000]
# print(lista)
# p=float(input("INGRESE EL NUMERO DE % QUIERE QUE SE LE REDUSCA ALOS PRECIOS: "))
# lista[0]-=lista[0]*(p/100)
# lista[1]-=lista[1]*(p/100)
# lista[2]-=lista[2]*(p/100)
# lista[3]-=lista[3]*(p/100)
# lista[4]-=lista[4]*(p/100)

# print(f"LOS PRECIOS DE LALISTA CON EL % REDUCIDO QUEDARIA ASI: ",lista)

#---------------------------TALLER9------------------------------

# tupla=()
# l2=list(tupla)

# n1=float(input("INGRESE LA NOTA NUMERO 1: "))
# n2=float(input("INGRESE LA NOTA NUMERO 2: "))
# n3=float(input("INGRESE LA NOTA NUMERO 3: "))
# n4=float(input("INGRESE LA NOTA NUMERO 4: "))

# l2.append(n1)
# l2.append(n2)
# l2.append(n3)
# l2.append(n4)
# tupla2=tuple(l2)

# max=max(tupla2)
# min=min(tupla2)

# print(F"SU NOTA MAS ALTA FUE: {max}, Y SU NOTA MAS BAJA FUE: {min}")

#---------------------------TALLER11------------------------------

# l3=[]

# pr1=int(input("INGRESE EL PRECIO NUMERO 1: "))
# pr2=int(input("INGRESE EL PRECIO NUMERO 2: "))
# pr3=int(input("INGRESE EL PRECIO NUMERO 3: "))

# l3.append(pr1)
# l3.append(pr2)
# l3.append(pr3)

# print(l3)

# l3[0]-=l3[0]*(19/100)
# l3[1]-=l3[1]*(19/100)
# l3[2]-=l3[2]*(19/100)

# print(F"LOS PRECIOS DIGITADOS MENOS EL 19% DEL IVA QUEDARIAN ASI: ",l3)

#---------------------------TALLER12------------------------------

# lis=[]
# n1=int(input("INGRESE UN NUMERO: "))
# n2=int(input("INGRESE OTRO NUMERO: "))

# suma=n1+n2
# resta=n1-n2
# multiplicacion=n1*n2
# division=n1=n2

# lis.append(suma)
# lis.append(resta)
# lis.append(multiplicacion)
# lis.append(division)

# tupla=tuple(lis)
# print(f"LA SUMA DE ESTOS NUMEROS ES: ",tupla[0])
# print(f"LA RESTA DE ESTOS NUMEROS ES: ",tupla[1])
# print(f"LA MULTIPLICACION DE ESTOS NUMEROS ES: ",tupla[2])
# print(f"LA DIVISION DE ESTOS NUMEROS ES: ",tupla[3])

#---------------------------TALLER14------------------------------

# l1=[]

# s1=int(input("INGRESE EL SALARIO DEL TRABAJADOR 1: "))
# s2=int(input("INGRESE EL SALARIO DEL TRABAJADOR 2: "))
# s3=int(input("INGRESE EL SALARIO DEL TRABAJADOR 3: "))
# s4=int(input("INGRESE EL SALARIO DEL TRABAJADOR 4: "))

# l1.append(s1)
# l1.append(s2)
# l1.append(s3)
# l1.append(s4)

# print(F"LOS SALARIOS DE TODOS SERIAN: ",l1)

# l1[0]+=l1[0]*(10/100)
# l1[1]+=l1[1]*(10/100)
# l1[2]+=l1[2]*(10/100)
# l1[3]+=l1[3]*(10/100)

# print(f"CON EL AUMENTO DEL 10% SUS SALARIOS QUEDARIAN ASI: ",l1)

#---------------------------TALLER15------------------------------

# dim={
# "MARACA": 3000,
# "BALON": 5000,
# "MUÑECO" : 4000
# }

# print(dim)

# imp=float(input("DIGITE EL % DE IMPUESTO QUE DESEA APLICAR ALOS PRODUCTOS ANTERIORES: "))

# dim["MARACA"]+=dim["MARACA"]*(imp/100)
# dim["BALON"]+=dim["BALON"]*(imp/100)
# dim["MUÑECO"]+=dim["MUÑECO"]*(imp/100)

# print(F"SEGUN EL % DE IMPUESTO APLICADO LOS PRECIOS QUEDARIAN ASI: ",dim)

#---------------------------TALLER16------------------------------

# edd=[]
# e1=int(input("INGRESE LA EDAD NUMERO 1: "))
# e2=int(input("INGRESE LA EDAD NUMERO 2: "))
# e3=int(input("INGRESE LA EDAD NUMERO 3: "))
# e4=int(input("INGRESE LA EDAD NUMERO 4: "))

# edd.append(e1)
# edd.append(e2)
# edd.append(e3)
# edd.append(e4)

# if edd[0] >= 18: 
#     print(f"ES MAYOR DE EDAD:",edd[0])
# else:
#     print(F"ES MENOR DE EDAD:",edd[0])   

# if edd[1] >= 18: 
#     print(f"ES MAYOR DE EDAD:",edd[1])
# else:
#     print(F"ES MENOR DE EDAD:",edd[1])   

# if edd[2] >= 18: 
#     print(f"ES MAYOR DE EDAD:",edd[2])
# else:
#     print(F"ES MENOR DE EDAD:",edd[2])   

# if edd[3] >= 18: 
#     print(f"ES MAYOR DE EDAD:",edd[3])
# else:
#     print(F"ES MENOR DE EDAD:",edd[3])   

#---------------------------TALLER17------------------------------

# dol=[]

# pla=int(input("INGRESE ALGUN NUMERO DE DOLARES: "))

# dol.append(pla)
# print(dol)

# tupla=tuple(dol)

# euro= 0.91
# peso= 4100
# yen= 160

# c1= pla*euro
# c2= pla*peso
# c3= pla*yen

# print(f"LA CONVERSION DE EL NUMERO DIGITADO EN EUROS ES: {c1}, EN PESOS: {c2} Y EN YEN: {c3}" )

#---------------------------TALLER13------------------------------

# dicc={
# "ANDRES" : 4.0,
# "FELIPE" : 3.5,
# "JOSUE" : 2.0
# }

# print(f"ESTUDIANTES Y SUS NOTAS: {dicc}")

# prom= dicc["ANDRES"]+dicc["FELIPE"]+dicc["JOSUE"]/3

# print(f"EL PROMEDIO DE LAS NOTAS DE ESTOS TRES ESTUDIANTES SERIA: {prom}")















