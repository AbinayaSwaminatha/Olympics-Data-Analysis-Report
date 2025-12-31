# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Load Dataset
df = pd.read_csv(r"C:\Users\Abinaya\Downloads\olympic_analysis\archive (1).zip")  # Replace with your actual file path
df.head()

#Data Cleaning
print("Initial shape:", df.shape)
df.drop_duplicates(inplace=True)
print("After dropping duplicates:", df.shape)
df.isnull().sum()
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Height'] = df['Height'].fillna(df['Height'].median())
df['Weight'] = df['Weight'] = df['Weight'].fillna(df['Weight'].median())
#Basic Info
print(df.info())
print(df.describe())

#Exploratory Data Analysis (EDA)

# Gender Distribution
sns.countplot(data=df, x='Sex', palette='Set2', hue='Sex', legend=False)
plt.title('Gender Distribution of Athletes')
plt.show()

# Age Distribution
sns.histplot(df['Age'], bins=30, kde=True, color='skyblue')
plt.title('Age Distribution of Athletes')
plt.xlabel('Age')
plt.show()

# Top 10 Countries by Participation
top_teams = df['Team'].value_counts().head(10)
top_teams.plot(kind='bar', color='orange', title='Top 10 Countries by Participation')
plt.ylabel('Number of Athletes')
plt.show()

# Participation Over Time
yearly_participation = df.groupby('Year')['ID'].nunique()
yearly_participation.plot(kind='line', marker='o', title='Athlete Participation Over Time')
plt.ylabel('Number of Athletes')
plt.show()

# Gender Participation Over Time
gender_year = df.groupby(['Year', 'Sex'])['ID'].nunique().reset_index()
fig = px.bar(gender_year, x='Year', y='ID', color='Sex', barmode='group',
             title='Gender Participation Over the Years')
fig.show()

# Height vs Weight by Gender
sns.scatterplot(data=df, x='Weight', y='Height', hue='Sex', alpha=0.6)
plt.title('Height vs Weight by Gender')
plt.show()

# Age Distribution by Gender
sns.boxplot(data=df, x='Sex', y='Age', palette='Set3', hue='Sex', legend=False)
plt.title('Age Distribution by Gender')
plt.show()

#  Medal Tally by Country
medals_df = df[df['Medal'].notnull()]
medal_tally = medals_df.groupby('Team')['Medal'].count().sort_values(ascending=False).head(10)
medal_tally.plot(kind='bar', color='gold', title='Top 10 Countries by Medal Count')
plt.ylabel('Number of Medals')
plt.xticks(rotation=45)
plt.show()

# Top Athletes by Medal Count
top_athletes = medals_df.groupby('Name')['Medal'].count().sort_values(ascending=False).head(10)
top_athletes.plot(kind='barh', color='purple', title='Top 10 Medal-Winning Athletes')
plt.xlabel('Number of Medals')
plt.gca().invert_yaxis()
plt.show()

# Sport-wise Participation
sport_participation = df['Sport'].value_counts().head(10)
sport_participation.plot(kind='bar', color='teal', title='Top 10 Sports by Participation')
plt.ylabel('Number of Athletes')
plt.xticks(rotation=45)
plt.show()

