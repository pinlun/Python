#%%
import pandas as pd
import numpy as np
#tranpose data
#train data
data = pd.read_csv("/Users/pinlunhuang/Desktop/PinTech/hw1/train.csv",encoding='utf8')
data = data.drop(['測站'], axis=1)
train = pd.melt(data, id_vars=['日期','測項']) 
train['value'] = [i if i!='NR' else 0 for i in train['value']]
train['value']=train['value'].astype(float)
train = train.pivot_table(values='value', index=['日期','variable'], columns="測項")

#test data
test = pd.read_csv("/Users/pinlunhuang/Desktop/PinTech/hw1/test.csv",encoding='utf8', header=None)
test.columns = ["測站","測項", '0','1','2','3','4','5','6','7','8']
test = pd.melt(test, id_vars=["測站","測項"]) 
test['value'] = [i if i!='NR' else 0 for i in test['value']]
test['value'] = test['value'].astype(float)
test = test.pivot_table(values='value', index=['測站','variable'], columns="測項")


#use sklearn:linear regression find parameters
from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = train.loc[:,['AMB_TEMP', 'CH4', 'CO', 'NMHC', 'NO', 'NO2', 'NOx', 'O3', 'PM10', 'PM2.5', 'RAINFALL', 'RH', 'SO2', 'THC', 'WD_HR', 'WIND_DIREC', 'WIND_SPEED', 'WS_HR']]
train_y = train.loc[:,'PM2.5']
test_x = test.loc[:,['AMB_TEMP', 'CH4', 'CO', 'NMHC', 'NO', 'NO2', 'NOx', 'O3', 'PM10', 'PM2.5', 'RAINFALL', 'RH', 'SO2', 'THC', 'WD_HR', 'WIND_DIREC', 'WIND_SPEED', 'WS_HR']]
test_y = test.loc[:,'PM2.5']
regr.fit(train_x, train_y)
predict_y = regr.predict(test_x)
print('Coefficients: \n', regr.coef_)

#gradient descent
def gradient_descent(x, y,theta, iterations, learning_rate):
    loss = np.zeros(iterations)
    for i in range(iterations):
        gradient_parameter = sum(2*np.dot( (y-( np.dot(x, theta)+constant )), -x))
        theta = theta - learning_rate*gradient_parameter
        loss[i] = np.sum((y- (np.dot(x, theta)+constant))**2)/(2 * len(y))
    
    return theta, loss


theta = [9.57567359e-1, 2.12971134e-13, -1.18948905e-14, -3.03888859e-14,
  3.72618603e-15,  7.11930515e-15, -5.82867088e-15,  4.71844785e-16,
  1.53089347e-16,  1.00000000e+00, -1.73472348e-18,  1.45716772e-16,
 -1.19695920e-16,  1.56243291e-14, -8.67361738e-18, -5.20417043e-17,
  1.13017234e-15, -4.44089210e-16]
theta, loss = gradient_descent(train_x, train_y, theta ,1000, 0.000000000001)


#plot the Error v.s Training Epoch
import matplotlib.pyplot as plt
fig, ax = plt.subplots()  
ax.plot(np.arange(1000), loss, 'r')  
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Error vs. Training Epoch')

#predict and write into csv
test_y = np.dot(test_x,theta)

with open('/Users/pinlunhuang/Desktop/PinTech/hw1/predictions.csv','w') as f:
        f.write('id,value\n')
        for i in range(len(test_y)):
            f.write('id_'+str(i)+','+str(round(test_y[i],2))+'\n')
