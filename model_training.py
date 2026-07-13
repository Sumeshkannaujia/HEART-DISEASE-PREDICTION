import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
df=pd.read_csv("heart.csv")
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
m=LogisticRegression(max_iter=1000)
m.fit(X_train,y_train)
joblib.dump(m,"model.pkl")
print("Saved model.pkl")
