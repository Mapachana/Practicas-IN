import pandas as pd
import numpy as np
import time
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, auc, roc_auc_score
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier

'''
lectura de datos
'''
#los ficheros .csv se han preparado previamente para sustituir ,, y "Not known" por NaN (valores perdidos)
data_x = pd.read_csv('training_set_features.csv')
data_y = pd.read_csv('training_set_labels.csv')
data_x_tst = pd.read_csv('test_set_features.csv')

print((data_y['h1n1_vaccine'] == 1).sum())
print((data_y['seasonal_vaccine'] == 1).sum())
print(((data_y['seasonal_vaccine'] == 1) & (data_y['h1n1_vaccine'] == 1)).sum())

print("HAGO SMOTE")
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import CountVectorizer

df1 = data_x.iloc[:,:22]
df2 = data_x.iloc[:,22:31]
df3 = data_x.iloc[:,31:-2]
df4 = data_x.iloc[:,-2:]


df1 = pd.concat((df1, df3), axis=1)
df2 = pd.concat((df2, df4), axis=1)

vectorizer = CountVectorizer()
df2 = df2.astype(str)
vectorizer.fit(df2.values.ravel())
df2=vectorizer.transform(df2.values.ravel())
#X_test=vectorizer.transform(X_test.values.ravel())
df2=df2.toarray()
#X_test=X_test.toarray()
print("yeah")
#oversample = SMOTE()
#data_x, data_y = oversample.fit_resample(data_x, data_y['h1n1_vaccine'])

#data_x = pd.DataFrame(data_x)

sm = SMOTE(random_state = 42)
X_train_oversampled, y_train_oversampled = sm.fit_resample(data_x, data_y['h1n1_vaccine'])
data_x = pd.DataFrame(X_train_oversampled, columns=data_x.columns)


print((data_y['h1n1_vaccine'] == 1).sum())
print((data_y['seasonal_vaccine'] == 1).sum())
print(((data_y['seasonal_vaccine'] == 1) & (data_y['h1n1_vaccine'] == 1)).sum())