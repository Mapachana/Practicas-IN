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

from os import name
import pandas as pd
import numpy as np
import time
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, auc, roc_auc_score
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

'''
lectura de datos
'''
#los ficheros .csv se han preparado previamente para sustituir ,, y "Not known" por NaN (valores perdidos)
data_x = pd.read_csv('training_set_features.csv')
data_y = pd.read_csv('training_set_labels.csv')
data_x_tst = pd.read_csv('test_set_features.csv')


print("LLEGO")
#se quitan las columnas que no se usan
data_x.drop(labels=['respondent_id'], axis=1,inplace = True)
data_x_tst.drop(labels=['respondent_id'], axis=1,inplace = True)
data_y.drop(labels=['respondent_id'], axis=1,inplace = True)
#data_all_features = pd.concat([data_x, data_x_tst])
print("LLEGO 2")

from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
mask = data_x.isnull()
# import ipdb; ipdb.set_trace()

# Vamos a imputar valores con cabeza
#data_x.drop(columns=['health_insurance'], inplace=True)
#data_x_tst.drop(columns=['health_insurance'], inplace=True)

no_empleado = "no empleado"
no_procede = "no procede"
empleado_healthcare_industry = "fcxhlnwr"
empleado_healthcare_occupation = "cmhcxjea"

#mask_no_empleado_health = (data_x['health_worker'] == 1) & (data_x['employment_status'] == "Unemployed") & (data_x['employment_industry'].isna())
data_x_tmp = data_x

#print(data_x_tmp["employment_industry"])

#mask = (data_x["health_worker"] == 1) &  data_x["employment_status"].isna() 
#data_x_tmp.loc[mask, "employment_status"] = "Employed" 

#mask = (data_x_tst["health_worker"] == 1) &  data_x_tst["employment_status"].isna() 
#data_x_tst.loc[mask, "employment_status"] = "Employed" 

#mask =  ~data_x_tmp["employment_status"].isna() 
#print(mask)
#print(mask.shape)
#print(data_y.shape)

#data_y = data_y.mask(mask)
#data_x_tmp = data_x_tmp.mask(mask)
#data_x_tmp.loc[mask, "employment_status"] = "unknown"

#mask = data_x_tst["employment_status"].isna() 
#data_x_tst.drop(data_x_tst[mask].index, inplace=True)

#data_x_tst.loc[mask, "employment_status"] = "unknown"

for hwdata, col in zip([empleado_healthcare_industry, empleado_healthcare_occupation], ["employment_industry", "employment_occupation"]):
    #mask = (data_x['health_worker'] == 1) & (data_x['employment_status'] == "Unemployed") & (data_x[col].isna())
    #data_x_tmp.loc[mask, col] = hwdata 

    #mask = (data_x_tst['health_worker'] == 1) & (data_x_tst['employment_status'] == "Unemployed") & (data_x_tst[col].isna())
    #data_x_tst.loc[mask, col] = hwdata 

    '''mask = (data_x["health_worker"] == 1) & (data_x["employment_status"] == "Employed") & (data_x[col].isna())
    data_x_tmp.loc[mask, col] = hwdata

    mask = (data_x_tst["health_worker"] == 1) & (data_x_tst["employment_status"] == "Employed") & (data_x_tst[col].isna())
    data_x_tst.loc[mask, col] = hwdata

    mask = (data_x['employment_status'] == "Unemployed") & (data_x[col].isna())
    data_x_tmp.loc[mask, col] = no_empleado

    mask = (data_x_tst['employment_status'] == "Unemployed") & (data_x_tst[col].isna())
    data_x_tst.loc[mask, col] = no_empleado

    mask = (data_x['employment_status'] == "Not in Labor Force") & (data_x[col].isna())
    data_x_tmp.loc[mask, col] = no_procede

    mask = (data_x_tst['employment_status'] == "Not in Labor Force") & (data_x_tst[col].isna())
    data_x_tst.loc[mask, col] = no_procede

    mask = data_x_tmp[col].isna()
    data_x_tmp.loc[mask, col] = "unknown"
    mask = data_x_tst[col].isna()
    data_x_tst.loc[mask, col] = "unknown"'''
    """
    most_frequent = data_x_tmp[col].value_counts().index
    selected = 0

    #print(data_x_tmp[col].value_counts())
    #print(data_x_tmp[col].isna().sum())

    while most_frequent[selected] == no_procede or most_frequent[selected] == no_empleado or most_frequent[selected] == hwdata:
        selected += 1
        
    data_x_tmp[col].fillna(most_frequent[selected], inplace=True)
    data_x_tst[col].fillna(most_frequent[selected], inplace=True)
    """
    pass

#print(data_x_tmp["employment_occupation"].isna().sum())

variables_categoricas = ['age_group',
       'education', 'race', 'sex', 'income_poverty', 'marital_status',
       'rent_or_own', 'employment_status', 'hhs_geo_region', 'census_msa',
       'employment_industry',
       'employment_occupation', 'behavioral_antiviral_meds', 'behavioral_avoidance', 'behavioral_face_mask',
       'behavioral_wash_hands', 'behavioral_large_gatherings', 'behavioral_outside_home', 'behavioral_touch_face',
       'doctor_recc_h1n1', 'doctor_recc_seasonal', 'chronic_med_condition', 'child_under_6_months', 'health_worker', 'health_insurance']

variables_numericas = np.setdiff1d(data_x.columns,variables_categoricas)


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(data_x[variables_numericas])
data_x[variables_numericas] = scaler.transform(data_x[variables_numericas])
data_x_tst[variables_numericas] = scaler.transform(data_x_tst[variables_numericas])
print(data_x)



data_all_features = pd.concat([data_x_tmp, data_x_tst])


labels = {}
imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
data_x_tmp = data_x_tmp.astype(str)

# Vamos a imputar valores con cabeza
#print(data_x_tmp)
#print(data_x_tmp.columns)

#print(data_x_tmp)
# Uso SimpleImputer para "eliminar los nulos", como elimina los nombres de las columnas los vuelvo a poner
cols = data_x_tmp.columns
data_x_tmp = pd.DataFrame(imp.fit_transform(data_x_tmp))
data_x_tmp.columns = cols
print("LLEGO 3")

#print(data_x_tmp)

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

#print(X)
data_x_tmp = data_x_tst.astype(str)
data_x_tmp = pd.DataFrame(imp.transform(data_x_tmp))
data_x_tmp.columns = cols
print("LLEGO 5")
# Aplico el mismo etiquetado con los valores de test
for col in data_x_tmp.columns:
    data_x_tmp[col] = labels[col].transform(data_x_tmp[col])

print("LLEGO 6")
# Conjunto final de test
X_tst = data_x_tmp
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

        #print(X_test['employment_status'])
        #print((X_test['employment_status'] == 0).sum())
        t = time.time()
        print("VOY A HACER FIT")
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
from lightgbm import LGBMClassifier, Dataset

print("------ LightGBMClassifier...")

# Creo el modelo normal
# lr = LogisticRegression(penalty="l2", C=1, max_iter=300)
#rf = RandomForestClassifier(class_weight="balanced", n_estimators=1200, min_samples_split=35, min_samples_leaf=3, n_jobs=2)
#rf = CatBoostClassifier(iterations=70, depth=6, learning_rate= 0.31, loss_function='MultiClass')
#aux.save_model('prueba.txt')

'''variables_categoricas = ['age_group',
       'education', 'race', 'sex', 'income_poverty', 'marital_status',
       'rent_or_own', 'employment_status', 'hhs_geo_region', 'census_msa',
       'employment_industry',
       'employment_occupation']'''



X = X.astype(float)
X_tst = X_tst.astype(float)
X[variables_categoricas] = X[variables_categoricas].astype("category")
X_tst[variables_categoricas] = X_tst[variables_categoricas].astype("category")
#print("COMPRUEBA TIRPO")
#print(X.dtypes)
"""
variables_categoricas = ['age_group',
       'education', 'income_poverty',
       'rent_or_own', 'employment_status']


data_x_tmp.drop(columns=['hhs_geo_region', 'census_msa', 'race', 'sex', 'marital_status', 'employment_industry', 'employment_occupation'], inplace=True)
X.drop(columns=['hhs_geo_region', 'census_msa', 'race', 'sex', 'marital_status', 'employment_industry', 'employment_occupation'], inplace=True)

encoder = OneHotEncoder()
encoder.fit(data_x_tmp[variables_categoricas])
print("!!!!")
print(encoder.categories_)
onehots = pd.DataFrame(encoder.transform(data_x_tmp[variables_categoricas]).toarray())
print(onehots.shape)
#onehots2 = pd.DataFrame(encoder.transform(data_x_tmp["race"]).toarray())
#print(onehots2)
xnuevo = X.drop(columns=variables_categoricas)
X = xnuevo.join(onehots)
del xnuevo, onehots 
"""



#name_var_cat = ["name:"+v for v in variables_categoricas]
#rf = LGBMClassifier(boosting_type="goss", top_rate=0.42, max_depth=0, subsample_for_bin=3000, n_estimators=2500, learning_rate=0.005, num_leaves=29, min_child_samples=100, path_smooth=100)
rf = LGBMClassifier(boosting_type="goss", top_rate=0.42, max_depth=0, subsample_for_bin=3000, n_estimators=2500, learning_rate=0.005, num_leaves=29, min_child_samples=100, path_smooth=10)

# Multioutput classifier, para indicar que tiene que aprender varias etiquetas a la vez
multi = MultiOutputClassifier(rf)
# Aplica validación cruzada y devuelve el modelo
clf1 = validacion_cruzada(multi,X,data_y,skf)

# Aprendo con todos los ejemplos
clf1 = clf1.fit(X,data_y)
                       
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
df_submission.to_csv("submission_15.csv", index=False)
