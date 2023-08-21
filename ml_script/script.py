from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

iris = datasets.load_iris()
X, y = iris.data, iris.target
clf = RandomForestClassifier()
clf.fit(X,y)

with open('iris_model.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)


