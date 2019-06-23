#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
def Main_fun():

    train = pd.read_csv("testtraining.csv")


    # In[2]:


    #train


    # In[3]:


    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import train_test_split
    train1 = train.copy()
    feature_df = train1[["NoWrd","NoSent","ADJ","ADP","ADV","CONJ","DET","NOUN","NUM","PRT","PRON", "VERB",".","X"]]
    x = np.asarray(feature_df)
    y = np.asarray(train["NScr"].astype('int'))
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 5)


    # In[4]:


    def train_model(x_train, y_train, x_test, y_test, classifier, **kwargs):
        
        
        # instantiate model
        model = classifier(**kwargs)
        
        # train model
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        #from sklearn.metrics import confusion_matrix
        #print("Confusion matrix")
        #print(confusion_matrix(y_test,y_pred))

        
        ### check accuracy and print out the results
        #fit_accuracy = model.score(x_train, y_train)
        #test_accuracy = model.score(x_test, y_test)
        
        #print(f"Train accuracy: {fit_accuracy:0.2%}")
        #print(f"Test accuracy: {test_accuracy:0.2%}")
        
        return model


    # In[5]:


    model = train_model(x_train, y_train, x_test, y_test, GaussianNB)
    #from sklearn.svm import SVC
    #model = train_model(x_train, y_train, x_test, y_test, SVC, C=0.05, kernel='linear')


    # In[6]:


    gnb = GaussianNB()


    # In[7]:


    gnb.partial_fit(x, y, np.unique(y))


    # In[8]:


    #print(gnb.predict([[499,30,30,65,43,16,47,134,3,16,59,102,65,0]]))
    final_result=gnb.predict([[499,30,30,65,43,16,47,134,3,16,59,102,65,0]])
    print(final_result)
    # In[ ]:
    #print(final_result[0])
    return final_result[0]



