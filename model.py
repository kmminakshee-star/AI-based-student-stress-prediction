import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('student_mental_health_burnout.csv')

df = df.select_dtypes(include=['int64','float64'])

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

y = pd.cut(y, bins=3, labels=[0,1,2])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pickle.dump(model, open('model.pkl','wb'))

print(" Model trained")