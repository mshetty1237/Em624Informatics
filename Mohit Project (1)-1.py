#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from wordcloud import WordCloud
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,roc_curve,classification_report


# In[ ]:





# In[3]:


df2 = pd.read_csv("chatgpt.csv",encoding ="ISO-8859-1",engine="python")


# In[4]:


df3 = pd.read_csv("chatgpt1 (1).csv",encoding ="ISO-8859-1",engine="python")


# In[5]:


df4 = pd.read_csv("file.csv",encoding ="ISO-8859-1",engine="python")


# ### DF4( Consists of both Tweets and labels)
# 

# In[6]:


df4.labels.value_counts()


# In[7]:


df4.labels.value_counts().plot(kind='barh')


# In[8]:


df4.labels.value_counts().plot(kind='pie')


# In[18]:


plt.hist(df4['labels'])


# ### Performing Sentiment Analysis for df 2

# In[9]:



from textblob import TextBlob
# Define a function to perform sentiment analysis on each row of text data
def get_sentiment(row):
    text = row['tweet']
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Apply the sentiment analysis function to the dataframe and create a new column for sentiment scores
df2['sentiment_score'] = df2.apply(get_sentiment, axis=1)

# Interpret the sentiment scores and add a new column for sentiment labels
df2['sentiment_label'] = df2['sentiment_score'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))

# Print the updated dataframe
print(df2)


# In[10]:


df2.sentiment_label.value_counts()


# In[11]:


df2['sentiment_label'].value_counts().plot(kind='barh')


# In[12]:


#df2['sentiment_score'].value_counts().plot(kind='barh')


# In[13]:


df2.sentiment_label.value_counts().plot(kind='pie')


# In[21]:


sns.pairplot(df2,hue = "sentiment_label",palette='bwr')


# ### Performing Sentiment analysis df3

# In[14]:


def get_sentiment(row):
    text = row['Text']
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Apply the sentiment analysis function to the dataframe and create a new column for sentiment scores
df3['sentiment_score'] = df3.apply(get_sentiment, axis=1)

# Interpret the sentiment scores and add a new column for sentiment labels
df3['sentiment_label'] = df3['sentiment_score'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))

print(df3)


# In[15]:


df3.sentiment_label.value_counts()


# In[16]:


df3['sentiment_label'].value_counts().plot(kind='barh')


# In[17]:


df3.sentiment_label.value_counts().plot(kind='pie')


# In[20]:


sns.pairplot(df3,hue = "sentiment_label",palette='bwr')


# In[ ]:





# In[ ]:





# In[ ]:




