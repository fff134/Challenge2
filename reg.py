import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn import svm
from sklearn import preprocessing
from sklearn.externals import joblib


data = np.loadtxt('all_wells_lim_test.csv', delimiter=',')
X = np.concatenate((data[:,0:3], data[:,4:]), axis = 1)
X = X.astype(float)
y = data[:,3]
y = y.astype(float)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Implement Linear SVR
clf = svm.SVR(kernel='linear', cache_size=1000, verbose = 2)
clf.fit(X_train, y_train)

# Mean square error of Linear SVR (Takes longer 20 mins +)
y_res = clf.predict(X_test)
mean_squared_error(y_test, y_res)

# Implement Ridge Regression
reg = linear_model.Ridge (alpha = 2)
reg.fit(X_train, y_train)

# Mean square error of Ridge Regression (Works better)
y_res = reg.predict(X_test)

# Measures the average of the squares of the errors
mean_squared_error(y_test, y_res)

# Indicates the proportion of the variance in the dependent variable that 
# is predictable from the independent variable
r2_score(y_test, y_res)  

# Measure how close forecasts or predictions are to the eventual outcomes
mean_absolute_error(y_test, y_res)

joblib.dump(clf, 'linearsvr50000.pkl') 


print y_res

