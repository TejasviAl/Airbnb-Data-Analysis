import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel('airbnb_data.xlsx')
print(df.head())
print(df.columns)

# missing values check
print(df.isnull().sum())
# to check type of data
print(df.info())

# lastreview format is changed from object to date type 
df['last review'] = pd.to_datetime(df['last review'], errors='coerce')
print(df.info())

# handling missing values, to not wrong output we are making the least present date to be in place NaN values 
df.fillna({'reviews per month':0, 'last review':df['last review'].min()}, inplace=True)
df.dropna(subset= {"NAME", "host name"}, inplace = True)
print(df.isnull().sum())

# for removing unnecessary columns
df= df.drop(columns={'license', 'house_rules'}, errors='ignore')
print(df.head())

# converting dollar values to float numbers
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
print(df['price'])
df['service fee'] = df['service fee'].replace('[\$,]', '', regex=True).astype(float)
print(df['service fee'])

# removing duplicates
df.drop_duplicates(inplace=True)
print(df.info())

# decriptive statistics : basics statistics is known  by using describe()
print(df.describe())

# Visualization
# the distribution of listing prices
plt.figure(figsize=(10,6))
sns.histplot(df['price'], bins=50, kde=True, color='red')
plt.title("Distribution of listing prices")
plt.xlabel("Price($)")
plt.ylabel("Frequency")
plt.show()

# different room type 
print(df['room type'])
plt.figure(figsize=(8,6))
sns.countplot(x='room type', data = df, color='blue') 
plt.title("Room type distribution")
plt.xlabel('room type')
plt.ylabel('count')
plt.show()

# listing distributed acrosss different neighborhood
plt.figure(figsize=(12, 8))
sns.countplot(y='neighbourhood group', data=df, color='lightgreen', order=df['neighbourhood group'].value_counts().index )
plt.title("No of listings across Neighborhood Group")
plt.xlabel('Count')
plt.ylabel('Neighborhood Group')
plt.show()

# relationship between price and room type?
plt.figure(figsize=(10, 6))
sns.boxplot(x='room type', y='price', data = df, palette='Set1')
plt.title('Relationship between price and type of room')
plt.xlabel('Room type')
plt.ylabel('Price($)')
plt.show()

# how has the no of reviews change over with time

reviews_over_time = df.groupby(df['last review'].dt.to_period('M')).size()
plt.figure(figsize=(10,6))
reviews_over_time.plot(kind='line', color='yellow')
plt.title("Review Change over with time")
plt.xlabel('Date')
plt.ylabel('Number of reviews')
plt.show()


