assignment7
================

Lab Notebook
------------

``` r
#install.packages("poliscidata")
data(gss, package = "poliscidata")

# convert to tibble
library(tidyverse)
```

    ## -- Attaching packages -------------------------------------------- tidyverse 1.2.1 --

    ## v ggplot2 2.2.1     v purrr   0.2.4
    ## v tibble  1.3.4     v dplyr   0.7.4
    ## v tidyr   0.7.2     v stringr 1.2.0
    ## v readr   1.1.1     v forcats 0.2.0

    ## -- Conflicts ----------------------------------------------- tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

``` r
gss <- as_tibble(gss)
```

#### demographic information

``` r
library(ggplot2)

# age density plot
ggplot(gss, aes(age))+
    geom_density(aes(fill=age), na.rm = TRUE, fill = "blue", alpha = 0.3)
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20age-1.png)

``` r
# race histogram
ggplot(gss, x = race) +
    geom_bar(aes(race), na.rm = TRUE, fill = "blue", alpha = 0.3)
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20race%20and%20sex-1.png)

``` r
# gender histogram
ggplot(gss, x = race) +
    geom_bar(aes(sex), na.rm = TRUE, fill = "blue", alpha = 0.3)
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20race%20and%20sex-2.png)

``` r
# race and sex histogram
ggplot(gss, aes(race)) +
    geom_bar(aes(fill = sex), na.rm = TRUE, alpha = 0.3)
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20race%20and%20sex-3.png)

``` r
# marital status histogram
ggplot(gss, x = marital) +
    geom_bar(aes(marital), na.rm = TRUE, fill = "blue", alpha = 0.3)
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20marital%20status-1.png)

``` r
ggplot(gss, aes(age)) +
    geom_bar(aes(fill = marital), na.rm = TRUE, alpha = 0.5) + 
    labs(title = " The distribution of marital status across age", x = "race", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20marital%20status-2.png)

``` r
# highest degree histogram
ggplot(gss, x = degree) +
    geom_bar(aes(degree), na.rm = TRUE, fill = "blue", alpha = 0.3)
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20highest%20degree-1.png)

``` r
# work status histogram
gss_temp = subset(gss, !is.na(wrkstat))
ggplot(gss_temp, x = wrkstat) +
    geom_bar(aes(wrkstat), fill = "blue", alpha = 0.3)
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20work%20status-1.png)

``` r
# income histogram
gss_temp = subset(gss, !is.na(income06))
ggplot(gss_temp, x = income06) +
    geom_bar(aes(income06), fill = "blue", alpha = 0.3) +
    labs(title = " The histogram of income", x = "income", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20income-1.png)

``` r
# The distribution of highest degree across income
ggplot(gss_temp, aes(income06)) +
    geom_bar(aes(fill = degree), na.rm = TRUE, alpha = 0.5) + 
    labs(title = " The distribution of highest degree across income", x = "income", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20income-2.png)

``` r
# political views histogram
gss_temp = subset(gss, !is.na(polviews))
ggplot(gss_temp, x = polviews) +
    geom_bar(aes(polviews), na.rm = TRUE, fill = "blue", alpha = 0.3)
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20political%20views-1.png)

``` r
# The distribution of voting in 2008 across political views
gss_temp = subset(gss, !is.na(polviews))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(polviews)) +
    geom_bar(aes(fill = pres08), na.rm = TRUE, alpha = 0.3) + 
    labs(title = "The distribution of voting in 2008 across political views", x = "political views", y = "num of paricipants")  +
    scale_fill_discrete(name = "voting") +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/demographic%20informattion%20-%20voting%20in%2008-1.png)

``` r
# The distribution of voting in 2008 across highest degree
gss_temp = subset(gss, !is.na(degree))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(degree)) +
    geom_bar(aes(fill = pres08), na.rm = TRUE, alpha = 0.3) + 
    labs(title = "The distribution of voting in 2008 across highest degree", x = "highest degree", y = "num of paricipants")  +
    scale_fill_discrete(name = "voting") +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/demographic%20informattion%20-%20voting%20in%2008-2.png)

``` r
# The distribution of voting in 2008 across income
gss_temp = subset(gss, !is.na(income06))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(income06)) +
    geom_bar(aes(fill = pres08), na.rm = TRUE, alpha = 0.3) + 
    labs(title = "The distribution of voting in 2008 across income", x = "income", y = "num of paricipants")  +
    scale_fill_discrete(name = "voting") +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/demographic%20informattion%20-%20voting%20in%2008-3.png)

``` r
# Voting for 2008 scatterplot of income vs age by degree
gss_temp = subset(gss, !is.na(age))
gss_temp = subset(gss_temp, !is.na(income06))
gss_temp = subset(gss_temp, !is.na(pres08))
gss_temp = subset(gss_temp, !is.na(degree))

ggplot(gss_temp, aes(age, income06, color = pres08), alpha = 0.5) + 
    geom_jitter() +
    facet_grid(.~ degree) +
    labs(title = "Voting for 2008 scatterplot of income vs age by degree", x = "age", y ="income")  +
    scale_fill_discrete(name = "voting") +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.y = element_text(size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20mixed-1.png)

``` r
# Voting for 2008 scatterplot of race vs gender by marital status
gss_temp = subset(gss, !is.na(race))
gss_temp = subset(gss_temp, !is.na(sex))
gss_temp = subset(gss_temp, !is.na(pres08))
gss_temp = subset(gss_temp, !is.na(marital))

ggplot(gss_temp, aes(race, sex, color = pres08), alpha = 0.5) + 
    geom_jitter() +
    facet_grid(.~ marital) +
    labs(title = "Voting for 2008 scatterplot of race vs gender by marital status", x = "race", y ="gender")  +
    scale_fill_discrete(name = "voting") +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.y = element_text(size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/demographic%20information%20-%20mixed-2.png)

#### attitude

``` r
# Should Government Reduce Income Differences?
gss_temp = subset(gss, !is.na(eqwlth))
ggplot(gss_temp, x = eqwlth) +
    geom_bar(aes(eqwlth), na.rm = TRUE, fill = "blue", alpha = 0.3) + 
    scale_x_continuous(breaks = seq(1, 7, 1)) + 
    labs(title = "The histogram of 'Should Government Reduce Income Differences'", x = "Agree to Disagree", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20income-1.png)

``` r
#Attitude of equal wealth across highest degree
gss_temp = subset(gss, !is.na(eqwlth))
gss_temp = subset(gss_temp, !is.na(degree))
ggplot(gss_temp, aes(degree)) +
    geom_bar(aes(fill = factor(eqwlth)), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude", labels = c("Agree", "", "", "No difference", "", "", "Disagree")) +
    labs(title = "Attitude of equal wealth across highest degree", x = "highest degree", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6))
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20income-2.png)

``` r
# Attitude of equal wealth across income
gss_temp = subset(gss, !is.na(eqwlth))
gss_temp = subset(gss_temp, !is.na(income06))
ggplot(gss_temp, aes(income06)) +
    geom_bar(aes(fill = factor(eqwlth)), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude", labels = c("Agree", "", "", "No difference", "", "", "Disagree")) +
    labs(title = "Attitude of equal wealth across income", x = "income", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6))
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20income-3.png)

``` r
# Allow communists to speak
gss_temp = subset(gss, !is.na(spkcom))
ggplot(gss_temp, x = spkcom) +
    geom_bar(aes(spkcom), na.rm = TRUE, fill = "blue", alpha = 0.3) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-1.png)

``` r
# Attitude of 'Allow communists to speak' across political views
gss_temp = subset(gss, !is.na(spkcom))
gss_temp = subset(gss_temp, !is.na(polviews))
ggplot(gss_temp, aes(polviews)) +
    geom_bar(aes(fill = spkcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Allow communists to speak' across political views", x = "political views", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-2.png)

``` r
# Attitude of 'Allow communists to speak'  across voting in 2008
gss_temp = subset(gss, !is.na(spkcom))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(pres08)) +
    geom_bar(aes(fill = spkcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Allow communists to speak' across voting in 2008", x = "voting in 2008", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-3.png)

``` r
# Voting for 2008 scatterplot of attitude towards communists vs income by political views
gss_temp = subset(gss, !is.na(spkcom))
gss_temp = subset(gss_temp, !is.na(income06))
gss_temp = subset(gss_temp, !is.na(pres08))
gss_temp = subset(gss_temp, !is.na(polviews))

ggplot(gss_temp, aes(spkcom, income06, color = pres08), alpha = 0.5) + 
    geom_jitter() +
    facet_grid(.~ polviews) +
    labs(title = "Voting for 2008 scatterplot of attitude towards communists vs income by political views", x = "Allow communists to speak", y ="income", color = "voting")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(size = 8), axis.text.y = element_text(size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-4.png)

``` r
# Should communist teacher be fired
gss_temp = subset(gss, !is.na(colcom))
ggplot(gss_temp, x = colcom) +
    geom_bar(aes(colcom), na.rm = TRUE, fill = "blue", alpha = 0.3) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-5.png)

``` r
# Attitude of 'Should communist teacher be fired' across political views
gss_temp = subset(gss, !is.na(colcom))
gss_temp = subset(gss_temp, !is.na(polviews))
ggplot(gss_temp, aes(polviews)) +
    geom_bar(aes(fill = colcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Should communist teacher be fired' across political views", x = "political views", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-6.png)

``` r
# Attitude of 'Should communist teacher be fired'  across voting in 2008
gss_temp = subset(gss, !is.na(colcom))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(pres08)) +
    geom_bar(aes(fill = colcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Should communist teacher be fired' across voting in 2008", x = "voting in 2008", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-7.png)

``` r
# Voting for 2008 scatterplot of attitude towards communists vs income by political views
gss_temp = subset(gss, !is.na(colcom))
gss_temp = subset(gss_temp, !is.na(income06))
gss_temp = subset(gss_temp, !is.na(pres08))
gss_temp = subset(gss_temp, !is.na(polviews))

ggplot(gss_temp, aes(colcom, income06, color = pres08), alpha = 0.5) + 
    geom_jitter() +
    facet_grid(.~ polviews) +
    labs(title = "Voting for 2008 scatterplot of attitude towards communists vs income by political views", x = "Should communist teacher be fired", y ="income", color = "voting")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(size = 8), axis.text.y = element_text(size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-8.png)

``` r
# Allow communist books in library
gss_temp = subset(gss, !is.na(libcom))
ggplot(gss_temp, x = libcom) +
    geom_bar(aes(libcom), na.rm = TRUE, fill = "blue", alpha = 0.3)
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-9.png)

``` r
# Attitude of 'Allow communist books in library' across political views
gss_temp = subset(gss, !is.na(libcom))
gss_temp = subset(gss_temp, !is.na(polviews))
ggplot(gss_temp, aes(polviews)) +
    geom_bar(aes(fill = libcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Allow communist books in library' across political views", x = "political views", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-10.png)

``` r
# Attitude of 'Allow communist books in library' across voting in 2008
gss_temp = subset(gss, !is.na(libcom))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(pres08)) +
    geom_bar(aes(fill = libcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Allow communist books in library' across voting in 2008", x = "voting in 2008", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-11.png)

``` r
# Voting for 2008 scatterplot of attitude towards communists vs income by political views
gss_temp = subset(gss, !is.na(libcom))
gss_temp = subset(gss_temp, !is.na(income06))
gss_temp = subset(gss_temp, !is.na(pres08))
gss_temp = subset(gss_temp, !is.na(polviews))

ggplot(gss_temp, aes(libcom, income06, color = pres08), alpha = 0.5) + 
    geom_jitter() +
    facet_grid(.~ polviews) +
    labs(title = "Voting for 2008 scatterplot of attitude towards communists vs income by political views", x = "Allow communist books in library", y ="income", color = "voting")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(size = 8), axis.text.y = element_text(size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/attitude%20towards%20policy%20-%20communists-12.png)

Exploration write-up
--------------------

#### Demographic information

To begin with, I would like to figure out who participated in the General Social Survey, so I choose these columns, including age, race, gender, martial status, highest education, working status, income, political views, and voting in 2008 to have a overview of the sample distribution.

I expected to observe approximately normal distributions for most demographic variables, however, this is not always the case.

-   Age: Most participants are 30-50, but the age distribution is greatly right-skewed.

-   Race and gender: The majority of participants are white, and male-female is roughly half-half in the sample.

-   Marital status: The majority of people are married, followed by people who have never married. This is somewhat surprising to me, as I supposed that people who have never married were rare among the population. If we look at the marital status and age at the same time, then it all makes sense - people under 35 largely contribute to the "never married" status.

``` r
# The distribution of marital status across age
ggplot(gss_temp, aes(age)) +
    geom_bar(aes(fill = marital), na.rm = TRUE, alpha = 0.5) + 
    labs(title = "The distribution of marital status across age", x = "age", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-1-1.png)

-   Highest education: Most participants only finished high school, and amazingly, only a small percentage of people entered college or graduate school.

-   Working status: As expected, most people work full time, but people who have retired, work part time and keep in the house also take some protportion.

-   Income: The distribution of income is obviously left-skewed, which means that participants are more likely to have a higher income. If we look at income and highest education at the same time, we can find out that people with advanced degree can earn a high income more easily, in particular, falling in the income group over $150,000.

``` r
# income histogram
gss_temp = subset(gss, !is.na(income06))
ggplot(gss_temp, x = income06) +
    geom_bar(aes(income06), fill = "blue", alpha = 0.3) +
    labs(title = "The histogram of income", x = "income", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-2-1.png)

``` r
# The distribution of highest degree across income
ggplot(gss_temp, aes(income06)) +
    geom_bar(aes(fill = degree), na.rm = TRUE, alpha = 0.5) + 
    labs(title = "The distribution of highest degree across income", x = "income", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-2-2.png)

-   Political Views: As for political views, most people recognize themselves as "moderate", and the rest of them distirbute equally between liberal and conservative.

-   Voting in 08: About 2/3 of participants voted for Obama. It might be unsuprising at first, but we should notice that most of them don't have a preference when being asked about political views.

Putting political views and voting in 2008 together, we can see that paricipants who are moderate or slightly conservative voted for Obama, rather than McCain.

Similarly, we put highest degree and income instead of political views. People with high-school degree majorly supported Obama, and people with lower income are more likely to vote for Obama.

``` r
# The distribution of voting in 2008 across political views
gss_temp = subset(gss, !is.na(polviews))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(polviews)) +
    geom_bar(aes(fill = pres08), na.rm = TRUE, alpha = 0.3) + 
    labs(title = "The distribution of voting in 2008 across political views", x = "political views", y = "num of paricipants")  +
    scale_fill_discrete(name = "voting") +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-3-1.png)

``` r
# The distribution of voting in 2008 across highest degree
gss_temp = subset(gss, !is.na(degree))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(degree)) +
    geom_bar(aes(fill = pres08), na.rm = TRUE, alpha = 0.3) + 
    labs(title = "The distribution of voting in 2008 across highest degree", x = "highest degree", y = "num of paricipants")  +
    scale_fill_discrete(name = "voting") +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-3-2.png)

``` r
# The distribution of voting in 2008 across income
gss_temp = subset(gss, !is.na(income06))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(income06)) +
    geom_bar(aes(fill = pres08), na.rm = TRUE, alpha = 0.3) + 
    labs(title = "The distribution of voting in 2008 across income", x = "income", y = "num of paricipants")  +
    scale_fill_discrete(name = "voting") +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-3-3.png)

-   Mixed analysis

After exploring demographic variables individually, I try to combine them together to validate my discovery in the previous plots. Actually, there does not exist fundamental differences between people voting for Obama and people voting for McCain. In general, people with higher income as well as higher education degree tend to vote for McCain; people who are white and married are more likely to vote for McCain. In other words, Obama received supports from relatively lower income, lower education background, black and single population.

``` r
# Voting for 2008 scatterplot of income vs age by degree
gss_temp = subset(gss, !is.na(age))
gss_temp = subset(gss_temp, !is.na(income06))
gss_temp = subset(gss_temp, !is.na(pres08))
gss_temp = subset(gss_temp, !is.na(degree))

ggplot(gss_temp, aes(age, income06, color = pres08), alpha = 0.5) + 
    geom_jitter() +
    facet_grid(.~ degree) +
    labs(title = "Voting for 2008 scatterplot of income vs age by highest degree", x = "age", y ="income", color = "voting")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.y = element_text(size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-4-1.png)

``` r
# Voting for 2008 scatterplot of race vs gender by marital status
gss_temp = subset(gss, !is.na(race))
gss_temp = subset(gss_temp, !is.na(sex))
gss_temp = subset(gss_temp, !is.na(pres08))
gss_temp = subset(gss_temp, !is.na(marital))

ggplot(gss_temp, aes(race, sex, color = pres08), alpha = 0.5) + 
    geom_jitter() +
    facet_grid(.~ marital) +
    labs(title = "Voting for 2008 scatterplot of race vs gender by marital status", x = "race", y ="gender", color = "voting" ) +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.y = element_text(size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-4-2.png)

From the discussion above, we can summarize that this sample of General Social Survey is not a well-represented sample of the American society. Therefore, attention is needed in the following process of analyzing the data.

#### Attitude

For this part, I selected some interesting variables to explore.

-   Should Government Reduce Income Differences?

While a lot of participants agree that government should reduce income differences, others don't. Some poeple even strongly believe that government shouldn't do so.

I am curious what kind of people will hold this opposing view. Plotting income and attitude of equal wealth together, we can observe that participants with the highest income are the most likely ones to disagree with the argument, which makes sense because the rich prefer to defense their own interest. However, those who are the most eager to reduce the income inequality are middle-income groups. Perhaps it is because middle class have more contact with rich people, and they feel unfair more easily compared to the poor.

``` r
# Should Government Reduce Income Differences?
gss_temp = subset(gss, !is.na(eqwlth))
ggplot(gss_temp, x = eqwlth) +
    geom_bar(aes(eqwlth), na.rm = TRUE, fill = "blue", alpha = 0.3) + 
    scale_x_continuous(breaks = seq(1, 7, 1)) + 
    labs(title = "The histogram of 'Should Government Reduce Income Differences'", x = "Agree to Disagree", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-5-1.png)

``` r
#Attitude of equal wealth across highest degree
gss_temp = subset(gss, !is.na(eqwlth))
gss_temp = subset(gss_temp, !is.na(degree))
ggplot(gss_temp, aes(degree)) +
    geom_bar(aes(fill = factor(eqwlth)), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude", labels = c("Agree", "", "", "No difference", "", "", "Disagree")) +
    labs(title = "Attitude of equal wealth across highest degree", x = "highest degree", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6))
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-5-2.png)

``` r
#Attitude of equal wealth across income
gss_temp = subset(gss, !is.na(eqwlth))
gss_temp = subset(gss_temp, !is.na(income06))
ggplot(gss_temp, aes(income06)) +
    geom_bar(aes(fill = factor(eqwlth)), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude", labels = c("Agree", "", "", "No difference", "", "", "Disagree")) +
    labs(title = "Attitude of equal wealth across income", x = "income", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 6))
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-5-3.png)

-   Attitude towards communists

In terms of ideology, communism is the strongest competitor for capitalism. Interestingly, participants' attitude become softer from "allow communists to speak", "should communist teacher be fired" to "Allow communist books in library". Maybe the rights of speaking and expressing is the most valuable in the hearts of participants.

If we put these attitude answers along with political views and voting for 2008 together, it is easy to find out that people with moderate political views have similar aggressive opinion with people holding conservative views. This finding is extremely interesting, as people claim to be "moderate" are not honestly objective, and they have a relatively lower tolerance towards communists.

I also used the mixed analysis in this part. For people who in the "not allowed" group with moderate and conservative political views, they are really different. The former group liked Obama, but the latter one loved McCain. So it seems that Obama won the heart of people with moderate political views, despite they might have similiar behavior patterns like conservatives.

``` r
# Attitude of 'Allow communists to speak' across political views
gss_temp = subset(gss, !is.na(spkcom))
gss_temp = subset(gss_temp, !is.na(polviews))
ggplot(gss_temp, aes(polviews)) +
    geom_bar(aes(fill = spkcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Allow communists to speak' across political views", x = "political views", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-6-1.png)

``` r
# Attitude of 'Allow communists to speak'  across voting in 2008
gss_temp = subset(gss, !is.na(spkcom))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(pres08)) +
    geom_bar(aes(fill = spkcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Allow communists to speak' across voting in 2008", x = "voting in 2008", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-6-2.png)

``` r
# Attitude of 'Should communist teacher be fired' across political views
gss_temp = subset(gss, !is.na(colcom))
gss_temp = subset(gss_temp, !is.na(polviews))
ggplot(gss_temp, aes(polviews)) +
    geom_bar(aes(fill = colcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Should communist teacher be fired' across political views", x = "political views", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-6-3.png)

``` r
# Attitude of 'Should communist teacher be fired'  across voting in 2008
gss_temp = subset(gss, !is.na(colcom))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(pres08)) +
    geom_bar(aes(fill = colcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Should communist teacher be fired' across voting in 2008", x = "voting in 2008", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-6-4.png)

``` r
# Attitude of 'Allow communist books in library' across political views
gss_temp = subset(gss, !is.na(libcom))
gss_temp = subset(gss_temp, !is.na(polviews))
ggplot(gss_temp, aes(polviews)) +
    geom_bar(aes(fill = libcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Allow communist books in library' across political views", x = "political views", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-6-5.png)

``` r
# Attitude of 'Allow communist books in library' across voting in 2008
gss_temp = subset(gss, !is.na(libcom))
gss_temp = subset(gss_temp, !is.na(pres08))
ggplot(gss_temp, aes(pres08)) +
    geom_bar(aes(fill = libcom), na.rm = TRUE, alpha = 0.5) +
    scale_fill_discrete(name = "Attitude") +
    labs(title = "Attitude of 'Allow communist books in library' across voting in 2008", x = "voting in 2008", y = "num of paricipants")  +
    theme(plot.title = element_text(hjust = 0.5)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-6-6.png)

``` r
# Voting for 2008 scatterplot of attitude towards communists vs income by political views
gss_temp = subset(gss, !is.na(spkcom))
gss_temp = subset(gss_temp, !is.na(income06))
gss_temp = subset(gss_temp, !is.na(pres08))
gss_temp = subset(gss_temp, !is.na(polviews))

ggplot(gss_temp, aes(spkcom, income06, color = pres08), alpha = 0.5) + 
    geom_jitter() +
    facet_grid(.~ polviews) +
    labs(title = "Voting for 2008 scatterplot of attitude towards communists vs income by political views", x = "Allow communists to speak", y ="income", color = "voting")  +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(axis.text.x = element_text(size = 6), axis.text.y = element_text(size = 6)) 
```

![](assignment7_test_files/figure-markdown_github/unnamed-chunk-6-7.png)

To summarize, it can help us discover more details bycombing demographic information and attitude questions. The conclusion is here:

-   Rich people want to defend their own interest, but middle-income people seek for income equality.

-   People with moderate political views are not as objective as they seem to be; in general, they love Obama.
