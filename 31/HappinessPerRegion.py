# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that creates a boxplot of the state of happiness per regions in the world using the world_happiness.csv dataset.

import matplotlib.pyplot as plt
f_in = open("world_happiness.csv", "rt")
X = [] # regions
Y_region = {} # happiness/region
f_in.readline()
for line in f_in:
    line = line.strip()
    data = line.split(",")
    region = data[1]
    if region not in X:
        X.append(region)
        Y_region[region] = []
    Y_region[region].append(float(data[5]))
f_in.close()
Y = []
for region in Y_region:
    Y.append(Y_region[region])
plt.ylabel("y (happiness)")
plt.grid(True)
plt.boxplot(Y, labels = X)
plt.show()

