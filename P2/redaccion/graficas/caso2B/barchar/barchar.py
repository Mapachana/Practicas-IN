import matplotlib.pyplot as plt

cluster = [0, 1, 2, 3, 4]
tam = [52.45, 8.33, 7.07, 8.46, 23.70]

colors = ['green','blue','purple','brown','teal']
plt.bar(cluster,tam, color=colors)
plt.title('Tamaño de clusters')
plt.xlabel('Cluster')
plt.ylabel('% de elementos')
plt.savefig("./bar.eps")