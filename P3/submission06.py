# -*- coding: utf-8 -*-
"""
Autor:
    Jorge Casillas y Daniel Molina
Fecha:
    Noviembre/2021
Contenido:
    Uso simple de LinearRegresion para competir en DrivenData:
       https://www.drivendata.org/competitions/66/flu-shot-learning/
    Inteligencia de Negocio
    Grado en Ingeniería Informática
    Universidad de Granada
"""

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

'''
print((data_y['h1n1_vaccine'] == 1).sum())
print((data_y['seasonal_vaccine'] == 1).sum())
print(((data_y['seasonal_vaccine'] == 1) & (data_y['h1n1_vaccine'] == 1)).sum())'''


print("LLEGO")
#se quitan las columnas que no se usan
data_x.drop(labels=['respondent_id'], axis=1,inplace = True)
data_x_tst.drop(labels=['respondent_id'], axis=1,inplace = True)
data_y.drop(labels=['respondent_id'], axis=1,inplace = True)
data_all_features = pd.concat([data_x, data_x_tst])
print("LLEGO 2")

from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
mask = data_x.isnull()
# import ipdb; ipdb.set_trace()

labels = {}
imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
data_x_tmp = data_x.astype(str)
# Uso SimpleImputer para "eliminar los nulos", como elimina los nombres de las columnas los vuelvo a poner
cols = data_x_tmp.columns
data_x_tmp = pd.DataFrame(imp.fit_transform(data_x_tmp))
data_x_tmp.columns = cols
print("LLEGO 3")

# Aprendo las etiquetas
for col in data_all_features.columns:
    labels[col] = LabelEncoder()
    labels[col].fit(data_all_features[col].astype(str))

print("LLEGO 4")
# Aplico el etiquetado
for col in data_x_tmp.columns:
    data_x_tmp[col] = labels[col].transform(data_x_tmp[col])

print("LLEGO 4B")
# Conjunto final de aprendizaje
X = data_x_tmp
y = data_y.values

data_x_tmp = data_x_tst.astype(str)
data_x_tmp = pd.DataFrame(imp.transform(data_x_tmp))
data_x_tmp.columns = cols
print("LLEGO 5")
# Aplico el mismo etiquetado con los valores de test
for col in data_x_tmp.columns:
    data_x_tmp[col] = labels[col].transform(data_x_tmp[col])

print("LLEGO 6")
# Conjunto final de test
X_tst = data_x_tmp.values
print("HASTA DEF DE FUNC")

#------------------------------------------------------------------------
# Validación cruzada con KFold y control de la aleatoriedad fijando la semilla
skf = KFold(n_splits=5, shuffle=True, random_state=123456)

from sklearn.metrics import f1_score

def validacion_cruzada(modelo, X, y, cv):
    measures = []
    t_g = time.time()
    print("ENTRO EN FUNCION")

    for train, test in cv.split(X, y):
        X_train = X.loc[train, :]
        X_test = X.loc[test, :]
        y_train = y.loc[train,:].values
        y_test = y.loc[test, :].values
        t = time.time()
        print("VOY A HACER FIT")
        #peso = [0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 1, 1, 0.75, 0.75, 0.75, 1, 1, 1, 0.75, 1, 1, 0.75, 1, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75]
        model = modelo.fit(X_train,y_train)
        tiempo = time.time() - t
        print("VOY A HACER PREDICT")
        preds = model.predict_proba(X_test)
        y_preds = pd.DataFrame(
            {
                "h1n1_vaccine": preds[0][:, 1],
                "seasonal_vaccine": preds[1][:, 1],
            },
            index = y.loc[test,:].index
        )
        measure = roc_auc_score(y_test, y_preds)
        print("AUC score (val): {:.4f}, tiempo: {:6.2f} segundos".format(measure, tiempo))
        measures.append(measure)

    tiempo_g = time.time() - t_g
    # Medida promedio final
    print("Average AUC score (val): {:.4f}, tiempo: {:6.2f} segundos".format(np.mean(measures), tiempo_g))
    return modelo

#------------------------------------------------------------------------


from sklearn.multioutput import MultiOutputClassifier
from catboost import CatBoostClassifier, EFstrType, Pool

print("------ RandomForestClassifier...")

#pesos = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.1, 0.1]
# feature_weights=pesos,
# Creo el modelo normal
# lr = LogisticRegression(penalty="l2", C=1, max_iter=300)
#rf = RandomForestClassifier(class_weight="balanced", n_estimators=1200, min_samples_split=35, min_samples_leaf=3, n_jobs=2)
rf = CatBoostClassifier(iterations=70, depth=6, learning_rate= 0.31, loss_function='MultiClass')
# Multioutput classifier, para indicar que tiene que aprender varias etiquetas a la vez
multi = MultiOutputClassifier(rf)
# Aplica validación cruzada y devuelve el modelo
clf1 = validacion_cruzada(multi,X,data_y,skf)

# Aprendo con todos los ejemplos
clf1 = clf1.fit(X,data_y)

# Miro importancia atributos
'''feature_names = [f"feature {i}" for i in range(X.shape[1])]
forest = clf1

feat_impts = [] 
for cl in forest.estimators_:
    feat_impts.append(cl.feature_importances_)

feat_impts = np.mean(feat_impts, axis=0)

importances = feat_impts
std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)

forest_importances = pd.Series(importances, index=X.columns)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()
plt.savefig("atributos.eps", format="eps")'''
                       
# Aplico probabilidad
preds = clf1.predict_proba(X_tst)
df_submission = pd.read_csv('submission_format.csv')

# Reformateo la salida
y_test_preds = pd.DataFrame(
            {
                "h1n1_vaccine": preds[0][:, 1],
                "seasonal_vaccine": preds[1][:, 1],
            },
            index = df_submission.index
        )

# Modifico las columnas con las predichas
df_submission['h1n1_vaccine'] = y_test_preds.h1n1_vaccine
df_submission['seasonal_vaccine'] = y_test_preds.seasonal_vaccine
# Escribo el fichero de salida
df_submission.to_csv("submission_07.csv", index=False)
