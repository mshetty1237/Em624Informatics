
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

print("\nRan by Mohit Shetty")

# setting the maximum rows and columns for display.
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 22000)

df = pd.read_csv('covid_comorbidities_USsummary.csv')
(df.head(10))
uniquegroups = list(df['Age Group'].unique())
a = []
for idx, group in enumerate(uniquegroups):
    a.append(df[df['Age Group'] == group]['COVID-19 Deaths'].sum())


# usage of above variables as a dictionary entry
x = {"0-24": a[0], '25-34': a[1], '35-44': a[2], '45-54': a[3], '55-64': a[4], '65-74': a[5], '75-84': a[6], '85+': a[7], 'Not stated':
     a[8]}
# creating the dataframe
df_2 = pd.DataFrame(data=x, index=["Deaths"]).transpose().reset_index()
# making final changes to the created data frame
df_final = df_2.rename(columns={'index': 'Age Groups'})

print("\nCount of people per class of age: ")
print(df_final)


# Creating a pie chart
plt.subplot(211)
n = 20
slices = df_final['Deaths']
# colors generated from random selection of hex-code.
# colors = ["#" + ''.join([random.choice('0123456789ABCDEFG') for j in range(6)]) for i in range(n)]

# assigning the count of Deaths to pie chart from 'slices' variable above
patches, texts = plt.pie(slices, startangle=90, radius=1.0)

plt.title("COVID-19 Deaths per Age group\n(in percentage)", bbox={'facecolor': '0.8', 'pad': 5})
labels = ['{0} - {1:1.2f} %'.format(i, j) for i, j in zip(df_final['Age Groups'], 100.*slices/slices.sum())]
# creating a legend to avoid over lapping of text due to minute percentage of the pie chart.
plt.legend(patches, labels, loc='right', bbox_to_anchor=(-0.5, .5), fontsize=8)

# Creating a bar plot
plt.subplot(212)
sns.barplot(x=df_final['Age Groups'], y=df_final['Deaths']).set(title='Count of deaths per age group.')
plt.plot(df_final['Age Groups'],df_final['Deaths'])
plt.show()

# Correlation
print(" \nFollowing is the correlation in the numeric values")
diff_conditions = list(df['Condition'].unique())
df['num_conditions'] = df['Condition'].apply(lambda x:diff_conditions.index(x))
corr = df[["num_conditions","COVID-19 Deaths"]].corr()
print(corr)
# creating the graph with the correlation matrix using seaborn
sns_plot = sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, cmap='PuRd', annot=True, vmin=-1,
                       vmax=1)

# getting hold of max deaths of group 0-24; first accessing the Age group column and getting max of COVID-19 Deaths.
# then sorting the values by ascending order to find the 2nd highest
print("\n\n Following is the comorbidity group with maximum Deaths of age 0-24:\n")
# using the max_death_1 from above as a condition to get hold of the comorbidity condition associated with it.
max_death_1 = df[df['Age Group'] == '0-24'].sort_values(by=['COVID-19 Deaths'],ascending=False)
print(max_death_1[1:2])

# getting hold of max deaths of group 25-34; first accessing the Age group column and getting max of COVID-19 Deaths.
# then sorting the values by ascending order to find the 2nd highest
print("\n\n Following is the comorbidity group with maximum Deaths of age 25-34:\n")
# using the max_death_2 from above as a condition to get hold of the comorbidity condition associated with it.
max_death_2 = df[df['Age Group'] == '25-34'].sort_values(by=['COVID-19 Deaths'],ascending=False)
print(max_death_2[1:2])

