Kaggle Competition
------------------

### Goal of the competition:

drawing on the Titanic package, we are required to predict the
likelihood of survival of passengers in the Titanic. In particular, we
should understand the impact of diverse categories such as gender, age,
or class, on the likelihood of survival . To this end, we are encouraged
to make use of machine learning methods.

### My strategy:

I would make use of machine learning algorithms in the "ssparkr" package
(in R) to participate in this competition. First, I'll explore the
dataset by looking at the correlations between variables such as age,
gender, class, and family relations. Then, I'll make several logistic
regression models, which predict the likelihood of survival via various
variables. Comparing the results of those regression models, I would
pick one with various statistically significant variables, high R
square, and theoretically and intuitively sound explanation.

Then, I'll use ml\_function in the "sparkr" package to do the machine
learning. This package offers various machine learning algorithms such
as Decision Tree, Random Forest, Gradient Boosted Tree, Na챦ve Bayes,
and Neutral Networks. After running various machine learning algorithms,
I'll compare results, and pick the best model, by examining performance
metrics. I will especially use AUC (area under the curve) method to pick
the best model.
