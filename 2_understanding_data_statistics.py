from pandas import read_csv
from pandas import set_option
path = r"/home/benjamim/Documents/ML1/test2.csv"
headernames = ['Lead', 'Title', 'Phone', 'Notes']
data = read_csv(path, names=headernames)
print(data.head(2))

print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------\n")
# verificar tamanho do sample
print(data.shape)

print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------\n")
# verificar datatypes dos campos
print(data.dtypes)

print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------\n")
# sumário estatistico da informação
path = r"/home/benjamim/Documents/ML1/dataStat.csv"
headernames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=headernames)
set_option('display.width', 100)
set_option('precision', 2)
print(data.shape)
print(data.describe())

print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------\n")
# rever a distribuição de classes
count_class = data.groupby('class').size()
print(count_class)

print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------\n")
# correlação entre atributos
correlations = data.corr(method='pearson')
print(correlations)

print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------\n")
# inclinação da distribuçao
print(data.skew())