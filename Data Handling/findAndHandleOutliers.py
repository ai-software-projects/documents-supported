import numpy as np


# Method to calculate inter-quantile ranges for the dataset
def calculate_IQR(df_column):
    q1=df_column.quantile(0.25)
    q3=df_column.quantile(0.75)
    IQR=q3-q1
    return [q1,q3,IQR]
# Find outliers in the dataframe and return the dataframe with values such that those
# values which are in outliers range will marked as NaN
def find_outliers_IQR(df):
    not_outliers=df.copy(deep=true)
    for column in df.columns:
        q1,q3,IQR=calculate_IQR(df[column])
        not_outliers[column] = ~((df[column]<(q1-1.5*IQR)) | (df[column]>(q3+1.5*IQR)))
    return not_outliers

# Technique 1: to drop all outliers from the dataframe
def drop_outliers(df):
    not_outliers_df = find_outliers_IQR(df)
    outliers_dropped = not_outliers_df.dropna().reset_index()
    return outliers_dropped

# Technique 2: Finding the thresholds as upper and lower limits and removings those
# outliers which are not present in these ranges
# Doing this for all columns present in the dataframe (Technique is called as CAP OUTLIERS)
def threshold_dropping_outliers(df):
    for column in df.columns:
        upper_limit = df[column].mean() + 3*df[column].std()
        lower_limit = df[column].mean() - 3*df[column].std()
        df[column] = np.where(df[column]>upper_limit,upper_limit,np.where(df[column]<lower_limit,lower_limit,df[column]))
    return df

# Technique 3: Here we will impute that is replace the outliers with means of there respective
# columns so as to there will be no loss of data
def impute_outliers_IQR(df):
    for column in df.columns:
        q1,q3,IQR=calculate_IQR(df[column])
        upper = ~(df[column]>(q3+1.5*IQR)).max()
        lower = ~(df[column]<(q1-1.5*IQR)).min()
        df[column] = np.where(df[column] > upper,df[column].mean(),np.where(df[column] < lower,df[column].mean(),df))
    return df