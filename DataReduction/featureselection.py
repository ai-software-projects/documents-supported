# DO not RUN 
# X_data is dependent variables y_data is target and feature_name is col names

# ANOVA - Classification example

# Import f_classif from Scikit-learn
from sklearn.feature_selection import f_classif

# Create f_classif object to calculate F-value
f_value = f_classif(X_data, y_data)

# Print the name and F-value of each feature
for feature in zip(feature_names, f_value[0]):
    print(feature)


#-------------------------------------------------------------------------
# Variance threshold remove < 15% variance

# Import VarianceThreshold from Scikit-learn
from sklearn.feature_selection import VarianceThreshold

# Create VarianceThreshold object to perform variance thresholding
selector = VarianceThreshold(threshold=0.15)

# Transform the dataset according to variance thresholding
X_data_new = selector.fit_transform(X_data)

# Print the results
print('Number of features before variance thresholding: {}'.format(X_data.shape[1]))
print('Number of features after variance thresholding: {}'.format(X_data_new.shape[1]))

# Print the name and variance of each feature
for feature in zip(feature_names, selector.variances_):
    print(feature)


#-------------------------------------------------------------------------
# Mutual Information

# Import mutual_info_classif from Scikit-learn
from sklearn.feature_selection import mutual_info_classif

# Create mutual_info_classif object to calculate mutual information
MI_score = mutual_info_classif(X_data, y_data, random_state=0)

# Print the name and mutual information score of each feature
for feature in zip(feature_names, MI_score):
    print(feature)


#-------------------------------------------------------------------------

#use SelectKBest for these algorithms other than variance threshold

# Import SelectKBest from Scikit-learn
from sklearn.feature_selection import SelectKBest

# Create a SelectKBest object
skb = SelectKBest(score_func=f_classif, # Set f_classif as our criteria to select features
                  k=2)                  # Select top two features based on the criteria

# Train and transform the dataset according to the SelectKBest
X_data_new = skb.fit_transform(X_data, y_data)

# Print the results
print('Number of features before feature selection: {}'.format(X_data.shape[1]))
print('Number of features after feature selection: {}'.format(X_data_new.shape[1]))

# Print the name of the selected features
for feature_list_index in skb.get_support(indices=True):
    print('- ' + feature_names[feature_list_index])


#----------------------------------------------------------------------------
# Embedded : Use feature selection with training algorithms
#----------------------------------------------------------------------------

# Create a random forest classifier
rfc = RandomForestClassifier(random_state=0, 
                             criterion='gini') # Use gini criterion to define feature importance

# Create a SelectFromModel object 
sfm = SelectFromModel(estimator=rfc, # Use random forest classifier to identify features
                      threshold=0.2) # that have an importance of more than 0.2

# Train the selector
sfm = sfm.fit(X_train, y_train)

# Print the names of the most important features
print('The most important features based on random forest classifier:')
for feature_list_index in sfm.get_support(indices=True):
    print('- ' + feature_names[feature_list_index])

# Similar for Decision tree

#------------------------------------------------------------------------

# ridge regularisation (lasso is similar)
# example

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize logistic regression model with regularization
# Ridge: penalty l2 solver lbfgs
# Lasso: penalty l1 solver liblinear
logistic = LogisticRegression(penalty='l2', solver='lbfgs', C=1.0)  # C is the inverse of regularization strength

# Fit the model to the training data
logistic.fit(X_train_scaled, y_train)