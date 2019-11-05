# -*- coding: utf-8 -*-
"""
clima_dt.py: Código para estudo de árvore de decisão

@author: Prof. Hugo de Paula
@contact: hugo@pucminas.br

@date	  15 Maio 2017
@version 1.0

"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn import tree


Internet = pd.read_excel('../Datasets/Atividade 3 - Bases.xlsx', sheetname=0) 
print("\nDimensões: {0}".format(Internet.shape))
print("\nCampos: {0}".format(Internet.keys()))
print(Internet.describe(), sep='\n')

X_dict = Internet.iloc[:,4:9].T.to_dict().values()
vect = DictVectorizer(sparse=False)
X_train = vect.fit_transform(X_dict)

le = LabelEncoder()
y_train = le.fit_transform(Internet.iloc[:,(Internet.shape[1] - 1)])

tree_nominal = DecisionTreeClassifier(random_state=0)
tree_nominal = tree_nominal.fit(X_train, y_train)
print("Acurácia:", tree_nominal.score(X_train, y_train))

Train_predict = tree_nominal.predict(X_train)
print("Acurácia de previsão:", accuracy_score(y_train, Train_predict))
print(classification_report(y_train, Train_predict))


with open("Internet.dot", 'w') as f:
     f = tree.export_graphviz(tree_nominal, out_file=f, 
                              feature_names=vect.feature_names_, 
                              class_names=["Early Adopter", "Early Majority","Innovator","Late Majority"])
     
# dot -Tpdf nominal.dot -o nominal.pdf
     
tree_entropy = DecisionTreeClassifier(random_state=0, criterion = "entropy")
tree_entropy = tree_entropy.fit(X_train, y_train)


Train_predict = tree_entropy.predict(X_train)
print("Acurácia de previsão (entropia):", accuracy_score(y_train, Train_predict))
print(classification_report(y_train, Train_predict))


with open("Internet_entropy.dot", 'w') as f:
     f = tree.export_graphviz(tree_entropy, out_file=f, 
                              feature_names=vect.feature_names_, 
                              class_names=["Early Adopter", "Early Majority","Innovator","Late Majority"])
     