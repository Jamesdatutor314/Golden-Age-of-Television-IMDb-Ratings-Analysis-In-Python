#!/usr/bin/env python
# coding: utf-8

# ## Basic Python - Project <a id='intro'></a>

# ## Introduction <a id='intro'></a>
# In this project, you will work with data from the entertainment industry. You will study a dataset with records on movies and shows. The research will focus on the "Golden Age" of television, which began in 1999 with the release of *The Sopranos* and is still ongoing.
# 
# The aim of this project is to investigate how the number of votes a title receives impacts its ratings. The assumption is that highly-rated shows (we will focus on TV shows, ignoring movies) released during the "Golden Age" of television also have the most votes.
# 
# ### Stages 
# Data on movies and shows is stored in the `/datasets/movies_and_shows.csv` file. There is no information about the quality of the data, so you will need to explore it before doing the analysis.
# 
# First, you'll evaluate the quality of the data and see whether its issues are significant. Then, during data preprocessing, you will try to account for the most critical problems.
#  
# Your project will consist of three stages:
#  1. Data overview
#  2. Data preprocessing
#  3. Data analysis

# ## Stage 1. Data overview <a id='data_review'></a>
# 
# Open and explore the data.

# You'll need `pandas`, so import it.

# In[14]:


# importing pandas
import pandas as pd


# Read the `movies_and_shows.csv` file from the `datasets` folder and save it in the `df` variable:

# In[15]:


# reading the files and storing them to df
df = pd.read_csv('/datasets/movies_and_shows.csv')


# Print the first 10 table rows:

# In[16]:


# obtaining the first 10 rows from the df table
# hint: you can use head() and tail() in Jupyter Notebook without wrapping them into print()
df.head(10)


# Obtain the general information about the table with one command:

# In[17]:


# obtaining general information about the data in df
df.info()


# The table contains nine columns. The majority store the same data type: object. The only exceptions are `'release Year'` (int64 type), `'imdb sc0re'` (float64 type) and `'imdb v0tes'` (float64 type). Scores and votes will be used in our analysis, so it's important to verify that they are present in the dataframe in the appropriate numeric format. Three columns (`'TITLE'`, `'imdb sc0re'` and `'imdb v0tes'`) have missing values.
# 
# According to the documentation:
# - `'name'` — actor/director's name and last name
# - `'Character'` — character played (for actors)
# - `'r0le '` — the person's contribution to the title (it can be in the capacity of either actor or director)
# - `'TITLE '` — title of the movie (show)
# - `'  Type'` — show or movie
# - `'release Year'` — year when movie (show) was released
# - `'genres'` — list of genres under which the movie (show) falls
# - `'imdb sc0re'` — score on IMDb
# - `'imdb v0tes'` — votes on IMDb
# 
# We can see three issues with the column names:
# 1. Some names are uppercase, while others are lowercase.
# 2. There are names containing whitespace.
# 3. A few column names have digit '0' instead of letter 'o'. 
# 

# ### Conclusions <a id='data_review_conclusions'></a> 
# 
# Each row in the table stores data about a movie or show. The columns can be divided into two categories: the first is about the roles held by different people who worked on the movie or show (role, name of the actor or director, and character if the row is about an actor); the second category is information about the movie or show itself (title, release year, genre, imdb figures).
# 
# It's clear that there is sufficient data to do the analysis and evaluate our assumption. However, to move forward, we need to preprocess the data.

# ## Stage 2. Data preprocessing <a id='data_preprocessing'></a>
# Correct the formatting in the column headers and deal with the missing values. Then, check whether there are duplicates in the data.

# In[18]:


# the list of column names in the df table
df.columns


# Change the column names according to the rules of good style:
# * If the name has several words, use snake_case
# * All characters must be lowercase
# * Remove whitespace
# * Replace zero with letter 'o'

# In[19]:


# renaming columns
column_names = list(df.columns) 
column_names


# In[20]:


#remove white space
def remove_white_space(dataframe,col_names):
    '''will remove white space in the column'''
    for col in col_names:
        dataframe = dataframe.rename(columns = {col:col.strip()})
    return dataframe

df = remove_white_space(df,column_names)
column_names = list(df.columns)
column_names


# In[21]:


#make columns lowercase
def lower_case(dataframe,col_names):
    '''will make columns lowercase'''
    for col in col_names:
        dataframe = dataframe.rename(columns = {col:col.lower()})
    return dataframe

df = lower_case(df,column_names)
column_names = list(df.columns)
column_names


# In[22]:


#replace 0 with o
def replace_zero(dataframe,col_names):
    '''will make columns that have zero with o'''
    for col in col_names:
        dataframe = dataframe.rename(columns = {col:col.replace('0','o')})
    return dataframe

df = replace_zero(df,column_names)
column_names = list(df.columns)
column_names


# In[23]:


#use snake case
def replace_zero(dataframe,col_names):
    '''will make columns with more than one words use snake case'''
    for col in col_names:
        dataframe = dataframe.rename(columns = {col:col.replace(' ','_')})
    return dataframe

df = replace_zero(df,column_names)
column_names = list(df.columns)
column_names


# Check the result. Print the names of the columns once more:

# In[24]:


# checking result: the list of column names
df.columns


# ### Missing values <a id='missing_values'></a>
# First, find the number of missing values in the table. To do so, combine two `pandas` methods:

# In[25]:


# calculating missing values
df.isna().sum()


# We identified missing values in several columns. While the missing value in `'title'` isn't critical, missing values in `'imdb_score'` and `'imdb_votes'` affect around 6% of the data, which could impact our analysis. To ensure data integrity, we'll drop all rows with missing values.

# In[26]:


# dropping rows where columns with scores, and votes have missing values
df = df.dropna(subset = ['imdb_votes','imdb_score']).reset_index(drop=True)


# Make sure the table doesn't contain any more missing values. Count the missing values again.

# In[27]:


# counting missing values
df.isna().sum()


# ### Duplicates <a id='duplicates'></a>
# Find the number of duplicate rows in the table using one command:

# In[28]:


# counting duplicate rows
df.duplicated().sum()


# Review the duplicate rows to determine if removing them would distort our dataset.

# In[29]:


# Produce table with duplicates (with original rows included) and review last 5 rows
duplicates = df[df.duplicated()]
duplicates


# There are two clear duplicates in the printed rows. We can safely remove them.
# Call the `pandas` method for getting rid of duplicate rows:

# In[30]:


# removing duplicate rows
df = df.drop_duplicates().reset_index(drop=True)


# Check for duplicate rows once more to make sure you have removed all of them:

# In[31]:


# checking for duplicates
df.duplicated().sum()


# Now get rid of implicit duplicates in the `'type'` column. For example, the string `'SHOW'` can be written in different ways. These kinds of errors will also affect the result.

# Print a list of unique `'type'` names, sorted in alphabetical order. To do so:
# * Retrieve the intended dataframe column 
# * Apply a sorting method to it
# * For the sorted column, call the method that will return all unique column values

# In[32]:


# viewing unique type names
df['type'].unique()


# Look through the list to find implicit duplicates of `'show'` (`'movie'` duplicates will be ignored since the assumption is about shows). These could be names written incorrectly or alternative names of the same genre.
# 
# You will see the following implicit duplicates:
# * `'shows'`
# * `'SHOW'`
# * `'tv show'`
# * `'tv shows'`
# * `'tv series'`
# * `'tv'`
# 
# To get rid of them, declare the function `replace_wrong_show()` with two parameters: 
# * `wrong_shows_list=` — the list of duplicates
# * `correct_show=` — the string with the correct value
# 
# The function should correct the names in the `'type'` column from the `df` table (i.e., replace each value from the `wrong_shows_list` list with the value in `correct_show`).

# In[33]:


# function for replacing implicit duplicates
def replace_wrong_show(dataframe,column_name,wrong_shows_list, correct_show):
    dataframe[column_name] = dataframe[column_name].replace(wrong_shows_list,correct_show)
    return dataframe


# Call `replace_wrong_show()` and pass it arguments so that it clears implicit duplicates and replaces them with `SHOW`:

# In[36]:


show_list = [x for x in list(df['type'].unique()) if 'movie' not in x.lower()]
show_list


# In[37]:


# removing implicit duplicates
df = replace_wrong_show(dataframe=df,column_name='type',wrong_shows_list=show_list, correct_show='SHOW')


# Make sure the duplicate names are removed. Print the list of unique values from the `'type'` column:

# In[38]:


# viewing unique genre names
df['type'].unique()


# ### Conclusions <a id='data_preprocessing_conclusions'></a>
# We detected three issues with the data:
# 
# - Incorrect header styles
# - Missing values
# - Duplicate rows and implicit duplicates
# 
# The headers have been cleaned up to make processing the table simpler.
# 
# All rows with missing values have been removed. 
# 
# The absence of duplicates will make the results more precise and easier to understand.
# 
# Now we can move on to our analysis of the prepared data.

# ## Stage 3. Data analysis <a id='hypotheses'></a>

# Based on the previous project stages, you can now define how the assumption will be checked. Calculate the average amount of votes for each score (this data is available in the `imdb_score` and `imdb_votes` columns), and then check how these averages relate to each other. If the averages for shows with the highest scores are bigger than those for shows with lower scores, the assumption appears to be true.
# 
# Based on this, complete the following steps:
# 
# - Filter the dataframe to only include shows released in 1999 or later.
# - Group scores into buckets by rounding the values of the appropriate column (a set of 1-10 integers will help us make the outcome of our calculations more evident without damaging the quality of our research).
# - Identify outliers among scores based on their number of votes, and exclude scores with few votes.
# - Calculate the average votes for each score and check whether the assumption matches the results.

# To filter the dataframe and only include shows released in 1999 or later, you will take two steps. First, keep only titles published in 1999 or later in our dataframe. Then, filter the table to only contain shows (movies will be removed).

# In[41]:


# using conditional indexing modify df so it has only titles released after 1999 (with 1999 included)
# give the slice of dataframe new name

df_after_1999 = df[df['release_year'] >= 1999]
df_after_1999.head()


# In[42]:


# repeat conditional indexing so df has only shows (movies are removed as result)
df_only_shows = df_after_1999[df_after_1999['type']=='SHOW']
df_only_shows.head()


# The scores that are to be grouped should be rounded. For instance, titles with scores like 7.8, 8.1, and 8.3 will all be placed in the same bucket with a score of 8.

# In[44]:


# rounding column with scores
df_only_shows['imdb_score_rounded'] = df_only_shows['imdb_score'].agg(lambda x: round(x)) 

#checking the outcome with tail()
df_only_shows.tail()


# It is now time to identify outliers based on the number of votes.

# In[49]:


# Use groupby() for scores and count all unique values in each group, print the result
df_only_shows.groupby('imdb_score_rounded')['name'].count()


# Based on the aggregation performed, it is evident that scores 2 (24 voted shows), 3 (27 voted shows), and 10 (only 8 voted shows) are outliers. There isn't enough data for these scores for the average number of votes to be meaningful.

# To obtain the mean numbers of votes for the selected scores (we identified a range of 4-9 as acceptable), use conditional filtering and grouping.

# In[52]:


# filter dataframe using two conditions (scores to be in the range 4-9)
df_range = df_only_shows[(df_only_shows['imdb_score_rounded'] >= 4) & (df_only_shows['imdb_score_rounded'] <= 9)]
df_range.head()


# In[57]:


# group scores and corresponding average number of votes, reset index and print the result
df_grouped_scores = df_range.groupby('imdb_score_rounded')['imdb_votes'].agg(['mean']).reset_index()
df_grouped_scores


# Now for the final step! Round the column with the averages, rename both columns, and print the dataframe in descending order.

# In[61]:


# round column with averages
df_grouped_scores['mean'] = df_grouped_scores['mean'].round()

# rename columns
df_grouped_scores = df_grouped_scores.rename(columns = {'imdb_score_rounded':'imdb score'})
df_grouped_scores

# print dataframe in descending order
df_grouped_scores.sort_values(by='mean',ascending = False)


# The assumption macthes the analysis: the shows with the top 3 scores have the most amounts of votes.

# ## Conclusion <a id='hypotheses'></a>

# The research done confirms that highly-rated shows released during the "Golden Age" of television also have the most votes. While shows with score 4 have more votes than ones with scores 5 and 6, the top three (scores 7-9) have the largest number. The data studied represents around 94% of the original set, so we can be confident in our findings.
