# import scipy
import pandas
import numpy
from sklearn.preprocessing import MinMaxScaler, Binarizer, StandardScaler

# dataset link
# url = "https://github.com/LamaHamadeh/Pima-Indians-Diabetes-DataSet-UCI/blob/master/pima_indians_diabetes.txt"

# data parameters
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
 
# preparating of dataframe using the data at given link and defined columns list
dataframe = pandas.read_csv("diabetes.csv")
array = dataframe.values

# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]


#### rescale data

# # initialising the MinMaxScaler
# scaler = MinMaxScaler(feature_range=(0,1))
# rescaleX = scaler.fit_transform(X)

# # summarize transformed data
# numpy.set_printoptions(precision=3)
# print(rescaleX[0:5,:])

'''#### binarizer data
binarizer = Binarizer(threshold = 0.0).fit(X)
binaryX = binarizer.transform(X)

# summarize transformed data
numpy.set_printoptions(precision = 3)
print(binaryX[0:5,:])'''

# scaler = StandardScaler().fit(X)
# rescaledX = scaler.transform(X)
 
# # summarize transformed data
# numpy.set_printoptions(precision = 3)
# print(rescaledX[0:5,:])

