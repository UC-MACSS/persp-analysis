## ### Assignment3: Gender Difference In Self- And Other-Competition
### 
### Siyi Fan

** **



## **Introduction**

​      Prior researches suggest that men tend to be more overconfident than women, even if they are all overconfident about their performances (Barber & Odean, 2001). This phenomenon could be explained in a social-developmental way. It is common that girls and boys are raised differently in society. Boys are directed to play competitive games, while girls are directed to select activities where there is no winner and no clear end point; boys are encouraged to be assertive, while girls are encouraged to be gentle and modest. In a long term, girls grow to be relatively reluctant to perform in competitions and it also explains why men often feel confident in their performances. However, it may be task dependent, depending on the perception of our tasks. Moore and Small (2004) found that gender difference in overconfidence has primarily been showed in masculine tasks. 

​      Besides, research on gender differences in willingness to compete has exclusively focused on against others. Therefore, I consider to examine another type of competition: competing against one’s own self, which mainly stresses on self-improvement and goal-setting. 

​      To do so, I will use a controlled laboratory experiment to investigate whether men and women differ in the willingness to compete against themselves (self-competition) and against others (other-competition). I will further explore the role of confidence underlying the differences in online market experiment by using a computationally enhanced way. 



## **Research Questions**

1. Is there a gender difference in the willingnessto self-compete? 
2. Is there a gender difference in the willingnessto other-compete? 
3. If the role of confidence could be a mechanismunderlying the gender difference in the willingness to self-competition?
4. If the role of confidence could be a mechanismunderlying the gender difference in the willingness to other-competition?




## **Experimental Design**

##### ***Laboratory experiment***

​      Participants will be recruited through Facebook ads and other social media ways (e.g., WeChat). They will be randomly assigned to *Other* treatment group and Self treatment group. I will ensure there are the same amount of male and female participants in eachgroup. 

​      I will conduct an experiment in which participants solve pattern recognition game. The test consists of 8 questions to be solved in 3 minutes. In each test item, the participants are asked to find the missing pattern in a series. The items get progressively harder, thus requiring greater cognitive capacity to analyze and solve. The whole experiment will be programmed in Z-Tree (Fischbacher, 2007) and conducted at the psychology building. 

​      First, I will display an example of pattern recognition game to subjects.

![../../../.Trash/Screen%20Shot%202017-10-27%20at%2019.56.13](file://localhost/Users/fansy/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image002.png)

​      After that, all subjects will be asked: 1. How experienceare you with pattern recognition game like this (1=No experience; 7=Expert)? 2. To what extent are you motivated to do well on this task (1=Not at allmotivated; 7=Extremely motivated)?

​      In the *Other*-treatment, subjects will take three rounds, each round consisting of 8 questions to be solved in 3 minutes. There will be no feedback between rounds. The questions will look like this (Upper=the easiest question; Lower=the hardeset question): 

![../../Screen%20Shot%202017-10-27%20at%2020.01.18.png](file://localhost/Users/fansy/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image002.png)

![../../Screen%20Shot%202017-10-27%20at%2020.01.36.png](file://localhost/Users/fansy/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image004.png)

​      In the first round, subjects will be paid a fixed amount of money for every correct answer. In the second round, the participants will be told that they are matched in pairs and the one with the higher score will be paid double for every correct answer, while the other subject will receive nothing. In the third round, subjects will pick one scheme introduced in the first and second round. For the first scheme, they will be paid for how many questions they solve correctly; for the second scheme, their bonus will mostly depend on their competitors’ performances, also with the risk of getting nothing. 

​      In the *Self* treatment, the experiment procedure is identical with the following exceptions: 1) the subjects will not be told to match in pairs; instead, their scores in the second round will be compared to their own scores in the first round; 2) when participants make a choice of the schemas applied to the third round, the second schema means that their score in the third round will be compared to their own score in the second round.  If the score in the third round is higher than the second round, they will get double bonus. Otherwise, they will get nothing. To be clear, participants don’t know their performances for each round during the experiments. 

​      After three rounds, all subjects will fill out a questionnaire on basic demographics and be asked to guess whether they outperform their opponents for the *Other* treatment group. For the Self treatment group, subjects will be asked to rank their own performance across the rounds. These questions provide measures of confidence.  

##### ***Online experiment***

​      I will use the labor market Amazon Mturk to ensure the results from the laboratory replicate and further explore the mechanisms underlying the laboratory findings. Specifically, there are two more groups in addition to the *Other* treatment. One is *Other-Same gender* group. Participants will be told that they are matched with the same gender in the second round competition. The other is *Other-Same score* group. Subjects will be informed that their competitors share the same score with them in the first round. 



## **Results**

​      I will do statistics summary and additional analysis by using R, specifically for collecting basic data like below two panels, calculating *p*-values for gender differences, probit regressions for the schema decisions, and OLS regressions for the gender differences in schema decisions. 

![Screen Shot 2017-10-29 at 21.19.50](/Users/fansy/Desktop/Screen Shot 2017-10-29 at 21.19.50.png)

 ![Screen Shot 2017-10-29 at 21.20.28](/Users/fansy/Desktop/Screen Shot 2017-10-29 at 21.20.28.png)



## **Study Considerations**

​      This study combines lab and digital experiments, both using digital infrastructure to recruit participants, deliver treatments, and measure outcomes. The laboratory experiment offers total control of the environment in which participants solve pattern recognition game and make a choice of the schemas. While at the same time, z-Tree could replace human time with computer time and collect rich data without much cost. Online experiment could replicate the gender-gap in the laboratory experiment and further reveal the mechanisms underlying this difference. 

​      In this study, statistical conclusion validity will be satisfied, because all data will be collected in a digital way and be analyzed on R which is available for multiple examinations. Z-Tree is a toolbox for most economic experiments, which is stable and allows almost any kind of experiments in a short time. It could show graphics by adding a “plot box” and display texts defining a so-called “chat box”. After the experiment, menu commands in z-Tree uses one text file containing tab separated tables to store the data, which can directly be imported into R or spreadsheet programs. For the online experiment, participants will be recruited through MTurk. Even if it provides a convenient platform to recruit a large number of subjects, there are two main concerns on its internal validity (Berinsky, Huber & Lenz, 2012). The first one is the same subject could participant in this experiment more than once. Addressing on this concern, I will assess the prevalence of subjects participating in the same MTurk HIP by using different user accounts. The second concern is that without laboratory control, subjects may lose their attention or interest on the task. Addressing on this threat, I will assess subject attentiveness at the end of the experiment and set pilot study to make sure that each pattern recognition is neither too easy nor too hard to most people. 

​      As for external validity, our findings in either laboratory or online experiment may not be able to extend to the real world, because we only use a pattern recognition game to examine gender differences. But in the real world, behavior competition may involve more domains, such as: STEM categories in education, workplace competition, and negotiation. To the extent that negotiation can be viewed as a two-person competition, their results may be consistent with my research findings. But for education, it mostly depends on the social environment. Negative aspects of schools’ climate and lack of social support will all force individuals to avoid competitions or even fail to compete, not simply because of low self-confidence or other personal reasons. 

​      The strength of this study is to reveal the mechanisms underlying the gender differences. Online experiment allows me to collect more process data and test many related treatments. For online experiment, I test four groups: other-treatment, other-same gender treatment, other-same score treatment, and self-treatment. Other-same score indicates that receiving a signal that the opponent has the same ability akin to one’s own, which is similar to self-competition. There is a possibility that women may shy away from competing with others, because they are less sure about if they can win the competition (less confidence compared to men overconfidence), however, women may prefer to compete against themselves or against other women. The reason may be that female opponents have a positive reinforcement on boosting women’s confidence in their ability to perform. Therefore, many underlying mechanisms can lead to the gender differences and digital experiments may help to reveal those mechanisms and get each combination tested. 

​      Even if I use a controlled laboratory experiment to examine individual choices in a nondiscriminatory environment, that is, men and women have equal opportunity to select any schema without under social pressure, heterogeneity caused by education level and age may happen to both laboratory experiment and online experiment. People who use Facebook and MTurk are relatively young with advanced thoughts and have a high education, so female subjects could perceive themselves as competitive as male and male may focus more on self-improvement. If we recruit another group of subjects offline or in a different cultural background, the same treatment can have different effects on them. 

​      

##  References

Barber, B. M., & Odean, T. (2000). Trading is hazardous to your wealth: The common stock investment    performance of individual investors. *The journal of Finance*, *55*(2), 773-806.

Berinsky, A. J., Huber, G. A., & Lenz, G. S. (2012). Evaluating online labor markets for experimental research: Amazon. com's Mechanical Turk. *Political Analysis*, *20*(3), 351-368.

Fischbacher, U. (2007). z-Tree: Zurich toolbox for ready-made economic experiments. *Experimental economics*, *10*(2), 171-178. 

Small, D. A., & Moore, D. A. Error and Bias in Comparative Judgment: On Being Both Better and Worse than We Think We are.

