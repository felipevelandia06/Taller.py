#Taller1
#ejercicio1
año=int(input('ingrese el año que quiera consultar '))
calculo1=año%4
calculo2=año%100
calculo3=año%400
if calculo1==0 and calculo2>0:
  print(año, 'es un año bisiesto')
elif calculo2==0 and calculo3>0:
  print(año, 'no es un año bisiesto')
elif calculo3==0:
  print(año, 'es un año bisiesto')
else:
  print(año, 'no es un año bisiesto')

#ejericio2 
peso=int(input('introduzca el peso de su perro (Kg) '))
altura=int(input('introduzca la altura de su perro (cm) '))
if peso<=15 and altura<=30:
  print('El tamaño de su perro mestizo es pequeño')
elif 30<altura<=40 and 15<peso<=25:
  print('El tamaño de su perro mestizo es mediano')
elif 40<altura<=60 and 25<peso<=45:
  print('El tamaño de su perro mestizo es grande')
else: print('Su perro mestizo no tiene medidas para catalogarlo en un tamaño específico')

#ejercicio3
def menu():
  print('''Ingresa el codigo correspondiente a la conversión que quiera realizar
1. °C - °F
2. °F - °C
3. °C - °K
4. °K - °C
5. °F - °K
6. °k - °F''')

def cf(a):
  t=(a*9/5)+32
  print(t)
  return t

def fc(a):
  t=(a-32)*5/9
  print(t)
  return t

def ck(a):
  t=a+273.15
  print(t)
  return t

def kc(a):
  t=a-273.15
  print(t)
  return t

def fk(a):
  t=(a-32)*5/9+273.15
  print(t)
  return t

def kf(a):
  t=(a-273.15)*9/5+32
  print(t)
  return t

def principal():
  menu()
  codigo=int(input())
  temperatura=float(input('ingrese la temperatura que quiera convertir '))
  if codigo==1:
    cf(temperatura)
  elif codigo==2:
    fc(temperatura)
  elif codigo==3:
    ck(temperatura)
  elif codigo==4:
    kc(temperatura)
  elif codigo==5:
    fk(temperatura)
  elif codigo==6:
    kf(temperatura)
  else: print('código no valido')

principal()

#ejercicio4
def menores(a):
  print('el costo de su curso es de 25.000 (grupo menores)')
  if 10<=a<=13:
    d=25000-(25000*0.15)
    print('el costo de su curso con el descuento es de', d)
  elif a==17:
    d=25000-(25000*0.08)
    print('el costo de su curso con el descuento es de', d)
  else: print('no aplica para ningun descuento')

def adultos(a):
  print('el costo de su curso es de 35.000 (grupo adultos)')
  if 18<=a<=30:
    d=35000-(35000*0.11)
    print('el costo de su curso con el descuento es de', d)
  else: 
    d=35000-(35000*0.09)
    print('el costo de su curso con el descuento es de', d)

def mayores(a):
  print('el precio de su curso es de 50.000 (grupo adultos mayores)')
  if a>65:
    d=50000-(50000*0.4)
    print('el costo de su curso con el descuento es de', d)
  else: print('no aplica para ningun descuento')

def principal():
  n=input('ingrese su nombre ')
  edad=int(input('ingrese su edad '))
  if 10<=edad<=17:
    menores(edad)
  elif 18<=edad<=50:
    adultos(edad)
  elif edad>50:
    mayores(edad)
  else: 
    print('no tiene edad permitida para inscribirse')

principal()

#ejercicio5
def menu():
  print('''ingrese el codigo correspondiente a la figura que desee calcular el volumen
1. Cubo
2. Cilindro
3. Esfera''')

def cubo():
  lado=float(input('ingrese el valor de un lado (m) '))
  vc=lado*lado*lado
  return vc

def cilindro():
  radiob=float(input('ingrese el valor del radio de la base (m) '))
  altura=float(input('ingrese el valor de la altura (m) '))
  vc=3.1416*(radiob**2)*altura
  return vc

def esfera():
  radio=float(input('ingrese el valor del radio (m) '))
  ve=(4/3)*3.1416*(radio**3)
  return ve

def principal():
  menu()
  codigo=int(input())
  if codigo==1:
    print('el volumen del cubo es', cubo(), 'm3')
  elif codigo==2:
    print('el volumen del cilindro es ', cilindro(), 'm3')
  elif codigo==3:
    print('el volumen de la esfera es ', esfera(), 'm3')
  else: print('codigo no valido')

principal()

#ejercicio6
def menu():
  print('''introduzca el codigo correspondiente al tamaño de la caja que quiera
1. Pequeña
2. Mediana
3. Grande
4. Extragrande''')

def pequeña(a):
  volumenc=a*0.167
  volument=volumenc/5
  if 0<volument<=1:
    print('se necesita una caja de este tamaño para este envío')
  elif 1<volument<=2:
    print('se necesitan dos cajas de este tamaño para este envío')
  else: print('Se necesitan tres o más cajas de este tamaño para este envío')

def mediana(a):
  volumenc=a*0.167
  volument=volumenc/7
  if 0<volument<=1:
    print('se necesita una caja de este tamaño para este envío')
  elif 1<volument<=2:
    print('se necesitan dos cajas de este tamaño para este envío')
  else: print('Se necesitan tres o más cajas de este tamaño para este envío')

def grande(a):
  volumenc=a*0.167
  volument=volumenc/10
  if 0<volument<=1:
    print('se necesita una caja de este tamaño para este envío')
  elif 1<volument<=2:
    print('se necesitan dos cajas de este tamaño para este envío')
  else: print('Se necesitan tres o más cajas de este tamaño para este envío')

def extragrande(a):
  volumenc=a*0.167
  volument=volumenc/15
  if 0<volument<=1:
    print('se necesita una caja de este tamaño para este envío')
  elif 1<volument<=2:
    print('se necesitan dos cajas de este tamaño para este envío')
  else: print('Se necesitan tres o más cajas de este tamaño para este envío')

def principal():
  cantidad=int(input('ingrese la cantidad de cubos rubik que desea ordenar '))
  menu()
  codigo=int(input())
  if codigo==1:
    pequeña(cantidad)
  elif codigo==2:
    mediana(cantidad)
  elif codigo==3:
    grande(cantidad)
  elif codigo==4:
    extragrande(cantidad)
  else: print('codigo no valido')

principal() 