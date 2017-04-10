import sklearn.linear_model.Lasso
features, labels = GetMyData()
regression = Lasso()
regression.fit(features, labels)
# Predict a label for a new point [2,4]
regression.predict([2,4])
