## Lab 9: Machine Learning ##

import doctest
_author_ = "Randy Hucker"
_credits_ = ["Me"]
_email_ = "huckerre@mail.uc.edu"

# Table:

# Estimators   Accuracy
# 1             86.89%
# 2             80.33%  
# 3             75.41%
# 4             86.89%
# 5             81.97%
# 6             85.25%
# 7             93.44%
# 8             85.24%
# 9             86.89%
# 10            83.61%

# From this test, the best estimator seemed to be 7
# This came as a surprise for me because I assumed that a higher number of estimators
# would actually improve the accuracy.


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pandas as pd
import numpy as np
import pickle
# Modify this to your file system
heart_disease = pd.read_csv('C:/Users/randa/Downloads/heart.csv')

# Create X (Features Matrix)
X = heart_disease.drop(['target'], axis=1)

# Create Y (Labels)
Y = heart_disease['target']

clf = RandomForestClassifier(n_estimators=1)

# .2 gives 80% of the data is for training and 20% for testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

clf.fit(X_train, Y_train)
Y_preds = clf.predict(X_test)

print(clf.score(X_train, Y_train))
print(clf.score(X_test, Y_test))

print(classification_report(Y_test, Y_preds))
print("-------------------------------------")
print(confusion_matrix(Y_test, Y_preds))
print("-------------------------------------")
print(accuracy_score(Y_test, Y_preds))

np.random.seed(42)
for i in range(1, 11, 1):
    print(f"Trying model with {i} estimators...")
    clf = RandomForestClassifier(n_estimators=i).fit(X_train, Y_train)
    print(f"Model accuracy on test set: {clf.score(X_test, Y_test) * 100:.2f}%")
    print("")

pickle.dump(clf, open("Random_Forst_Model_1.pkl", "wb"))

loaded_model = pickle.load(open("Random_Forst_Model_1.pkl", "rb"))
print(loaded_model.score(X_test, Y_test)) 
