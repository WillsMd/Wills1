# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 09:09:55 2022

@author: HP
"""
  import matplotlib
  import matplotlib.pyplot as plt
  import matplotlib.patches as mpatches
  from sklearn import datasets
 
  iris = datasets.load_iris()
  x = iris.data[:,0] #X-Axis - sepal length
  y = iris.data[:,1] #Y-Axis - sepal length
  species = iris.target #Species
 
  x_min, x_max = x.min() - .5,x.max() + .5
  y_min, y_max = y.min() - .5,y.max() + .5
 
  #SCATTERPLOT
  plt.figure()
  plt.title('Iris Dataset - Classification By Sepal Sizes')
  plt.scatter(x,y, c=species)
  plt.xlabel('Sepal length')
  plt.ylabel('Sepal width')
  plt.xlim(x_min, x_max)
  plt.ylim(y_min, y_max)
  plt.xticks(())
  plt.yticks(())
