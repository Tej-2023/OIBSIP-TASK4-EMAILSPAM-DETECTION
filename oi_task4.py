

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

data=pd.read_csv('spam.csv',encoding='ISO-8859-1')
data

data.columns

data.info()

data.isnull().sum()

data.isnull().mean()*100

data.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True)
data

data['text length']=data['v2'].apply(len)

data

sns.boxplot(x='v1',y='text length',data=data)
plt.xlabel('Email type')
plt.ylabel('Text length')
plt.title('Box plot with Text length with Spam/Ham Differentiation')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(data['v2'], data['v1'], test_size=0.2, random_state=42)

vectorizer=CountVectorizer()
X_train_vectorized=vectorizer.fit_transform(X_train)
X_test_vectorized=vectorizer.transform(X_test)

classifier=MultinomialNB()
classifier.fit(X_train_vectorized,y_train)

y_pred=classifier.predict(X_test_vectorized)

accuracy=accuracy_score(y_test,y_pred)
conf_matrix=confusion_matrix(y_test,y_pred)
class_report=classification_report(y_test,y_pred)

print(f"Accuracy: {accuracy}")
print("Confusion Matrix:",conf_matrix)
print("Classification Report:",class_report)
