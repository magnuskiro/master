__author__ = 'kiro'

import numpy as np
import mlpy
import matplotlib.pyplot as plt  # required for plotting


# testing file for the Support vector machine.
# auto classification with learning.

# load data
iris = np.loadtxt('iris.csv', delimiter=',')
#iris = np.loadtxt('classification-testdata.txt', delimiter=',')

# first 4 elements of each line.
# x: (observations x attributes) matrix --> for each tweet we have an array with observations(features).
x = iris[:, :4]

# last element in array for all lines.
# y: classification classes (1: setosa, 2: versicolor, 3: virginica) --> pos/neg
y = iris[:, 4].astype(np.int)

print "x", x.shape
print "y", y.shape

# reduce dimensions. Principal component analysis (PAC)
pca = mlpy.PCA()  # new PCA instance
pca.learn(x)  # learn from data
z = pca.transform(x, k=2)  # embed x into the k=2 dimensional subspace
print "z", z.shape

# Plot the principal components.
plt.set_cmap(plt.cm.Paired)
fig1 = plt.figure(1)
title = plt.title("PCA on iris dataset")
plot = plt.scatter(z[:, 0], z[:, 1], c=y)
labx = plt.xlabel("First component")
laby = plt.ylabel("Second component")
plt.show()

exit()

# learning by Kernel SVMs on principal components.
linear_svm = mlpy.LibSvm(kernel_type='linear')  # new linear SVM instance
linear_svm.learn(z, y)  # learn from principal components

xmin = z[:, 0].min() - 0.1
xmax = z[:, 0].max() + 0.1
ymin = z[:, 1].min() - 0.1
ymax = z[:, 1].max() + 0.1

print xmin, xmax
print ymin, ymax

xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.01), np.arange(ymin, ymax, 0.01))
zgrid = np.c_[xx.ravel(), yy.ravel()]

yp = linear_svm.pred(zgrid)

# plot the predictions.
plt.set_cmap(plt.cm.Paired)
fig2 = plt.figure(2)
title = plt.title("SVM (linear kernel) on principal components")
plot1 = plt.pcolormesh(xx, yy, yp.reshape(xx.shape))
plot2 = plt.scatter(z[:, 0], z[:, 1], c=y)
labx = plt.xlabel("First component")
laby = plt.ylabel("Second component")
limx = plt.xlim(xmin, xmax)
limy = plt.ylim(ymin, ymax)
plt.show()

