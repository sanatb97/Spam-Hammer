import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix 
import pickle

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
          if (i==2):
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

train_dir = "C:\\Users\\sanat\\Documents\\I_Hack 2018\\training"
dictionary = make_Dictionary(train_dir)
#print(dictionary)

# Prepare feature vectors per training mail and its labels

train_labels = np.zeros(19998)
train_labels[10000:19997] = 1
train_matrix = extract_features(train_dir)
"""print(train_matrix[0])
print(train_matrix[1000])
print(train_matrix[8000])"""

# Training SVM and Naive bayes classifier

model1 = MultinomialNB()
model2 = LinearSVC()
model1.fit(train_matrix,train_labels)
model2.fit(train_matrix,train_labels)
filename1="model1.sav"
filename2="model2.sav"
pickle.dump(model1, open(filename1, 'wb'))
pickle.dump(model2, open(filename2, 'wb'))

# Test the unseen mails for Spam
test_dir = 'C:\\Users\\sanat\\Documents\\I_Hack 2018\\ling-spam\\test-mails'
test_matrix = extract_features(test_dir)
test_labels = np.zeros(260)
test_labels[130:260] = 1
result1 = model1.predict(test_matrix)
result2 = model2.predict(test_matrix)
print("Using Naive Bayes Multinomial Classifier:")
print(confusion_matrix(test_labels,result1))
print("Using SVM:")
print(confusion_matrix(test_labels,result2))
