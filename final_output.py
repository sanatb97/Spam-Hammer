# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 08:00:14 2018

@author: sanat
"""

import os
import numpy as np
import csv
import pickle
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix 
from sklearn import preprocessing
import pickle
filename="C:\\Users\\sanat\\Documents\\I_Hack 2018\\finalized_model.sav"

loaded_model = pickle.load(open(filename, 'rb'))
X_test=[]
y_test=[]
dictionary=loaded_model[3]
def extract_features(mail_dir): 
    files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files),100))
    docID = 0;
    for fil in files:
      with open(fil,encoding="utf-8") as fi:
        for i,line in enumerate(fi):
          if i == 2:
            words = line.split()
            for word in words:
              wordID = 0
              for i,d in enumerate(dictionary):
                if d[0] == word:
                  wordID = i
                  features_matrix[docID,wordID] = words.count(word)
        docID = docID + 1     
    return features_matrix
test_dir = 'C:\\Users\\sanat\\Documents\\I_Hack 2018\\final test'
test_matrix = extract_features(test_dir)
res2 = test_matrix
csvfile2 = "Test.csv"
with open(csvfile2, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res2)
with open('Test.csv') as f:
    for line in f:
        curr = line.split(',')
        new_curr = [1]
        for item in curr[:len(curr) - 1]:
            new_curr.append(float(item))
        X_test.append(new_curr)
        y_test.append([float(curr[-1])])


X_test = np.array(X_test)
X_test = preprocessing.scale(X_test)      # feature scaling
y_test = np.array(y_test)

#result = loaded_model.score(X_test, Y_test)





#print(loaded_model)
layer_0=loaded_model[0]
weight_0=loaded_model[1]
weight_1=loaded_model[2]
layer_0 = X_test
layer_1 = sigmoid(np.dot(layer_0,weight0))
layer_2 = sigmoid(np.dot(layer_1,weight1))

def smn():
    
    threshold =0.75
    ham=0
    spam=0
    files = os.listdir(test_dir)
    spaml=[]
    haml=[]
    destination = "C:\\Users\\sanat\\Documents\\I_Hack 2018\\results\\"
    # if the output is > 0.75, then label as spam else no spam
    for i in range(len(layer_2)):
        
        if(layer_2[i][0] > threshold):
            spaml.append(files[i])
            spam=spam+1
        else:
            haml.append(files[i])
            ham=ham+1
        

    # printing the output
    #print ("threshold = ", threshold)
    print ("Total number of emails  = ", len(layer_2))
    print ("HAM emails = ", len(haml))
    fp = open(destination+"hamMails.txt","w")
    fp.write(str(len(haml))+"\n")
    for h in haml:
        fp.write(h+"\n")
    fp.close()
    
    fp = open(destination+"spamMails.txt","w")
    print("SPAM emails = ",len(spaml))
    fp.write(str(len(spaml))+"\n")
    for s in spaml:
        fp.write(s+"\n")
    fp.close()
    
    #print ("Accuracy = ", correct * 100.0 / len(layer_2),"%")
    print ("*****************************")
smn()
