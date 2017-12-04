Exploration Write-Up
================
Nora Nickels
11/27/2017

Assignment 7 - EDA
==================

Perspectives of Computational Analysis - Fall 2017
--------------------------------------------------

Exploration Write-Up
====================

Introduction
------------

For my exploration write-up, I focus on two different topics based on what I learned from my exploratory data analysis: 1) how does family size, in terms of children and number of siblings, vary with both religious denomination and reported strength; and 2) what subjective confidence in national systems (e.g., business, medicine) varies with reported subjective happiness?

    ## Warning: package 'ggplot2' was built under R version 3.3.2

    ## Warning: package 'knitr' was built under R version 3.3.2

Family size and Religion/Faith
------------------------------

When performing exploratory data analysis looking at the variable of family size, in terms of number of children and number of siblings, I began by hypothesizing what data in the GSS survey may vary with differences in small and large families. After some preliminary analyses looking at factors such as age and race, I took a look at how religion beliefs and the strength of these beliefs may affect family size individuals grew up and the number of children they decide to have. Based on the two bar graphs below, it does seem to be the case that certain religous faiths may vary with larger family sizes. Religions such as Islam and Native American seem to have some of the highest average sized families, in terms of average number of siblings and average number of children. Religions such as Hinduism are on the smaller end of the spectrum, while Christian and Catholic families seem to fall in the middle of the road. By graphing these as the average number of siblings/children, we seem to remove some of the outliers; particularly with number of siblings, there were some outlying families that had 20 to 30 siblings, which seem to be fairly extreme cases of large families. Overall, it does make sense that religious beliefs may vary with family size, as often time religious denominations play into the decisions of parents in terms of family size.

![](Exploration_Write-Up_files/figure-markdown_github/Write-Up%201-1.png)![](Exploration_Write-Up_files/figure-markdown_github/Write-Up%201-2.png)

What varies with subjective happiness?
--------------------------------------

Another variable from GSS I found interest in was subjective happiness. There were multiple variable that looked at subjective confidence in various national agencies. I explored the variance of subjective happines groups with these confidence levels. Overall, there does not seem to be much of a pattern looking at how subjective happiness fluctuates with confidence in financial institutions, religious institutions, medicine - even tv programming. Below is a graph that looks at the makeup of subjective happiness groups over the groups who have different compentence in major business companies. This was the only variable in which individuals who had a great deal of confidence in these institutions had a slightly different makeup of happy individuals. Specifically, it does seem that individuals with the most confidence contain a higher proportion of very happy people. However, I take all these analyses that look at subjective happiness with a grain of salt; these different institutions mean different things to different people, and an exploratory data analysis looking at varying patterns in happiness and confidence in these institutions by no means confirms correlation. Overall, I found these subjective ratings interesting to observe.

![](Exploration_Write-Up_files/figure-markdown_github/Write-Up%202-1.png)
