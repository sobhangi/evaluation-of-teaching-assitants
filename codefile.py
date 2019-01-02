#import
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv('DATASET PROJECT.csv')
X= dataset.iloc[:,2:4].values
Y=dataset.iloc[:,4].values

#importing dataset
dataset = pd.read_csv('DATASET PROJECT.csv')
X= dataset.iloc[:,0:5].values
Y=dataset.iloc[:,5].values