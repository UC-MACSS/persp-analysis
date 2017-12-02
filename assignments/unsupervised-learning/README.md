## Unsupervised learning (10 points)

## Colleges (4 points)

`College.csv` dataset contains statistics for a large number of U.S. colleges from the 1995 issue of U.S. News and World Report.

* `Private` - A factor with levels `No` and `Yes` indicating private or public university.
* `Apps` - Number of applications received.
* `Accept` - Number of applications accepted.
* `Enroll` - Number of new students enrolled.
* `Top10perc` - Percent of new students from top 10% of H.S. class.
* `Top25perc` - Percent of new students from top 25% of H.S. class.
* `F.Undergrad` - Number of fulltime undergraduates.
* `P.Undergrad` - Number of parttime undergraduates.
* `Outstate` - Out-of-state tuition.
* `Room.Board` - Room and board costs.
* `Books` - Estimated book costs.
* `Personal` - Estimated personal spending.
* `PhD` - Percent of faculty with Ph.D.'s.
* `Terminal` - Percent of faculty with terminal degrees.
* `S.F.Ratio` - Student/faculty ratio.
* `perc.alumni` - Percent of alumni who donate.
* `Expend` - Instructional expenditure per student.
* `Grad.Rate` - Graduation rate.

1. Perform PCA analysis on the college dataset and plot the first two principal components. Describe the results.
    * What variables appear strongly correlated on the first principal component?
    * What about the second principal component?
    
    > Be sure to remove any variables that are not numeric - PCA only works on numeric variables.
    
1. Calculate the **cumulative proportion of variance explained** by all the principal components (see 10.2.3 in ISLR). Approximately how much of the variance in `College` is explained by the first two principal components?

# Clustering states (6 points)

`USArrests.csv` contains 50 observations (one for each state) from 1973 with variables on crime statistics:

* `Murder` - Murder arrests (per 100,000)
* `Assault` - Assault arrests (per 100,000)
* `Rape` - Rape arrests (per 100,000)
* `UrbanPop` - Percent urban population

1. Perform PCA on the dataset and plot the observations on the first and second principal components.
1. Perform $K$-means clustering with $K=2$. Plot the observations on the first and second principal components and color-code each state based on their cluster membership. Describe your results.
1. Perform $K$-means clustering with $K=4$. Plot the observations on the first and second principal components and color-code each state based on their cluster membership. Describe your results.
1. Perform $K$-means clustering with $K=3$. Plot the observations on the first and second principal components and color-code each state based on their cluster membership. Describe your results.
1. Perform $K$-means clustering with $K=3$ on the first two principal components score vectors, rather than the raw data. Describe your results and compare them to the clustering results with $K=3$ based on the raw data.
1. Using hierarchical clustering with complete linkage and Euclidean distance, cluster the states.
1. Cut the dendrogram at a height that results in three distinct clusters. Which states belong to which clusters?
1. Hierarchically cluster the states using complete linkage and Euclidean distance, after scaling the variables to have standard deviation $1$. What effect does scaling the variables have on the hierarchical clustering obtained?

## Writing the code

Here are some relevant resources for how to write code in Python or R to estimate PCA or clustering.

* [James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning*. New York: Springer.](http://link.springer.com.proxy.uchicago.edu/book/10.1007%2F978-1-4614-7138-7)
* [VanderPlas, Jake. (2016). *Python Data Science Handbook*. O'Reilly Media, Inc.](http://proquestcombo.safaribooksonline.com.proxy.uchicago.edu/book/programming/python/9781491912126)
* My lecture notes (which I will post in the repo after class on Wednesday)
* Lab session on Wednesday

## Submitting your assignment

See [here](../students/) for instructions on submitting course assignments.

## Submission format

Submit your assignment as a **reproducible notebook**.

* If you use Python, this means a Jupyter Notebook (`.ipynb`).
* If you use R, this means an R Markdown document (`.Rmd` knitted with `output: github_document` in the [front matter](http://rmarkdown.rstudio.com/markdown_document_format.html)). Be sure to stage and commit not only the source file but also the output images as well so everything is visible in GitHub.

**Do not submit a plain `.py` or `.R` script.** Your generated graphs will not be visible in the repo, and we will not be running every single script to ensure it works correctly. Make sure to use a notebook format. If you have questions about this, please ask.

## Submission deadline

Submit your pull request before Monday, December 4 (11:30 am).
