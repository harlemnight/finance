import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import pandas as pd


x = np.array([[1,2,3],[4,5,6]])
print("x:\n{}".format(x))


eye = np.eye(4)
print("numpy array:\n{}".format(eye))
print(eye)

sparse_matrix = sparse.csr_matrix(eye)
print("\nScipy sparse csr matrix:\n{}".format(sparse_matrix))

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data,(row_indices,col_indices)))
print("coo represenetation:\n{}".format(eye_coo))

data = {'Name': ["John", "Anna", "Peter", "Linda"],
'Location' : ["New York", "Paris", "Berlin", "London"],
'Age' : [24, 13, 53, 33]
}
data_pandas = pd.DataFrame(data)
print(data_pandas[data_pandas.Age > 30])


#
# x = np.linspace(-10,10,100)
# y = np.sin(x)
# plt.plot(x,y,marker="X")
# plt.show()
from sklearn.datasets import load_iris
iris_dataset = load_iris()
print(type(iris_dataset))
print(iris_dataset.keys())
print(iris_dataset['target_names'])
print(iris_dataset['target'])
print(iris_dataset['data'].shape)