#importing usable library

#numpy for algebra operation
#matplotlib for visualization
#pandas for data analysing

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading data from csv file
data = pd.read_csv('studentscores.csv')


#trainning data
x_train = data['Hours'].head(15)
y_train = data['Scores'].head(15)

#test data
x_test =  data['Hours'].tail(10)
y_test = data['Scores'].tail(10)

#mean of x and y training set
mean_x = np.mean(x_train)
mean_y = np.mean(y_train)


#calculate predicted y
def predicted_y(x_train,y_train,mean_x,mean_y):
    # length of training set
    m = len(x_train)

    nume_val = 0;
    deno_val = 0;

    #formula
    """ 
        line = y = b1x + bo
        b1 = slope =((x-x_mean) * (y-y_mean)) / x-x_mean^2
        b0 = intercept = y-b1x
    """


    for i in range(m):
        nume_val += (x_train[i] - mean_x) * (y_train[i] - mean_y)
        deno_val += (x_train[i] - mean_x) ** 2

    b1 = nume_val / deno_val
    b0 = mean_y - (b1 * mean_x)
    Y = b0 + b1 * x_test
    return Y

#calculate R2test for accuracy

def R2Test(y_test,Y):
    mean_y_test = sum(y_test) / len(y_test)
    r1 = sum((y_test - mean_y_test) ** 2)
    r2 = sum((Y - mean_y_test) ** 2)
    r_sq = r2 / r1
    return r_sq


Y = predicted_y(x_train,y_train,mean_x,mean_y)
r_sq = R2Test(y_test,Y)
print(r_sq)


plt.scatter(x_test,y_test,c='#ef5423',label="scatter plot")
plt.plot(x_test,Y,label="regression line")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

plt.show()


