---
title: "Assignment 5 Collaboration"
author: "Lerong Wang"
date: "11/13/2017"
---

## Kaggle open call projects

### Create an account with Kaggle.com
I created an account with Kaggle and my user name is lwang11.

### Explore the Kaggle competitions page
The Kaggle competition that I am interested in is New York City Taxi Trip Duration. The goal of this competition is to build a model that accurately predicts the duration of taxi trips in New York City. 
The evaluation metric for the competition is Root Mean Squared Logarithmic Error (RMSLE). For the submission file, I need to have two columns for every row in the dataset, the first is id, which corresponds to the id in the column of id in test.csv file and the second is trip duration that's calculated based on the model I build. The file must also contain a header and have the following format:

id,trip_duration
id00001,978
id00002,978
id00003,978
id00004,978
etc.

### Explore the Kaggle datasets page
The dataset I explored on Kaggle is Student Alcohol Consumption. There are two csv files in the original file that I downloaded from Kaggle, and I used the student-mat.csv file, which is the data from students in math course. The scripts and plots are shown in the ipynb file.

## Improving a journal article
The research paper I choose to reformulate in this section is “The Role of Mindfulness in Romantic Relationship Satisfaction and Responses to Relationship Stress” published in the Journal of Marital and Family Therapy. Mindfulness, which is defined as an open or a receptive attention to and awareness of what is taking place, both internally and externally, in the present (Brown & Ryan, 2003), has been shown in some past research that may contribute to increasing the quality of romantic relationships by indirectly showing that mindfulness is associated with several positive interpersonal behaviors and traits such as openness, relatedness, interpersonal closeness, and good social skills. However, it’s not clear from past research whether mindfulness itself is an active ingredient in promoting positive relationship outcomes. The current research paper considers the association between the role of mindfulness in romantic relationship and responses to relationship stress (Barnes et al. 2007).  

I will briefly describe the original research design in the paper, mostly on the data collection part. There are two studies in this paper. The first study was designed to test the two hypotheses in this paper, which are mindfulness has a positive relationship with romantic relationship satisfaction, and mindfulness is positively related to the capacity of dealing adaptively with romantic relationship stress. Participants in this study, who must be dating when conducting this research, were recruited from a large southeastern U.S. University. The study was a short-term longitudinal study that measures the relevant constructs twice, ten weeks apart. Mindfulness Attention Awareness Scale was used to measure mindfulness scale of participants; Dyadic Adjustment Scale and Investment Model Scale was used to measure romantic relationship satisfaction. For measuring the capacity of dealing adaptively with romantic relationship stress, the researchers chose to measure Self-Control Scale and Accommodation scale.

The purpose of the second study was to replicate the basic findings of the first study and to conduct a more comprehensive test of the hypothesis related to the role of mindfulness in dealing with romantic relationship stress. Sixty heterosexual couples from a small northeastern U.S. university were recruited for this study. Before the study, they will complete trait and relationship measures. Couples were asked to come to the laboratory without interacting with each other for 6 hours before the lab. Then there is a five-phase interaction sequence, which includes sitting quietly and relax without talking to each other, discussing daily events of the current day, which is recorded, pre-conflict mood assessment and generating conflict topics, sitting quietly and relax without talking to each other again, and finally discussing the conflict topic generated before, which is also recorded. Before leaving, they will also be asked to complete a post-conflict discussion measures. Similar to the first study, the trait and romantic relationship background were measured by researchers using Mindful Attention Awareness Scale and Dyadic Adjustment Scale. However, the pre-conflict discussion measures and post-conflict discussion measures were added and made the study more thorough than the first study on the role of mindfulness in dealing with relationship stress. 

To reformulate the research topic as a human computation project, I will use Amazon MTurk to recruit participants. Since the purpose of the second study in the paper is to replicate the findings in the first study and further verify the relationship between mindfulness and the capacity to deal adaptively with romantic relationship stress, I plan to combine the original two studies into one study. Roughly 500 participants will be recruited, and like the original design, one of their qualifications must be currently dating with others or in a relationship. I will give online surveys and measurements of different constructs to participants, and these will be given each day for two weeks consecutively. Before they start their two-week survey, and they will need to complete some preliminary questionnaire and assessment, which will include Mindful Attention Awareness Scale and Dyadic Adjustment Scale. After they officially begin their two-week study, their everyday survey and assessment will include some questions that are listed below.
1. Please indicate on a scale of 0 to 5, with 5 being most satisfied and 0 being least satisfied, how satisfied are you with your relationship today?
2. Did you and your partner discuss the events of your day with each other?
3. Did you and your partner have conflicts today?
4. If yes, please briefly discuss what happened?

If the answer to question 4 is yes, then after the participants completed the daily survey, they will be given the Post-conflict Discussion Measures, and a survey about their mood change before, during and after the conflicts. 

By reformulating the research as a human computation project, there are several advantages compared to the original research method. First, more participants will be recruited, and the sample population will be more diverse. The original research question in this paper does not restrict the topic to college students, but the data collections in the paper were completed in several U.S. universities, so we don’t know whether the result can accurately predict the role of mindfulness in romantic relationship satisfaction and the capacity of dealing with relationship stress among population in all age groups with different occupations. Second, being asked to talk about a conflict topic in front of a camera may be an unnatural setting in this paper and couples’ reaction may be different from the situation that a conflict happens naturally. In my research design, I asked participants to talk about the conflicts that happen naturally in the realistic setting so that we can measure the mood change more accurately. Finally, in study one of the original method, relevent constructs were measured twice, ten weeks apart, and in study two, couples were asked to come into the laboratory for only once. However, in my research design, the study is given to participants every day for a two-week period so that the short longitudinal study will capture some constructs such as mood change and self-control after conflicts more dynamically and accurately.


## Amazon Mechanical Turk
Since my Amazon Mechanical Turk account is still under review and Benjamin said, "If you are aware of one that you can legally participate on, feel free to use that site instead of MTurk - again, completing an hour's worth of micro-task assignments." I did an alternative one using Baidu test, which is a Chinese website, and completed several surveys. 

### Proof

<img src="../Assignment5/Mturk.png" width="500" height="300">


## References
1. Barnes, Sean, et al. “The role of mindfulness in romantic relationship satisfaction and responses to relationship stress.” Journal of Marital and Family Therapy, vol. 33, no. 4, 2007, pp. 482–500., doi:10.1111/j.1752-0606.2007.00033.x.

2. Brown, K. W., & Ryan, R. M. (2003). The benefits of being present: Mindfulness and its role in psychological
well-being. Journal of Personality and Social Psychology, 84, 822–848.



