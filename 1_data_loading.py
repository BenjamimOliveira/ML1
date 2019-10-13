import csv
import numpy as np
import pandas

# using csv
path = r"/home/benjamim/Documents/ML1/test.csv"
with open(path, 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    headers = next(reader)
    data = list(reader)
    data = np.array(data)

# headers do csv
print(headers)
# linhas x colunas
print(data.shape)
# conteudo do csv
print(data)
#######################
print("-------------------------------------")
print("-------------------------------------\n")

# using numpy
from numpy import loadtxt
path = r"/home/benjamim/Documents/ML1/numbers.csv"
datapath = open(path, 'r')
data = loadtxt(datapath, delimiter=",")
print(data.shape)
print(data)
print("-------------------------------------")
print("-------------------------------------\n")

# using pandas
from pandas import read_csv
path = r"/home/benjamim/Documents/ML1/test.csv"
data = read_csv(path)
print(data.shape)
print(data)