import matplotlib.pyplot as plt

cluster = [0, 1, 2, 3, 4]
tam = [13.17, 14.92, 33.25, 34.56, 4.10]

colors = ['green','blue','purple','brown','teal']
plt.bar(cluster,tam, color=colors)
plt.title('Tamaño de clusters')
plt.xlabel('Cluster')
plt.ylabel('% de elementos')
plt.savefig("./bar.eps")