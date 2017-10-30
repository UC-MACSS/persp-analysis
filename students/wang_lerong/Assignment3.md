---
title: "Assignment 3 Proposing an Experiment"
author: "Lerong Wang"
date: "10/30/2017"
---

## Introduction

Online ratings occur in all kinds of websites nowadays, and nearly everything can be rated online by users and customers. Customers give ratings after their online shopping experiences; users rate their experience after using a mobile application; people also tend to rate and give reviews to the films they have watched. However, social influence may occur during their rating processes. Social influence occurs when a person’s emotions, opinions, or behaviors are affected by others (Wikipedia contributors). I am interested in how likely people’s rating processes will be affected by the social influence from others, so in this assignment, I plan to take film ratings as an example and study how people’s rating behaviors are affected by prior film ratings by conducting a computationally-enhanced experiment, and I will specify the research questions in the section below.  

## Specific Research Questions

1. Whether prior film ratings will affect people’s rating behaviors or not? 
2. Are people more likely to be influenced by prior negative film ratings or positive film ratings?
3. How people in different age group differ in their tendency to be affected by prior film ratings? (Different age groups are divided by the following criterion: age 18-25, age 25-35, age 35-45, age 45-55, age 55 or older)

## Basic experiment design
I will be using between-subjects design in this experiment.

### Recruitment of participants
The process of recruiting participants is digitally-enhanced. I plan to use Amazon Mechanical Turk (MTurk) to recruit participants. Participants who are selected to participate in this experiment will be asked to complete the first survey of their age group and whether they have watched the three films that we will be given later in this experiment. For those who have not watched all three films, they are selected to continue the experiment. For this experiment, I plan to recruit about 500 participants. The experiment will be given in the form of a survey which is embedded with a short film, and participants will be asked to rate the film after they finish watching the film. There are three surveys in total and will be given in three consecutive weeks. Each survey will take approximately 1 hour. The films in the three surveys fall into the category of above-average IMDb rating, average IMDb rating, and below-average rating separately.

### Randomization
We will use a computer to randomly assign participants to two groups. The first one is the control group, in which the participants will be given a short introduction about the film before watching. The second one is treatment group, in which the participants will also be given an introduction to the film, but a more comprehensive introduction which includes the average rating of the film on IMDb. 

### Delivery of treatment
The treatment will be delivered in the survey by giving the participants relevant information about average film ratings on IMDb.

### Measurement of outcome
In this assignment, I consider three specific questions related to the effects of prior film ratings on people’s rating behaviors. Before answering these three questions, I will first compute the mean and standard deviation of film ratings I obtained in the survey. 
The first question is whether prior film ratings will affect people’s rating behavior or not. We can measure the outcome by comparing the difference between the average ratings of the control group and average IMDb rating, and the difference between the average of ratings of the treatment group and the average IMDb rating. Then we can perform a two-sample t-test in R for the average of treatment group ratings and average of IMDb ratings. If the difference between the average ratings of the treatment group and the average IMDb rating is rather small compared to the difference between the average rating of the control group and average IMDb rating, then prior ratings are more likely to affect people’s rating behavior. Moreover, by comparing the p-value we get from our hypothesis test, we can also infer whether people in the treatment group are affected.
The second question is whether people are more likely to be influenced by positive ratings or negative ratings. Since there are three surveys in total, and the film included in the first survey has above-average IMDb ratings, the one included in the second survey has average IMDb ratings, and the one included in the last survey has below-average ratings, we can measure the outcome of the second questions by comparing the difference between average ratings in treatment group and average IMDb ratings under these three conditions. 
The third question, which is about how the rating behaviors of different age group will differ based on prior ratings, can be measured by comparing the difference between the average ratings in different age groups in the treatment group and the average ratings on IMDb separately.

## Assessment of the experimental design

### Validity
In this experiment, we can ensure statistical validity by choosing the appropriate statistical measurement and hypothesis test. Internal validity centers around whether the experimental procedures were performed correctly (Salganik, 2017). I think this experiment has strong internal validity. Before the experiment officially starts, participants will be asked if they have watched the three films which will be shown in the survey later to ensure the reliability of the results and minimize confounding variables. Recruiting participants and randomization are both done digitally to minimize the confounding factors. We also ensure that the only difference between the control group and treatment group is that treatment groups will be given information about the average ratings on IMDb. Construct validity is warranted in this experiment because the data we collected matches what we want to analyze fundamentally. 

For external validity, the best situation will be that the results of this study on film ratings can generalize to other rating situations. However, the external validity may be a potential problem for this experiment because we don’t know how the film in this experiment can be comparable to products or experience in other settings. For example, an individual’s understanding of certain film may require some basic knowledge of history, which means the film may not be understandable by everyone; however, the user experience of the product does not require comprehension ability, so it’s more likely that people may not conform with others while rating their user experience.

### Measure heterogeneity of treatment effects
We want to measure how prior film ratings may affect people’s rating behaviors generally, but there might be differences in how people in different age group respond to prior ratings. For example, older people who have more life experience may be more likely to trust their feelings, and younger people who cannot thoroughly understand the theme of the film may be more likely to rate based on prior film ratings. Therefore, I specified different age group by letting participants filling out their age groups at the beginning of the experiment, and analyze whether age plays a role in their rating behaviors.

### Mechanisms
The ultimate goal of this experiment is to see whether social influence can affect how people give their ratings. In this experiment, we only have one treatment which is to provide relevant IMDb ratings on the film introduction page, and this is the only difference between the control group and treatment group. Thus, if the analyzation of the experiment concludes that prior film ratings can affect people’s rating behavior, then there’s only one mechanism accounts for this effect, which is the social influence from others.



## References

“Social influence.” Wikipedia, Wikimedia Foundation, 25 Oct. 2017, en.wikipedia.org/wiki/Social_influence.

“Bit By Bit: Social Research in the Digital Age.” Bit By Bit: Social Research in the Digital Age, www.bitbybitbook.com/.



