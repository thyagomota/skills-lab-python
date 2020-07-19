# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that plot data points in an attempt to show an association between income and happiness. Then, modify the program and try to model the association using a linear regression tool.

import statsmodels.api as sm
import matplotlib.pyplot as plt
f_in = open("income_happiness.csv", "rt")
X = []
Y = []
f_in.readline()
for line in f_in:
    line = line.strip()
    seq, income, happy = line.split(",")
    X.append(float(income))
    Y.append(float(happy))
f_in.close()
plt.scatter(X, Y)
plt.xlabel("x (income)")
plt.ylabel("y (happiness)")
plt.grid(True)
# linear model
model = sm.OLS(Y, X).fit()
Y_model = model.predict(X)
plt.plot(X, Y_model, color = "r")
plt.show()


