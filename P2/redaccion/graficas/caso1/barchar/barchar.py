import matplotlib.pyplot as plt

cluster = [0, 1, 2, 3, 4]
tam = [48.17, 16.84, 9.12, 8.42, 17.45]

colors = ['green','blue','purple','brown','teal']
plt.bar(cluster,tam, color=colors)
plt.title('Tamaño de clusters')
plt.xlabel('Cluster')
plt.ylabel('% de elementos')
plt.savefig("./bar.eps")