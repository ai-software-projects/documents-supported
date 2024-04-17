# Data Reduction Practices

# 1. Dimensionality Reduction

### Concept

Reduce the number of features in the dataset without losing the insights of data. Features are reduced to principal components which map to same data and has almost full coverage of original data points.

IMP: 

Need to find out right number of principal components

If number of components are too high or too low, do not perform dimensionality reduction as it may lead to data insight loss


### Algorithm proposed : PCA

Here, 
d is dimensions in dataset

indices are number of components that cover more than 95% of data points

new_n is number of required Components for ideal PCA

If too many or too less dimensions, DNP = Do Not Perform

If d < 8 : initial_n = d, 
    if indices in [2,6] : new_n = indices else : DNP

If d in [8,30] initial_n = d* 0.8, 
    if indices in [0.3*d, 0.8*d] : new_n = indices else : DNP

If d > 30 initial_n = d* 0.7, 
    if indices in [0.2*d, 0.7*d] : new_n = indices else : DNP

### If PCA is not applicable, we use Feature Selection instead


### eg1 :

d = 15

with this, initial_n = (15*0.8) = 12

Suppose component array comes as [40,20,10,8,7,6,4,1,1,1,1,1]

Hence indices = 7 (it covers 95%) => 7 lies in [4,12]

and so new_n = 7

Result : Apply PCA with n = 7

### eg2 : 

d = 12

with this, initial_n = (12*0.8) = 10

Suppose component array comes as [90,8,0.2,0.2,......]

Hence indices = 2 (it covers 95%) but 2 does not lie in [4,9]

and so DNP

Result : Do not Apply PCA


# 2. Feature Selection

Select the required features and ignore the features with less importance, less variance and correlation.

IMP: We consider two ways to automate and generalise this

Feature selection by Filter methods

Feature selection by Embedded methods

### Filter methods: 

#### ANOVA: 
ANOVA F-value method estimates the degree of linearity between the input feature (i.e., predictor) and the output feature.

f_classif, which calculate F-value between input and output feature for classification task

f_regression, which calculate F-value between input and output feature for classification task

#### Variance threshold:
Variance threshold method removes features whose variance below a pre-defined cutoff value.

#### Mutual Information:
Mutual information (MI) measures the dependence of one variable to another by quantifying the amount of information obtained about one feature, through the other feature

mutual_info_classif, which calculate MI for classification task

mutual_info_regression, which calculate MI for regression task

#### Selector for these algorithms: SelectKBest

SelectKBest has two important parameters:

score_func: the filter function that is used for feature selection
k: the number of top features to select

### Algorithm for Filter:

If linear dependency is there (check first) use ANOVA and optimise it

If non linear, use Mutual Info and optimise it

If too many features, first apply Variance threshold and remove those with variance < 15%

Optimisation: Check total variance and SelectKBest


### Embedded methods

#### For Tree/Forest classification Use Decision tree/RFC based feature selection

#### For Linear/Logistic Regression Use Lasso / Ridge Regression