#!usr/bin/python
#!encoding: UTF-8

import pylab as dibujo

x=[0.1,0.01,0.001,0.0001,0.00001]
x1=[10,50,100,150,500,550,1000]
y=[0,0,2,9,10]
y1=[0,0,0,4,18]
y2=[0,0,0,2,9]
y3=[0,0,0,1.33,6]
y4=[0,0,0,0.4,1.80]
y5=[0,0,0,0.36,1.64]
y6=[0,0,0,0.20,0.90]
t=[0.000686,0.007109,0.032868,0.058673,0.651724,0.885562,2.693729]

p1=dibujo.subplot(211)
dibujo.title('Porcentaje de fallo') 
dibujo.plot(x,y,marker='o',linestyle='-.',color='r',label='Aprox 10')    # Los colores Pueden ser: 'r','m','c','g','y','b'. Los estilos de lineas pueden ser: '--',':','-','-.'
                                                                       # Los marker pueden ser: 'o','s','p','*','+','.','^'
dibujo.plot(x,y1,marker='o',linestyle='-.',color='g',label='Aprox 50')
dibujo.plot(x,y2,marker='o',linestyle='-.',color='y',label='Aprox 100')
dibujo.plot(x,y3,marker='o',linestyle='-.',color='b',label='Aprox 150')
dibujo.plot(x,y4,marker='o',linestyle='-.',color='c',label='Aprox 500')
dibujo.plot(x,y5,marker='o',linestyle='-.',color='m',label='Aprox 550')
dibujo.plot(x,y6,marker='o',linestyle=':',color='r',label='Aprox 1000')
dibujo.legend()      # Esto se pone para que aparezca la leyenda de las lineas
dibujo.xlim(0,0.1)
dibujo.ylim(0,10)
dibujo.xticks(x)

p2=dibujo.subplot(212)
dibujo.xlabel('intervalos')
dibujo.ylabel('Tiempo en segundos')
dibujo.plot(x1,t,marker='+',linestyle='-',color='m',label='Linea 4')
dibujo.xlim(9,1000)
dibujo.ylim(0,2.8)
dibujo.show()