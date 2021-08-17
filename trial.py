import numpy as np

m = "455"
m = list(m)
n = "123123"
n = list(n)

row = "|                        |"
row = list(row)
row_sliced1 = row[0:2]
row_sliced2 = row[2:len(m)]
row_sliced3 = row[len(m):]
row_sliced2 =  m

row = np.concatenate((row_sliced1,row_sliced2,row_sliced3))

print(row)
