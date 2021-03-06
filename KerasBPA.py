# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 18:27:59 2018

@author: Shrinath
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('AndaData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 5:6].values

print(len(dataset))
"""
# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_1.fit_transform(X[:, 2])

onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X=X[:,1:]
"""
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
"""
k=0
for i in range(0,104):
    for j in range(0,5):
        out[i,j]=dataset[2,k++]

"""

"""
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
"""
#Feature scaling
from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
X=sc.fit_transform(X)
y=sc.fit_transform(y)




#importing keras
import keras
from keras.models import Sequential
from keras.layers import Dense

#initailizing the layer
classifier = Sequential()

#Adding the input layer and the First hidden layer
classifier.add(Dense(output_dim=3,init='uniform',activation= 'relu',input_dim=5))

#Adding the second hidden layer
classifier.add(Dense(output_dim=3,init='uniform',activation= 'relu'))

#Adding the ouput layer
classifier.add(Dense(output_dim=1,init='uniform',activation= 'sigmoid'))

#Compiling the ANN
classifier.compile(optimizer= 'adam',loss='mean_squared_logarithmic_error',metrics=['accuracy'])

#Fitting the ANN to the Training Set
classifier.fit(X_train,y_train,batch_size=1,epochs=100) 

#Predicting the test set result
y_pred=classifier.predict(X_test)

#y_pred=(y_pred>0.5)

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)


#Predicting the test set result
y_pred=classifier.predict(X_test)
y_pred=sc.inverse_transform(y_pred)
y_test=sc.inverse_transform(y_test)

#visualing the result
plt.plot(y_test,color= 'red',label='Real Actual Value')
plt.plot(y_pred,color= 'blue',label='Predicted Value')
plt.title('RainFall Prediction')
plt.xlabel('Year')
plt.ylabel('Rainfall')
plt.legend()
plt.show()

