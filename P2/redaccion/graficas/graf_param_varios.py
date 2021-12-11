from matplotlib import pyplot as plt



fichero_leer = "2B_dbscan.csv"

silhouette1 = []
ch1 = []
silhouette2 = []
ch2 = []
silhouette3 = []
ch3 = []
silhouette4 = []
ch4 = []
silhouette5 = []
ch5 = []
param1 = []
param2 = []
param3 = []
param4 = []
param5 = []
lineas = []
with open(fichero_leer, "r") as fichero:
    lineas = fichero.readlines()

aux = lineas[0].split(",")
parametro = aux[1]
fijo = aux[2]
parametro1 = 15
parametro2 = 20
parametro3 = 25
parametro4 = 30
parametro5 = 35
lineas.pop(0)

for linea in lineas:
    aux = linea.split(",")

    if float(aux[2]) == parametro1:
        silhouette1.append(float(aux[-2]))
        ch1.append(float(aux[-3]))
        param1.append(float(aux[1]))
    elif float(aux[2]) == parametro2:
        silhouette2.append(float(aux[-2]))
        ch2.append(float(aux[-3]))
        param2.append(float(aux[1]))
    elif float(aux[2]) == parametro3:
        silhouette3.append(float(aux[-2]))
        ch3.append(float(aux[-3]))
        param3.append(float(aux[1]))
    elif float(aux[2]) == parametro4:
        silhouette4.append(float(aux[-2]))
        ch4.append(float(aux[-3]))
        param4.append(float(aux[1]))
    elif float(aux[2]) == parametro5:
        silhouette5.append(float(aux[-2]))
        ch5.append(float(aux[-3]))
        param5.append(float(aux[1]))



parametro1 = str(parametro1)
parametro2 = str(parametro2)
parametro3 = str(parametro3)
parametro4 = str(parametro4)
parametro5 = str(parametro5)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(param1,ch1, marker='x', label=fijo+"= "+parametro1)
ax1.plot(param2,ch2, marker='x', label=fijo+"= "+parametro2)
ax1.plot(param3,ch3, marker='x', label=fijo+"= "+parametro3)
ax1.plot(param4,ch4, marker='x', label=fijo+"= "+parametro4)
ax1.plot(param5,ch5, marker='x', label=fijo+"= "+parametro5)

ax1.set_title('Calinski-Harabasz')
ax1.set_xlabel(parametro)
ax1.set_ylabel('Calinski-Harabasz')
#ax1.legend(bbox_to_anchor=(0.5, -0.1))

ax2.plot(param1,silhouette1, marker='x', label=fijo+"= "+parametro1)
ax2.plot(param2,silhouette2, marker='x', label=fijo+"= "+parametro2)
ax2.plot(param3,silhouette3, marker='x', label=fijo+"= "+parametro3)
ax2.plot(param4,silhouette4, marker='x', label=fijo+"= "+parametro4)
ax2.plot(param5,silhouette5, marker='x', label=fijo+"= "+parametro5)

ax2.set_title('Silhouette')
ax2.set_xlabel(parametro)
ax2.set_ylabel('Silhouette')
#ax2.legend(bbox_to_anchor=(0.5, -0.1))

fig.legend(loc='lower left', bbox_to_anchor= (0.0, -0.2), ncol=2, borderaxespad=0, frameon=False)
fig.tight_layout(pad=3.0)
fig.savefig('B_parametros_dbscan.eps', bbox_inches='tight')
