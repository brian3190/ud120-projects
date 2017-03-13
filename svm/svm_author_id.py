#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
# With smaller training dataset:
# training time 0.125s vs 204.247s
# predicting time 1.248s vs 20.721s
# accuracy 0.8845(1% training data) vs 0.9841(linear) vs 0.6160(rbf)
#
####### Using full training set: Optimized RBF, comment the following two lines
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
# training time=139.307s, predicting time=15.411s, accuracy=0.9909



# low C, straighter boundary
# high C, better accuracy, more complex boundary
# C=10000.0, training time=0.124s, predicting time=1.218, accuracy=0.8925
# C=1000.0, training time=0.126s, predicting time=1.359s, accuracy=0.8214
# C=100.0, training time=0.136s, predicting time=1.421s, accuracy=0.6160
# C=10.0, training time=0.153s , predicting time=1.483s, accuracy=0.6160

from sklearn.svm import SVC
clf = SVC(kernel='rbf', C=10000.0)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:",round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predicting time:",round(time()-t1, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print accuracy


print sum(pred)


#########################################################
