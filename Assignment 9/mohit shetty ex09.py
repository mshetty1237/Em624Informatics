#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Read the data from the CSV file
data = pd.read_csv('REG_CAP_Spring22_B.csv')


# In[3]:


# Task 1: Print the 5 courses with the highest number of students
top_5_courses = data.nlargest(5, 'Enrollment Count')
print("Top 5 courses with the highest number of students:")
print(top_5_courses['Enrollment Count'])


# In[5]:


# Task 3: Compare the total number of students for "UG", "G", "Corp"
level_counts = data['Enrollment Count'].groupby(data['Level']).sum()
print("\nTotal no. of students per level:")
print(level_counts)


# In[4]:


# Task 2: Print the 5 instructors with the highest number of students
instructors = data.groupby('Instructor(s)/Teaching Assistant').agg({'Enrollment Count': 'sum'}).nlargest(5, 'Enrollment Count')
print("\nTop 5 instructors with the highest number of students:")
print(instructors['Enrollment Count'])


# In[6]:


# Task 4: Compare the number of courses that run at full capacity ("Closed") with those that were not ("Open")
section_status_counts = data.groupby('Section Status').size()
print("\nNumber of courses per section status:")
print(section_status_counts)


# In[7]:


# Task 5: Create a pie chart with the distribution of students per program
program_counts = data['Enrollment Count'].groupby(data['Program']).sum()
plt.pie(program_counts, labels=program_counts.index, autopct='%1f%%')
      
plt.title('Distribution of Students per Program')
plt.show()


# In[8]:


# Task 6: Create a pie chart with the distribution of students per type of delivery (In-Person/Online)
delivery_counts = data['Enrollment Count'].groupby(data['Delivery Mode']).sum()
plt.pie(delivery_counts, labels=delivery_counts.index, autopct='%1f%%' ,)
plt.title('Distribution of Students per Delivery Mode')
plt.show()


# In[9]:


# Task 7: Perform any other analysis that could make sense to better monitor the semester
# Example: Number of students per Delivery Mode
instructional_format_counts = data.groupby('Delivery Mode')['Enrollment Count'].sum()
print("\nNumber of students per Delivery Mode:")
print(instructional_format_counts)


# In[ ]:




