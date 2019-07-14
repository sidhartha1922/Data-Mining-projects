#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np  
import pandas as pd  


# In[3]:


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
iris_data = pd.read_csv(url, names=colnames)  


# In[61]:


train=iris_data.drop('Class',axis=1)
label=iris_data['Class']


# In[31]:


from sklearn import svm
mymodel=svm.SVC(kernel="rbf")
mymodel.fit(train,label)

  


# In[32]:


test=train[:5]


# In[58]:


# prediction on training data
prediction=mymodel.predict(train)


# In[53]:


# custom prediction
data = {'sepal-length':[6.1], 'sepal-width':[2.2],'petal-length':[4.6],'petal-width':[1.5]}
data


# In[54]:


df=pd.DataFrame(data)


# In[55]:


df


# In[56]:


mymodel.predict(df)


# In[59]:


from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(label, prediction))  
print(classification_report(label, prediction))  


# In[ ]:




