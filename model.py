import numpy as np
import pandas as pd

df = pd.read_csv("data/winequality-red.csv")

df["quality"] = df["quality"].map({
    3: "Low", 4: "Low",
    5: "Medium", 6: "Medium",
    7: "High", 8: "High"
})

X = df.drop("quality", axis=1)
y = df["quality"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train_scaled)

import pickle
pickle.dump(rf, open("models/rf2.pkl", "wb"))