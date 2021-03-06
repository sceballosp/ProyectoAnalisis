import PySimpleGUI as sg
from matplotlib import pyplot as plt
from prettytable import PrettyTable
import sympy as sym
import numpy as np
import sympy.parsing.sympy_parser as symp
from sympy.parsing.sympy_parser import parse_expr
from numpy.linalg import inv


transformations = (symp.standard_transformations + (symp.implicit_multiplication_application,))

x = sym.Symbol('x')

sg.theme('LightBlue5')

layout = [[sg.Text('Escoga el metodo que desea utilizar.')],
          [sg.Text('Cada vez que quiera escoger un metodo diferente debe volver a correr la aplicacion.')],
          [sg.InputCombo(('Busquedas incrementales', 
                          'Biseccion',
                          'Regla falsa',
                          'Punto fijo',
                          'Secante',
                          'Newton',
                          'Raices multiples metodo 1',
                          'Raices multiples metodo 2',
                          'Jacobi',
                          'Factorización LU',
                          'GaussSeidel',
                          'Eliminación Gaussiana',
                          'Pivoteo parcial',
                          'Pivoteo total',
                          'Sor',
                          'Vandermonde',
                          'Newton interpolacion'), size=(30, 1))], [sg.Submit(), sg.Cancel()]]

window = sg.Window('Escoger método', layout)

event, values = window.read()
window.close()
metodo =  values[0]

def entradaMatricesAb(n):
    col1 = [[sg.Text('A')],
           [sg.Input()],
           [sg.Text('b')],
           [sg.Input()]]
    col2 = [[sg.Text('A')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()]]
    col3 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    col4 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    col5 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    
    if n==1:
        col=col1
    elif n==2:
        col=col2
    elif n==3:
        col = col3
    elif n==4:
        col = col4
    elif n==5:
        col = col5
        
    return col

def entradaMatricesA(n):
    col1 = [[sg.Text('A')],
           [sg.Input()]]
    col2 = [[sg.Text('A')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    col3 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input()]]
    col4 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()]]
    col5 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()]]
    
    if n==1:
        col=col1
    elif n==2:
        col=col2
    elif n==3:
        col = col3
    elif n==4:
        col = col4
    elif n==5:
        col = col5
        
    return col

def entradaPuntos(n):
    col1 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()]]
    
    col2 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    
    col3 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    
    col4 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    col5 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]

    if n==1:
        col=col1
    elif n==2:
        col =col2
    elif n==3:
        col =col3
    elif n==4:
        col =col4
    elif n==5:
        col =col5
        
    return col

def grafica(f):
  xlist = np.linspace(-30, 30, num=1000)
  ylist = []

  for i in xlist:
    ylist.append(round(float(f.subs(x, i)), 3))

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')

  plt.plot(xlist, ylist)
  plt.grid()
  plt.show() 

#------------------------------------------------------------------------------------------------------------------------------------------------------

bITable = PrettyTable()
bITable.field_names =['Iteracion', 'Xn', 'F(x)']

def busquedasIncrementales (f, x0, deltax, numIteracion):
  if f.subs(x, x0) == 0:
    return (str(x0) + " Es una raíz de " + str(f))
  else: 
    xn = x0 + deltax
    iter = 0
  bITable.add_row([iter, xn, float(f.subs(x, xn))])
  while (numIteracion > iter and (f.subs(x,x0) * f.subs(x,xn)) > 0):
    x0 = xn
    xn = x0 + deltax
    iter += 1
    bITable.add_row([iter, xn, float(f.subs(x, xn))])
  if f.subs(x,xn) == 0:
    return (str(xn) + " Es una raíz de " + str(f))
  elif (f.subs(x,x0) * f.subs(x,xn)) < 0:
    result = [bITable, ("Existe una raíz de " + str(f) + " entre " + str(x0) + " y " + str(xn))]
    return result
  else:
    return ("No se han encontrado raices")
    

if metodo =='Busquedas incrementales':
    sg.theme('LightBlue5') 

    layout = [[sg.Text('Ingrese los datos solicitados.')],
              [sg.Text('Para expresar exponentes utilice ** o exp() y ulitice puntos para los decimales.')],
              [sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
              [sg.Text('deltax', size=(15, 1)), sg.InputText()],
              [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Busquedas incrementales', layout)
    event, values = window.read()
    window.close()

    f,x0, deltax, numIteracion = values[0],float(values[1]), float(values[2]),int(values[3]) 
    
    f = parse_expr(f, transformations=transformations)

    result = busquedasIncrementales(f,x0,deltax,numIteracion)

    if(len(result) != 2):
      resultLayout = [[sg.Text(result)]]
    else:
      resultLayout = [[sg.Text(result[0])],
                      [sg.Text(result[1])],
                      [sg.Button('Mostrar grafica')]]

    resultWindow = sg.Window('Resultado busquedas incrementales', resultLayout)
    event2, values2 = resultWindow.read()

    if event2 == 'Mostrar grafica':
      grafica(f)

    window.close()

#--------------------------------------------------------------------------------------------------------------------------------

biseccionTable = PrettyTable()
biseccionTable.field_names =['Iteracion', 'Xn', 'F(x)', 'Error']

def biseccion(f,xi, xf, tol, numIter):
  if (f.subs(x,xi) * f.subs(x,xf) == 0): 
    if (f.subs(x,xi) == 0):
      return("Hay una raíz de " + str(f) + " en " + str(xi))
    if (f.subs(x,xf) == 0):
      return("Hay una raíz de " + str(f) + " en " + str(xf))
  elif (f.subs(x,xi) * f.subs(x,xf) > 0):
    return("No se encuentran raices de " + str(f) )
  else:
    xm = (xi + xf)/2
    numIteracion = 0
    error = abs(xi-xm)
    biseccionTable.add_row([numIteracion, xm, float(f.subs(x, xm)), error])
    while (error>tol and numIteracion<numIter and f.subs(x,xm) != 0):
      if (f.subs(x,xi) * f.subs(x,xm) < 0):
        xf = xm
      else: 
        xi = xm
      xm = (xi + xf) / 2
      error = abs(xm - xi)
      numIteracion += 1
      biseccionTable.add_row([numIteracion, xm, float(f.subs(x, xm)), error])
      
    if (f.subs(x,xm) == 0):
      return("Se halló una raíz en " + str(xm) )
    elif error < tol: 
      result = [biseccionTable, str(xm) + " es raíz con tolerancia " + str(tol)+ " y el algorítmo paró en la iteración: " + str(numIteracion)]
      return result
    else:
      return("No se halló una solución")
         
if metodo =='Biseccion':
    sg.theme('LightBlue5')  # please make your windows colorful

    layout = [[sg.Text('Ingrese los datos solicitados.')],
              [sg.Text('Para expresar exponentes utilice ** o exp() y ulitice puntos para los decimales.')],
              [sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('xinicial', size=(15, 1)), sg.InputText()],
              [sg.Text('xfinal', size=(15, 1)), sg.InputText()],
              [sg.Text('tolerancia', size=(15, 1)), sg.InputText()],
              [sg.Text('Numerodeiteraciones', size=(15, 1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Bisección', layout)

    event, values = window.read()
    window.close()

    f,x0, xf, tol, numIter = values[0], float(values[1]),float(values[2]),float(values[3]),int(values[4]) 
    
    f = parse_expr(f, transformations=transformations)

    result = biseccion(f, x0, xf, tol, numIter)

    if(len(result) != 2):
      resultLayout = [[sg.Text(result)]]
    else:
      resultLayout = [[sg.Text(result[0])],
                      [sg.Text(result[1])],
                      [sg.Button('Mostrar grafica')]]

    resultWindow = sg.Window('Resultados Biseccion', resultLayout)
    event2, values2 = resultWindow.read()
    
    if event2 == 'Mostrar grafica':
      grafica(f)
      
    window.close()

#---------------------------------------------------------------------------------------------------------------------------------------    

reglaFalsaTable = PrettyTable()
reglaFalsaTable.field_names =['Iteracion', 'Xn', 'F(x)', 'Error']

def reglaFalsa (f,xi, xf, tol, numIter):
  if (f.subs(x,xi) * f.subs(x,xf) == 0):
    if (f.subs(x,xi) == 0):
      return("Hay una raíz de " + str(f) + " en " + str(xi))
    if (f.subs(x,xf) == 0):
      return("Hay una raíz de " + str(f) + " en " + str(xf))
  elif (f.subs(x,xi) * f.subs(x,xf) > 0):
    return("No se encuentran raices de " + str(f) )
  else: 
    xm = xf -((f.subs(x,xf)*(xi-xf))/(f.subs(x,xi)-f.subs(x,xf)))
    xm = float(xm)
    numIteracion = 0
    error = abs(xi-xm)
    reglaFalsaTable.add_row([numIteracion, xm, float(f.subs(x, xm)), error])
    while (error>tol and numIteracion<numIter and f.subs(x,xm) != 0):
      if (f.subs(x,xi) * f.subs(x,xm) < 0):
        xf = xm
      else: 
        xi = xm
      xm = xf -((f.subs(x,xf)*(xi-xf))/(f.subs(x,xi)-f.subs(x,xf)))
      xm = float(xm)
      error = abs(xm - xf)
      numIteracion += 1
      reglaFalsaTable.add_row([numIteracion, xm, float(f.subs(x, xm)), error])
    if(error < tol or f.subs(x,xm) == 0)  : 
      result =[reglaFalsaTable, str(xm) + "es raíz con tolerancia " + str(tol)+ " y el algorítmo paró en la iteración: " + str(numIteracion)]
      return result
    else:
      return("No se halló una solución")
     
if metodo =='Regla falsa':
    sg.theme('LightBlue5')  

    layout = [[sg.Text('Ingrese los datos solicitados.')],
              [sg.Text('Para expresar exponentes utilice ** o exp() y ulitice puntos para los decimales.')],
              [sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
              [sg.Text('xf', size=(15, 1)), sg.InputText()],
              [sg.Text('tol', size=(15, 1)), sg.InputText()],
              [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Regla falsa', layout)

    event, values = window.read()
    window.close()
    f, x0, xf, tol, numIter = values[0],float(values[1]), float(values[2]),float(values[3]),int(values[4]) 
    f = parse_expr(f, transformations=transformations)
    
    result = reglaFalsa(f, x0, xf, tol, numIter)

    if(len(result) != 2):
      resultLayout = [[sg.Text(result)]]
    else:
      resultLayout = [[sg.Text(result[0])],
                      [sg.Text(result[1])],
                      [sg.Button('Mostrar grafica')]]

    resultWindow = sg.Window('Resultados Regla Falsa', resultLayout)
    event2, values2 = resultWindow.read()
    
    if event2 == 'Mostrar grafica':
      grafica(f)
      
    window.close()

#--------------------------------------------------------------------------------------------------------------------------------

puntoFijoTable = PrettyTable()
puntoFijoTable.field_names =['Iteracion', 'Xn', 'F(x)', 'Error']

def puntoFijo(f, g, x0, tol, numIter):
  iter = 0
  error = tol + 1
  puntoFijoTable.add_row([iter, x0, float(f.subs(x, x0)), error])
  while (iter < numIter and error > tol):
    xn = float(g.subs(x,x0))
    error = abs(xn - x0)
    iter += 1
    x0 = xn
    puntoFijoTable.add_row([iter, xn, float(f.subs(x, x0)), error])
  if error < tol:
    result = [puntoFijoTable, str(xn) + " es raíz con tolerancia " + str(tol)+ " y el algorítmo paró en la iteración: " + str(iter)]
    return result
  else:
    return("El método no converge")
    
    
if metodo =='Punto fijo':
    sg.theme('LightBlue5') 

    layout = [[sg.Text('Ingrese los datos solicitados.')],
              [sg.Text('Para expresar exponentes utilice ** o exp() y ulitice puntos para los decimales.')],
              [sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('g', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
              [sg.Text('tol', size=(15, 1)), sg.InputText()],
              [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Punto Fijo', layout)

    event, values = window.read()
    window.close()
    f, g, x0, tol, numIter = values[0], values[1],float(values[2]), float(values[3]),int(values[4]) 
    f = parse_expr(f, transformations=transformations)
    g = parse_expr(g, transformations=transformations)
    
    result = puntoFijo(f, g, x0, tol, numIter)

    if(len(result) != 2):
      resultLayout = [[sg.Text(result)]]
    else:
      resultLayout = [[sg.Text(result[0])],
                      [sg.Text(result[1])],
                      [sg.Button('Mostrar grafica')]]

    resultWindow = sg.Window('Resultados Punto Fijo', resultLayout)
    event2, values2 = resultWindow.read()
    
    if event2 == 'Mostrar grafica':
      grafica(f)
      
    window.close()

#-----------------------------------------------------------------------------------------------------------------------------

secanteTable = PrettyTable()
secanteTable.field_names =['Iteracion', 'Xn', 'F(x)']

def metodoSecante(f,x0,x1,numIter,tol):
  iter = 0
  while iter <= numIter:
    newX1 = float(x1 - (f.subs(x, x1)*((x1 - x0) / (f.subs(x, x1) - f.subs(x, x0)))))
    secanteTable.add_row([iter, newX1, float(f.subs(x, newX1))])
    if f.subs(x, x0) == 0:
      return(str(x0) + " es una raíz de " + str(f))
    elif abs(newX1 - x1) <= tol:
      result = [secanteTable, str(newX1) + " es raíz con tolerancia " + str(tol) + " con "+ str(iter)+" iteraciones."]
      return result
    elif iter > numIter:
      return("El metodo no converge en estas iteraciones " + str(iter))
    else:
      iter += 1
      x0 = x1
      x1 = newX1

if metodo =='Secante':
    sg.theme('LightBlue5')

    layout = [[sg.Text('Ingrese los datos solicitados.')],
              [sg.Text('Para expresar exponentes utilice ** o exp() y ulitice puntos para los decimales.')],
              [sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
              [sg.Text('xf', size=(15, 1)), sg.InputText()],
              [sg.Text('tol', size=(15, 1)), sg.InputText()],
              [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Secante', layout)

    event, values = window.read()
    window.close()
    f,x0, xf,tol, numIter = values[0],float(values[1]), float(values[2]),float(values[3]),int(values[4]) 
    f = parse_expr(f, transformations=transformations)
    
    result = metodoSecante(f, x0, xf, numIter, tol)

    if(len(result) != 2):
      resultLayout = [[sg.Text(result)]]
    else:
      resultLayout = [[sg.Text(result[0])],
                      [sg.Text(result[1])],
                      [sg.Button('Mostrar grafica')]]

    resultWindow = sg.Window('Resultados Secante', resultLayout)
    event2, values2 = resultWindow.read()
    
    if event2 == 'Mostrar grafica':
      grafica(f)
      
    window.close()

#-----------------------------------------------------------------------------------------------------------------------------------------------    

newtonTable = PrettyTable()
newtonTable.field_names =['Iteracion', 'Xn', 'F(x)', 'Error']

def Newton (f, df, x0, tol, numIter):
  cont = 0
  error = tol + 1
  newtonTable.add_row([cont, x0, float(f.subs(x, x0)), error])
  while (cont < numIter and error > tol):
    xn = x0 - float(f.subs(x, x0))/float(df.subs(x, x0))
    error = abs(xn - x0) / abs(xn) # Relativo
    cont += 1
    x0 = xn
    newtonTable.add_row([cont, x0, float(f.subs(x, xn)), error])
    
  if error <= tol:
    result = [newtonTable, str(xn) + " es raíz con tolerancia " + str(tol)+ " y el algorítmo paró en la iteración: " + str(cont)]
    return result
  else:
    return ("El método no converge")

if metodo =='Newton':
  sg.theme('LightBlue5') 

  layout = [[sg.Text('Ingrese los datos solicitados.')],
            [sg.Text('Para expresar exponentes utilice ** o exp() y ulitice puntos para los decimales.')],
            [sg.Text('f', size=(15, 1)), sg.InputText()],
            [sg.Text('x0', size=(15, 1)), sg.InputText()],
            [sg.Text('tol', size=(15, 1)), sg.InputText()],
            [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]]

  window = sg.Window('Newton', layout)

  event, values = window.read()
  window.close()

  f, x0, tol, numIter = values[0],float(values[1]), float(values[2]),int(values[3]) 
      
  f = parse_expr(f, transformations=transformations)
  df = sym.diff(f, x)

  result = Newton(f, df, x0, tol, numIter)

  if(len(result) != 2):
    resultLayout = [[sg.Text(result)]]
  else:
    resultLayout = [[sg.Text(result[0])],
                    [sg.Text(result[1])],
                    [sg.Button('Mostrar grafica')]]

  resultWindow = sg.Window('Resultados Newton', resultLayout)
  event2, values2 = resultWindow.read()
  
  if event2 == 'Mostrar grafica':
      grafica(f)
      
  window.close()
  
#-----------------------------------------------------------------------------------------------------------------------------------------------    

raicesMultiplesTable = PrettyTable()
raicesMultiplesTable.field_names =['Iteracion', 'Xn', 'F(x)', 'Error']

def RaicesMultiples (f, df, dff, x0, numIter, tol):
  iter = 0
  error = tol + 1
  raicesMultiplesTable.add_row([iter, x0, float(f.subs(x, x0)), error])
  while (iter < numIter and error > tol):
    xn = x0 - (float(f.subs(x, x0))/float(df.subs(x, x0)))
    error = abs(xn - x0) #Absoluto
    iter += 1
    x0 = xn
    raicesMultiplesTable.add_row([iter, x0, float(f.subs(x, x0)), error])
  if error <= tol:
    result = [raicesMultiplesTable, str(xn) + " es raíz con tolerancia " + str(tol)+ " y el algorítmo paró en la iteración: " + str(iter)]
    return result
  else:
    return("El método no converge")

if metodo =='Raices multiples metodo 1':
    sg.theme('LightBlue5') 

    layout = [[sg.Text('Ingrese los datos solicitados.')],
              [sg.Text('Para expresar exponentes utilice ** o exp() y ulitice puntos para los decimales.')],
              [sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
              [sg.Text('tol', size=(15, 1)), sg.InputText()],
              [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Raíces multiples meotodo 1', layout)

    event, values = window.read()
    window.close()
    f,x0, tol,numIter = values[0],float(values[1]), float(values[2]),int(values[3]) 
    
    f = parse_expr(f, transformations=transformations)
    df = sym.diff(f, x)
    dff= sym.diff(df,x)
    
    result = RaicesMultiples(f, df, dff, x0, numIter, tol)

    if(len(result) != 2):
      resultLayout = [[sg.Text(result)]]
    else:
      resultLayout = [[sg.Text(result[0])],
                      [sg.Text(result[1])],
                      [sg.Button('Mostrar grafica')]]

    resultWindow = sg.Window('Resultados Raices multiples metodo 1', resultLayout)
    event2, values2 = resultWindow.read()
    
    if event2 == 'Mostrar grafica':
      grafica(f)
      
    window.close()

#-------------------------------------------------------------------------------------------------------------------------------------

raicesMultiples2Table = PrettyTable()
raicesMultiples2Table.field_names =['Iteracion', 'Xn', 'F(x)', 'Error']

def RaicesMultiples2 (f, df, dff, x0, numIter, tol):
  iter = 0
  error = tol + 1
  raicesMultiples2Table.add_row([iter, x0, float(f.subs(x, x0)), error])
  while (iter < numIter and error > tol):
    xn = x0 - (float(f.subs(x, x0)*df.subs(x,x0))/float(df.subs(x, x0)**2-(f.subs(x, x0)*dff.subs(x,x0))))
    error = abs(xn - x0) #Absoluto
    iter += 1
    x0 = xn
    raicesMultiples2Table.add_row([iter, x0, float(f.subs(x, x0)), error])
  if error <= tol:
    result = [raicesMultiples2Table, str(xn) + " es raíz con tolerancia " + str(tol)+ " y el algorítmo paró en la iteración: " + str(iter)]
    return result
  else:
    return("El método no converge")

if metodo =='Raices multiples metodo 2':
    sg.theme('LightBlue5') 

    layout = [[sg.Text('Ingrese los datos solicitados.')],
              [sg.Text('Para expresar exponentes utilice ** o exp() y ulitice puntos para los decimales.')],
              [sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
              [sg.Text('tol', size=(15, 1)), sg.InputText()],
              [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Raíces multiples meotodo 2', layout)

    event, values = window.read()
    window.close()
    f,x0, tol,numIter = values[0],float(values[1]), float(values[2]),int(values[3]) 
    
    f = parse_expr(f, transformations=transformations)
    df = sym.diff(f, x)
    dff= sym.diff(df,x)
    
    result = RaicesMultiples2(f, df, dff, x0, numIter, tol)

    if(len(result) != 2):
      resultLayout = [[sg.Text(result)]]
    else:
      resultLayout = [[sg.Text(result[0])],
                      [sg.Text(result[1])],
                      [sg.Button('Mostrar grafica')]]

    resultWindow = sg.Window('Resultados Raices multiples metodo 2', resultLayout)
    event2, values2 = resultWindow.read()
    
    if event2 == 'Mostrar grafica':
      grafica(f)
      
    window.close()

#------------------------------------------------------------------------------------------------------------------

def factorizacionLU(A):
    n, m = A.shape
    P = np.identity(n)
    L = np.identity(n)
    U = A.copy()
    PF = np.identity(n)
    LF = np.zeros((n,n))
    for k in range(0, n - 1):
        index = np.argmax(abs(U[k:,k]))
        index = index + k 
        if index != k:
            P = np.identity(n)
            P[[index,k],k:n] = P[[k,index],k:n]
            U[[index,k],k:n] = U[[k,index],k:n] 
            PF = np.dot(P,PF)
            LF = np.dot(P,LF)
        L = np.identity(n)
        for j in range(k+1,n):
            L[j,k] = -(U[j,k] / U[k,k])
            LF[j,k] = (U[j,k] / U[k,k])
        U = np.dot(L,U)
    np.fill_diagonal(LF, 1)
    return  LF, U


if metodo =='Factorización LU':
    sg.theme('LightBlue5')

    layout = [[sg.Text('Defina el tamaño de la matriz')],
              [sg.Slider(range=(1, 5), orientation='h', size=(20, 20), default_value=3)],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Jacobi', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')

    col = entradaMatricesA(n)
        
    layout = [[sg.Text('Ingrese la matriz')],
              [sg.Column(col)],
              [sg.OK()]]
    
    window = sg.Window('FactorizacionLU', layout)
    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
    
    A = []

    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    
    L,U=factorizacionLU(A)
        
    sg.Popup('FactorizacionLU',
             'La matriz L es: ',L,
             'La matriz U es: ',U)
    window.close()

#----------------------------------------------------------------------------------------------------------------------------

def jacobi(A,b,tol,numIter):
  n = np.size(A,0)
  L = - np.tril(A, -1)
  U = - np.triu(A,1)
  D = A+L+U
  x0 = np.zeros([n,1])
  Tj = np.matmul(inv(D),(L+U))
  autovalores, autovectores = np.linalg.eig(Tj)
  autovalores = abs(autovalores)

  for lam in autovalores:
    if lam >= 1:
      return ("El método no converge.")

  C = np.matmul(inv(D),b)
  xn = (np.matmul(Tj,x0))+C
  error = np.array(abs(xn - (np.dot(Tj,xn)+C)))
  error = np.amax(error)
  iter = 0
  while ((error > tol) and (iter<numIter)):
    nuevo = np.matmul(Tj,xn)+C
    error = np.array(abs(nuevo-xn))
    error = np.amax(error)
    xn = nuevo
    iter = iter +1
  result = "El método converge en "+str(xn)
  return result

if metodo =='Jacobi':
    sg.theme('LightBlue5') 

    layout = [[sg.Text('Escoger el número de ecuaciones')],
              [sg.Slider(range=(1, 5), orientation='h', size=(20, 20), default_value=3)],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Jacobi', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')

    col = entradaMatricesAb(n)
        
    layout = [[sg.Text('Ingrese los datos solicitados.')],
              [sg.Text('Para la matriz ingrese solo el coeficiente de las variables.')],
              [sg.Column(col)],
              [sg.Text('Tolerancia', size=(15, 1)), sg.InputText()],
              [sg.Text('NumeroIteraciones', size=(15, 1)), sg.InputText()],
              
              [sg.OK()]]
    window = sg.Window('Jacobi', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
    
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
    tol = values[cont]
    numIter = int(values[cont+1])
        
    result = jacobi(A, b, tol, numIter)

    sg.Popup('Resultados Jacobi', result, line_width=300)

    window.close()

#---------------------------------------------------------------------------------------------------------------------------------

def GaussSeidel(A,b,tol,numIter):
  n = np.size(A,0)
  L = - np.tril(A, -1)
  U = - np.triu(A,1)
  D = A+L+U
  x0 = np.zeros([n,1])
  Tg = np.matmul(inv(D-L),U)
  autovalores, autovectores = np.linalg.eig(Tg)
  autovalores = abs(autovalores)

  for lam in autovalores:
    if lam >= 1:
      return ("El método no converge.")

  C = np.matmul(inv(D-L),b)
  xn = (np.matmul(Tg,x0))+C
  error = np.array(abs(xn - (np.dot(Tg,xn)+C)))
  error = np.amax(error)
  iter = 0
  while ((error > tol) and (iter<numIter)):
    nuevo = np.matmul(Tg,xn)+C
    error = np.array(abs(nuevo-xn))
    error = np.amax(error)
    xn = nuevo
    iter = iter +1
  return("El método converge en "+str(xn))

if metodo =='GaussSeidel':
    sg.theme('LightBlue5')  

    layout = [[sg.Text('Escoger el número de ecuaciones')],
              [sg.Slider(range=(1, 5), orientation='h', size=(20, 20), default_value=3)],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('GaussSeidel', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')
    
    col = entradaMatricesAb(n)
        
    layout = [[sg.Text('Ingrese los datos solicitados.')],
              [sg.Text('Para la matriz ingrese solo el coeficiente de las variables.')],
              [sg.Column(col)],
              [sg.Text('Tolerancia', size=(15, 1)), sg.InputText()],
              [sg.Text('NumeroIteraciones', size=(15, 1)), sg.InputText()],
              
              [sg.OK()]]
    window = sg.Window('GaussSeidel', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
        
    
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
    tol = values[cont]
    numIter = int(values[cont+1])
        
    sg.Popup('GaussSeidel',
             GaussSeidel(A, b,tol,numIter))
    window.close() 

#-------------------------------------------------------------------------------------------------------------------------------------

def eliminacionGaussiana(A, b):
  n = b.size
  Ab =  np.append(A,b, axis=1)
  for k in range(n):
    for i in range(k+1,n):
      mult = Ab[i][k] / Ab[k][k]
      for j in range(k,n+1):
        Ab[i][j]=Ab[i][j]-mult*Ab[k][j]
  x = np.zeros(n)
  x[n-1]=Ab[n-1][n]/Ab[n-1][n-1]
  for i in range(n-1,-1,-1):
    sum= 0 
    for p in range(i+1,n):
      sum = sum + Ab[i][p] * x[p]
    x[i] = (Ab[i][n]-sum)/Ab[i][i]
  return x
    
if metodo =='Eliminación Gaussiana':
    sg.theme('LightBlue5')  

    layout = [[sg.Text('Escoger el número de ecuaciones')],
              [sg.Slider(range=(1, 5), orientation='h', size=(20, 20), default_value=3)],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Eliminación Gaussiana', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')
    
    col = entradaMatricesAb(n)
        
    layout = [[sg.Text('Para la matriz ingrese solo el coeficiente de las variables.')],
              [sg.Column(col)],
              [sg.OK()]]

    window = sg.Window('Eliminación Gaussiana', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
        
    
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
        
    sg.Popup('Eliminación Gaussiana',
             eliminacionGaussiana(A, b))
    window.close()
    

#--------------------------------------------------------------------------------------------------------------------------------------

def pivoteoParcial(A, b):
  n = b.size
  Ab =  np.append(A,b, axis=1)
  for k in range(n):
    c = max(abs(Ab[k:,k]))
    index = list(abs(Ab[:,k])).index(c)
    maxx = np.array(Ab[index,:],dtype=float)
    Ab[index,:] = np.array(Ab[k,:],dtype=float)
    Ab[k,:] = maxx
    Ab = np.array(Ab,dtype=float)
    for i in range(k+1,n):
      mult = Ab[i][k] / Ab[k][k]
      for j in range(k,n+1):
        Ab[i][j]=Ab[i][j]-mult*Ab[k][j]
  x = np.zeros(n)
  x[n-1]=Ab[n-1][n]/Ab[n-1][n-1]
  for i in range(n-1,-1,-1):
    sum= 0 
    for p in range(i+1,n):
      sum = sum + Ab[i][p] * x[p]
    x[i] = (Ab[i][n]-sum)/Ab[i][i]
  return x


if metodo =='Pivoteo parcial':
    sg.theme('LightBlue5')

    layout = [[sg.Text('Defina el tamaño de la matriz')],
              [sg.Slider(range=(1, 5), orientation='h', size=(20, 20), default_value=3)],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Pivoteo parcial', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')
    
    col = entradaMatricesAb(n)
        
    layout = [[sg.Text('Ingrese la matriz.')],
              [sg.Column(col)],
              [sg.OK()]]

    window = sg.Window('Pivoteo parcial', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
        
    
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
        
    sg.Popup('Pivoteo parcial',
             'Se obtiene como respuesta el vector x:',
             pivoteoParcial(A, b))
    window.close()

#----------------------------------------------------------------------------------------------------------------------------------------------------    
    
def pivoteoTotal(A, b):
  n = b.size
  Ab =  np.append(A,b, axis=1)
  Ab = np.array(Ab,dtype=float)
  x = np.array(list(range(n)))
  for k in range(0,n):
    A = Ab[:,:-1]
    c = abs(A[k:,k:]).max()
    index = np.where(abs(A)==c)

    c_temp = Ab[:,index[1][0]].copy()
    Ab[:,index[1][0]]= Ab[:,k].copy()
    Ab[:,k] = c_temp

    x_temp= x[index[1][0]]
    x[index[1][0]]= x[k]
    x[k]= x_temp

    r_temp= Ab[index[0][0],:].copy()
    Ab[index[0][0],:]= Ab[k,:].copy()
    Ab[k,:] = r_temp

    Ab[k,:]= Ab[k,:]*(1/c)

    for i in range(0,n):
      if i != k:
        Ab[i,:]= Ab[i,:].copy()+Ab[k,:].copy()*(-Ab[i,k].copy())

  S= Ab[:,-1]
  B=[]
  for i in range(0,n):
    B.append(float(S[np.where(x==i)]))
  return B

if metodo =='Pivoteo total':
    sg.theme('LightBlue5')
    layout = [[sg.Text('Defina el tamaño de la matriz')],
              [sg.Slider(range=(1, 5), orientation='h', size=(20, 20), default_value=3)],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Pivoteo total', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')
    
    col = entradaMatricesAb(n)
        
    layout = [[sg.Text('Ingrese la matriz.')],
              [sg.Column(col)],
              [sg.OK()]]

    window = sg.Window('Pivoteo total', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
        
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
    
    sg.Popup('Pivoteo total',
             'Se obtiene como respuesta el vector x:',
             pivoteoTotal(A, b))
    window.close()

#----------------------------------------------------------------------------------------------------------------------------------------------------
def vander(x,y):
  
  points = zip(x, y)
  sorted_points = sorted(points)
  new_xs = [point[0] for point in sorted_points]
  new_ys = [point[1] for point in sorted_points]
  xn = np.array(new_xs)
  yn = np.array([new_ys]).T

  A = np.vander(xn)
  Ainv = np.linalg.inv(A)
  a = np.dot(Ainv, yn)
  
  return [A, Ainv, a]

def convert(string):
  vector = []
  li = list(string.split(" "))
  for i in li:
    vector.append(int(i))
  
  return vector

if metodo =='Vandermonde':
    sg.theme('LightBlue5')

    layout = [[sg.Text('Ingrese los vectores X y Y')],
              [sg.Text('Digite cada numero seguido de un espacio')],
              [sg.Text('X', size=(15, 1)), sg.InputText()],
              [sg.Text('Y', size=(15, 1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Vandermonde', layout)

    event, values = window.read()
    window.close()
    
    x = convert(values[0])
    y = convert(values[1])

    result = vander(x, y)

    resultLayout = [[sg.Text('Matriz de Vandemonde:')],
                    [sg.Text(result[0])],
                    [sg.Text('Matriz inversa:')],
                    [sg.Text(result[1])],
                    [sg.Text(result[2])],
                    [sg.Button('Mostrar grafica')]]
    
    resultWindow = sg.Window('Resultados Raices multiples metodo 1', resultLayout)
    event2, values2 = resultWindow.read()
    
    if event2 == 'Mostrar grafica':
      grafica(f)
      
    window.close()


  
#def sor(x0, A, b, tol, numIter, w):
#  n = np.size(A,0)
#  L = - np.tril(A, -1)
#  U = - np.triu(A,1)
#  D = A+L+U
#  x0 = np.zeros([n,1])
#  Tg = np.matmul(inv(D-L),U)
#  autovalores, autovectores = np.linalg.eig(Tg)
#  autovalores = abs(autovalores)
#
#  for lam in autovalores:
#    if lam >= 1:
#      return ("El método no converge.")
#
#  C = np.matmul(inv(D-L),b)
#  xn = (np.matmul(Tg,x0))+C
#  error = np.array(abs(xn - (np.dot(Tg,xn)+C)))
#  error = np.amax(error)
#  iter = 0
#  while ((error > tol) and (iter<numIter)):
#    nuevo = np.matmul(Tg,xn)+C
#    error = np.array(abs(nuevo-xn))
#    error = np.amax(error)
#    xn = nuevo
#    iter = iter +1
#  return("El método converge en "+str(xn))
#
#
#if metodo =='Sor':
#    sg.theme('Dark Blue 3')  
#
#    layout = [[sg.Text('Escoger el número de ecuaciones')],
#              [sg.Slider(range=(1, 5), orientation='h', size=(20, 20), default_value=3)],
#              [sg.Submit(), sg.Cancel()]]
#
#    window = sg.Window('Sor', layout)
#
#    event, values = window.read()
#    window.close()
#    
#    n = int(values[0])
#
#    window = sg.Window('Columns')
#    
#    col = entradaMatricesAb(n)
#        
#    layout = [[sg.Column(col)],
#              [sg.Text('Tolerancia', size=(15, 1)), sg.InputText()],
#              [sg.Text('NumeroIteraciones', size=(15, 1)), sg.InputText()],
#              
#              [sg.OK()]]
#    window = sg.Window('GaussSeidel', layout)
#
#    event, values = window.read()
#    window.close()
#    
#    for i in range(len(values)):
#        values[i]=float(values[i])
#        
#    
#    A = []
#    b = []
#    cont = 0
#    
#    for i in range(n):
#        row = []
#        for j in range(n):
#            row.append(values[cont])
#            cont = cont +1
#        A.append(row)
#    A=np.array(A)
#    for i in range(n):
#        b.append([values[cont]])
#        cont = cont+1
#    b = np.array(b)
#    tol = values[cont]
#    numIter = int(values[cont+1])
#        
#    sg.Popup('GaussSeidel',
#             GaussSeidel(A, b,tol,numIter))
#    window.close()
#