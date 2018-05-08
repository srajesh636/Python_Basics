#Series are nothing but one dimensional array capable of hollding any data type

import pandas as pd
import numpy as np

#Pandas contains a Method Series() for Creating Series

a=pd.Series()

print(a)

#to create a array we use array() in numpy module`
#creating empty array
b=np.array([])
print(b)

#creating array with some values

c=np.array([1,2])
d=pd.Series(c)
print(d)
