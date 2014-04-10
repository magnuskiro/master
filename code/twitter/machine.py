__author__ = 'kiro'

import numpy as np
import mlpy
import matplotlib.pyplot as plt # required for plotting


# testing file for the Support vector machine.
# auto classification with learning.

#iris = np.loadtxt('iris.csv', delimiter=',')
iris = np.loadtxt('classification-testdata.txt', delimiter=',')
# x: (observations x attributes) matrix --> for each tweet we have an array with observations(features).
# y: classes (1: setosa, 2: versicolor, 3: virginica) --> pos/neg
#x, y = iris[:, :4], iris[:, 4].astype(np.int)
x, y = iris[:, :3], iris[:, 3].astype(np.int)

print x.shape
print y.shape

pca = mlpy.PCA() # new PCA instance
pca.learn(x) # learn from data
z = pca.transform(x, k=2) # embed x into the k=2 dimensional subspace
print z.shape

plt.set_cmap(plt.cm.Paired)
fig1 = plt.figure(1)
title = plt.title("PCA on iris dataset")
plot = plt.scatter(z[:, 0], z[:, 1], c=y)
labx = plt.xlabel("First component")
laby = plt.ylabel("Second component")
plt.show()

linear_svm = mlpy.LibSvm(kernel_type='linear') # new linear SVM instance
linear_svm.learn(z, y) # learn from principal components

xmin, xmax = z[:,0].min()-0.1, z[:,0].max()+0.1
ymin, ymax = z[:,1].min()-0.1, z[:,1].max()+0.1

print xmin, xmax
print ymin, ymax

xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.01), np.arange(ymin, ymax, 0.01))
zgrid = np.c_[xx.ravel(), yy.ravel()]

yp = linear_svm.pred(zgrid)

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

