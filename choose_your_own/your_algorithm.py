#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

def run_classifier(clf, features, labels, name):
    from sklearn.metrics import accuracy_score
    from time import time
    t0 = time()
    clf.fit(features_train, labels_train)
    print name, "training time: ", round(time() - t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print name, "prediction time: ", round(time() - t0, 3), "s"

    accuracy = accuracy_score(labels_test, pred)

    print accuracy

    try:
        prettyPicture(clf, features_test, labels_test, name)
    except NameError:
        pass

from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='brute', leaf_size=50, p=2, metric='minkowski', metric_params=None, n_jobs=1)
run_classifier(clf, features_train, labels_train, "K Nearest Neighbors")

clf = AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm='SAMME', random_state=None)
run_classifier(clf, features_train, labels_train, "Adaboost")

clf = RandomForestClassifier(n_estimators=50, criterion='gini', max_depth=None, min_samples_split=10, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0, warm_start=False, class_weight=None)
run_classifier(clf, features_train, labels_train, "Random Forest")



