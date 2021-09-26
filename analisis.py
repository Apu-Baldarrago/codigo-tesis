import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos=pd.read_csv("test-1.csv",sep=";")
#print(datos)
datos.info()
#print(datos.iloc[0,0])
#print(datos.iloc[0:2,3:6])
#print(datos.iloc[-5:-1,3:6])
a=0
b=0
#pru = datos[["Tiempo","Resistencia","Etapa"]]
for i in datos["Tiempo"]:
	if 0 == datos.iloc[a,8]:
		
		b+=1
	a+=1
print(a)
print(b)

plt.plot(datos["Tiempo"],datos["Resistencia"],".",label="R-vs-T")
plt.legend()
plt.xlabel("Tiempo (s)")
plt.ylabel("Resistencia Mohm")
#plt.show()
