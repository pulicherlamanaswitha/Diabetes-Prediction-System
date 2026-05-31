import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
data=pd.read_csv(r"C:\Users\pulic\Documents\ML project\diabetes.csv")
df=pd.DataFrame(data)
x=df[['Glucose','BMI']]
y=df['Outcome']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=23)
model=LogisticRegression()
model1=RandomForestClassifier()
model.fit(x_train,y_train)
# test_data=list(map(float,input("enter glucose and bmi with space").split()))
# testing=pd.DataFrame([test_data],columns=['Glucose','BMI'])
# y_pred=model.predict(x_test)
# print("accuracy:",accuracy_score(y_test,y_pred))
# final_outcome=model.predict(testing)
# print("having disease" if final_outcome==1 else "No disease")
import joblib
joblib.dump(model,'diabetes_model.pkl')
print("model saved")