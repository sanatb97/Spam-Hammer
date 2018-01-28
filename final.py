import os
import numpy as np
import csv
import pickle
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix 
from sklearn import preprocessing

def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]    
    all_words = []       
    for mail in emails:    
        with open(mail,encoding="utf-8") as m:
            for i,line in enumerate(m):
                if i == 2:  #Body of email is only 3rd line of text file
                    words = line.split()
                    all_words += words
    dictionary = Counter(all_words)
    # Paste code for non-word removal here(code snippet is given below) 
    list_to_remove = list(dictionary)
    for item in list_to_remove:
        if item.isalpha() == False: 
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(100)
    return dictionary

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

# Create a dictionary of words with its frequency

train_dir = 'C:\\Users\\sanat\\Documents\\I_Hack 2018\\training'
test_dir = 'C:\\Users\\sanat\\Documents\\I_Hack 2018\\ling-spam\\test-mails'
dictionary = make_Dictionary(train_dir)

def derivative(x):
    return x * (1.0 - x)

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# Prepare feature vectors per training mail and its labels

train_matrix = extract_features(train_dir)
test_matrix = extract_features(test_dir)
res1 = train_matrix
csvfile1 = "Train.csv"
res2 = test_matrix
csvfile2 = "Test.csv"
#Assuming res is a list of lists
with open(csvfile1, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res1)

with open(csvfile2, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res2)

X = []
Y = []
X_test = []
y_test = []
# read the training data
with open('Train.csv') as f:
    for line in f:
        curr = line.split(',')
        new_curr = [1]
        for item in curr[:len(curr) - 1]:
            new_curr.append(float(item))
        X.append(new_curr)
        Y.append([float(curr[-1])])

X = np.array(X)
X = preprocessing.scale(X)      # feature scaling
Y = np.array(Y)

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

# the first 2500 out of 3000 emails will serve as training data
X_train = X
Y_train = Y

X = X_train
y = Y_train

# we have 3 layers: input layer, hidden layer and output layer
# input layer has 57 nodes (1 for each feature)
# hidden layer has 4 nodes
# output layer has 1 node

dim1 = len(X_train[0])
dim2 = 4

# randomly initialize the weight vectors
np.random.seed(1)
weight0 = 2 * np.random.random((dim1, dim2)) - 1
weight1 = 2 * np.random.random((dim2, 1)) - 1

# you can change the number of iterations
for j in range(1000):
    # first evaluate the output for each training email
    layer_0 = X_train
    layer_1 = sigmoid(np.dot(layer_0,weight0))
    layer_1 = np.array(layer_1)
    layer_2 = sigmoid(np.dot(layer_1,weight1))

    # calculate the error
    layer_2_error = Y_train - layer_2

    # perform back propagation
    layer_2_delta = layer_2_error * derivative(layer_2)
    layer_1_error = layer_2_delta.dot(weight1.T)
    layer_1_delta = layer_1_error * derivative(layer_1)

    # update the weight vectors
    weight1 += layer_1.T.dot(layer_2_delta)
    weight0 += layer_0.T.dot(layer_1_delta)
filename = open('finalized_model.sav',"wb")
pickle.dump([layer_0,weight0,weight1,dictionary],filename)
filename.close()
# evaluation on the testing data
layer_0 = X_test
layer_1 = sigmoid(np.dot(layer_0,weight0))
layer_2 = sigmoid(np.dot(layer_1,weight1))

def smn():
    
    threshold =0.75
    correct=0
    # if the output is > 0.7 5, then label as spam else no spam
    for i in range(len(layer_2)):
        current = 0
        if(layer_2[i][0] > threshold):
            current = 1
        else:
            current = 0
        if(current == y_test[i][0]):
            correct += 1

    # printing the output
    print ("threshold = ", threshold)
    print ("total = ", len(layer_2))
    print ("correct = ", correct)
    print ("accuracy = ", correct * 100.0 / len(layer_2))
    print ("*****************************")
smn()



