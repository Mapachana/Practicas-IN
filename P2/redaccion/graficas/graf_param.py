from matplotlib import pyplot as plt



fichero_leer = "3_meanshift.csv"

silhouette = []
ch = []
param = []
lineas = []
with open(fichero_leer, "r") as fichero:
    lineas = fichero.readlines()

aux = lineas[0].split(",")
parametro = aux[1]
lineas.pop(0)
for linea in lineas:
    aux = linea.split(",")

    if aux[-2] != "" and aux[-1] != "":
        silhouette.append(float(aux[-2]))
        ch.append(float(aux[-3]))
        param.append(float(aux[1]))
        print("aa")
        
print(param)
print(silhouette)
print(ch)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(param,ch, marker='x')
ax1.set_title('Calinski-Harabasz')
ax1.set_xlabel(parametro)
ax1.set_ylabel('Calinski-Harabasz')
ax2.plot(param,silhouette, marker='x')
ax2.set_title('Silhouette')
ax2.set_xlabel(parametro)
ax2.set_ylabel('Silhouette')

fig.legend()
fig.tight_layout(pad=3.0)
fig.savefig('3_parametros_meanshift.eps')
