import matplotlib.pyplot as plt


cluster = [0, 1, 2, 3, 4]
tam = [20.30, 27.05, 7.72, 20.25, 24.69]

colors = ['green','blue','purple','brown','teal']
plt.bar(cluster,tam, color=colors)
plt.title('Tamaño de clusters')
plt.xlabel('Cluster')
plt.ylabel('% de elementos')
plt.savefig("./bar.eps")