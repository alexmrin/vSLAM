import matplotlib.pyplot as plt
import numpy as np

k = 4
iterations = 10

class Cluster():
    def __init__(self):
        self.sum = np.zeros(2).reshape(2, 1)
        self.elements = []
        self.centroid = 0

    def mean(self):
        return self.sum/len(self.elements)

    def addelement(self, element):
        self.elements.append(element)
        self.sum += element

    def reset(self):
        mean = self.mean()
        self.centroid  = mean
        self.elements = []
        self.sum = 0


# Set a seed for reproducibility
np.random.seed(0)

# Generate 20 random points for x and y within the range -5 to 5
x = np.random.uniform(-5, 5, 100)
y = np.random.uniform(-5, 5, 100)
coordinates = np.array([np.array([x[i], y[i]]).reshape(2, 1) for i in range(len(x))])

clusters = [Cluster() for i in range(k)]
initial_coords = np.random.permutation(coordinates)[:k]
for cluster, init in zip(clusters, initial_coords):
    cluster.centroid = init

for i in range(iterations):
    for point in coordinates:
        distances = []
        for cluster in clusters:
            distances.append(np.linalg.norm(cluster.centroid - point))     

        closestIndex = np.argmin(distances)
        clusters[closestIndex].addelement(point)

    for cluster in clusters:
        cluster.centroid = cluster.mean()
        if i < iterations-1:
            cluster.reset()


for i, cluster in enumerate(clusters):
    cluster_elements = np.array(cluster.elements).squeeze()
    if cluster_elements.ndim == 1:
        plt.scatter(cluster_elements[0], cluster_elements[1])
    else:
        plt.scatter(cluster_elements[:, 0], cluster_elements[:, 1])
    plt.scatter(cluster.centroid[0, 0], cluster.centroid[1, 0], color='black', marker='+')

# Set the title and labels for the axes
plt.title('k means clustering')
plt.xlabel('X')
plt.ylabel('Y')

# Display the plot
plt.show()
