# Handling Missing values 
### What are missing values?
 In datasets, missing values happen when information about something is not available. It's like having gaps in our data. - Example: Think of a class register where we know some students' names, but we don't have their ages or grades.

 ### Impact of Missing Values on Model Performance:
 When our computer programs try to learn from data, missing information can confuse them. It's like trying to learn a new game, but someone keeps hiding the rules—it makes things much harder.

### Understanding Missing Data
Types of Missing Data:
<br/>
<ul>
<li>
 <h4>Missing Completely at Random (MCAR): - </h4>
 In MCAR, the probability of data being missing is the same for all the observations. In this case, there is no relationship between the missing data and any other values observed or unobserved (the data which is not recorded) within the given dataset. That is, missing values are completely independent of other data. There is no pattern.
 </li>
<li>
 <h4>Missing at Random (MAR): -</h4>

 MAR data means that the reason for missing values can be explained by variables on which you have complete information, as there is some relationship between the missing data and other values/data. In this case, the data is not missing for all the observations. It is missing only within sub-samples of the data, and there is some pattern in the missing values.
 <br/>
For example, if you check the survey data, you may find that all the people have answered their ‘Gender,’ but ‘Age’ values are mostly missing for people who have answered their ‘Gender’ as ‘female.’ (The reason being most of the females don’t want to reveal their age.)
</li>
<li>
<h4>Missing Not at Random (MNAR): - </h4>
Missing values depend on the unobserved data. If there is some structure/pattern in missing data and other observed data can not explain it, then it is considered to be Missing Not At Random (MNAR).This is when the missing data is related to the information we're missing itself. It's a bit tricky because the fact that it's missing tells us something. 
<br/>
 Example: If students who struggle in a subject are less likely to report their grades, and that's why we have missing grades for some, it's not random; it's because of their performance.
</li>
</ul>

### Handling Missing Values
### A. Removal of Missing Values:
<ol>
<li>Listwise Deletion: - Imagine you have a list of students, and if any student has a missing value (like age or grades), you just remove that entire student from the list. 
<br/>
 Example: If you're trying to find the average height of students, and you delete all the students with missing height data, you might end up with a smaller group.
</li>

<li>Pairwise Deletion: - This is like listwise deletion, but instead of removing the whole student, you only ignore the specific missing information when doing certain calculations. 
<br/>
Example: If you're calculating the average weight of students but only some students have missing weight data, you use the available weight data for those calculations.
</li>
</ol>

### B. Imputation Techniques:
<ol>

<li>
Mean, Median, and Mode Imputation: - If you're missing a number (like a student's age), you can use the average (mean), middle value (median), or most common value (mode) for that group. - Example: If you're missing the ages of some students, you might use the average age of all the other students as a guess.
<br/>
Important:
<ul>
<li>
Mean is the most common method of imputing missing values of numeric columns. If there are outliers, then the mean will not be appropriate. In such cases, outliers need to be treated first. 
</li>
<li>
The median is the middlemost value. It’s better to use the median value for imputation in the case of outliers
</li>
</ul>
</li>
<li>
Forward Fill and Backward Fill: - If information is missing in a sequence (like dates), you can use the value from the previous (backward fill) or next (forward fill) observation to fill in the gap. - Example: If you have daily temperature data, and one day's data is missing, you can use the temperature from the day before (backward fill) or after (forward fill).
</li>
<li>
Interpolation Methods: - If you have a series of values, interpolation estimates the missing ones by considering the trend between the available values. - Example: If you have sales data for some months but not all, interpolation can help estimate the missing sales numbers based on the trend in the available data.
</li>
<li>
Regression Imputation: - This is like asking a friend for advice. You use the relationships between variables to predict the missing value. - Example: If you're missing a student's test score but know their study hours, you can use a regression model built on other students to estimate the likely test score.
</li>
<li>
k-Nearest Neighbors (k-NN) Imputation: - Imagine you're lost and ask the nearest people for directions. k-NN imputation uses information from the nearest neighbors to guess the missing value. - Example: If you're missing a student's height, you can look at the heights of the students who are most similar (nearest) to them to make an educated guess.
</li>
</ol>

### C. Advanced Imputation Methods:
<ol>
<li>
Multiple Imputation: - It's like asking several friends for advice and considering multiple opinions. Multiple imputation creates multiple estimates for each missing value. - Example: Instead of relying on just one friend's suggestion, you ask a few others, and the final answer is a combination of their opinions.
</li>
<li>
Matrix Factorization Methods: - Think of a puzzle with missing pieces. Matrix factorization methods try to fill in the missing pieces by breaking down the puzzle into smaller parts. - Example: If you have a matrix representing student performance, and some grades are missing, matrix factorization tries to estimate those missing grades by understanding the patterns in the available data.
</li>
<li>
Generative Adversarial Networks (GANs) for Imputation: - GANs are like artists trying to create a missing part of a painting. They generate realistic values to fill in the gaps in the data. - Example: If you have missing values in an image dataset, GANs can generate new images that fit well with the existing ones, completing the dataset.
</li>
</ol>

##### Reference Link : https://www.linkedin.com/pulse/complete-guide-handling-missing-values-machine-learning-didarul-islam-1elpe/
