import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, accuracy_score


df = pd.read_csv('loan_data.csv')
colnames = df.columns.tolist()
predictors = colnames[:-1]
target = colnames[-1]
X = df[predictors]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
model = RandomForestClassifier(n_estimators=10 ,random_state=0)
model.fit(X_train, y_train)
preds = model.predict(X_test)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
    print('Model has been serialized')