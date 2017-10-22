# Planning and Game Addiction: An Empirical 

**Zhiyu Fu**

Computer games are increasingly popular among adolescents and young adults. However, though with positive effects, it creates non-negligible educational and psychological issues and thus raises the concerns over its overuse. Due to the increasing awareness of excessive game playing, why people are addicted to these games is becoming an important research issues, and several hypotheses attributing the addiction to personality characteristics are postulated. Some previous studies suggested aggression, as an individual characteristics, is one of the main factors for addiction and also reinforced by some computer games (for example, see Gentile etc., 2005). Some research also identified poor self-control may increase the possibility of addiction in games (Baumeister, 2003).

Nevertheless, personality traits may not be the whole picture. Cognitive or metacognitive concepts may be also involved in the process of addiction. That is, addiction may be due to the failure in executive functions (or cognitive control, Sternberg, 1985), in particular, metacognitive planning. Metacognitive planning refers to the high order process where individuals set short-term and long term goals and form and select strategies to achieve these goals (Schraw & Moshman, 1995). We hypothize that one could be addicted to games not because he or she is willing to, but he or she failed to make and maintain a valid plan regarding game playing. There are few studies exploring the association between planning and game addiction. In this study, we try to empirically test our hypothesis. 



## Method

### Subjects

We plan to collect survey data from players of games produced by Tencent. The platform to collect data is Wechat, a social network app also developed by the same company. It is similar to Facebook in terms of the their dominance in respective market and features. We can push our survey to the timeline of game players via Wechat (if funding is sufficient), and encourage Wechat users to share it to their friends. As discussed in the following, it would be most approporiate to collect data from game players through the internet, especially via Wechat. 

Besides, in order to enlarge our sample size to obtain better external validity, we plan to implement an amplified-asking paradigm to make use of existing digital trace data.


### Instrument

There exist mature scales to measure game for addiction and planning already. For game addiction, we plan to use Whang's (2002) Online Game addiction Scale; for planning, we plan to use Scale for Self-Rated Metacognitve Planning (SRMP), developed by Schraw (1995). Sample questions are attached in the appendix. Nevertheless, these traditional questionare-based scales are not built for spreading on the internet, and thus we have the following procedures to augmentation.

For game addiction, we plan to utilize the game-playing data of Wechat users to amplify the survey. Wechat and games from Tencent share the same account, so the data is linked. Wechat provides special APIs so that with authorization from users, we can get access to their game-playing information, such as playing hours per week for each game developed by Tencent. 

We plan to use a gamification strategy proposed by Li etc. (2014) to augment the questionare-based assessment of planning. Respondents will be asked to play a classic video game Sokoban. Sokoban is a transport puzzle, in which players need to push boxes into the certain destinations. Figure 1 presents a screenshot of the game. In our study, there are 10 items in total at varied levels of difficulty. The log files of the specially designed game program will record detailed information including subjects' every move, time between each move, and the result of each game. After analyzing the log-file data, Li etc. (2014) found the ratio between planning time before the first move and the total time in a game is positively correlated with scores of metacognitive planning scale. Due to their limited sample size, they did not fit the log-file data to sophisticated models to achieve better prediction power, which becomes possible in our internet-based studies. 

![A Screenshot for Sokoban](game.png)
### Procedure

We will push a survey to game players on Wechat. In the post we claim it is a game-based measurement, which is true and makes it more attractive. Before they start playing the game, we will also ask respondents for the access to their game-playing data. After subjects finish Sokoban game, we will invite them to fill a simple survey including questions about demographic factors, Online Game Addiction Scale, and Self-Rated Metacognitive Planning Scale. After the completion of whole survey, they are encouraged to share the survey to their friends. They can exist at any time during the whole process. 

We expect that most respondents will exist after they complete the game, but there also will be a proportion of respondents who complete the whole survey. We can perform supervised learning on these complete observations. We could estimate a model to predict game addiction from Tencent's game-playing data, and another one to predict planning from sokoban log files. With estimated models, we can impute the missing survey scores for those incomplete observations.

After the imputation, we can do the correlation analysis on the survey scores and test our hypothesis about the assiociation between game addiction and planning. 



## Discussion

This research is fully digitalized. The sample is random picked through the internet, a part of the survey is an interactive game, and we also use digital trace data to amplify the survey.

It is suitable to conduct this research online, especially with Tencent. Tencent is the largest game company in China. For example, one of the most famous game it produced, *king of glory*, has attracted 200 million players in China alone and aroused the most addictions. Furthermore, Wechat is also the largest social network app in China with more than 900 million users. It is fair to assume almost all game players in China use Wechat and have tried Tencent's game at one time. Therefore, limiting our sampling frame to players of Tencent's games via Wechat will only influence our inference to a very little extent.

Our research also benefits from the internet-based sampling. In a traditional offline survey, it is very difficult to reach a specific group, which, in our case, is game players. With the shared data between Wechat and games from Tencents, we can speficially push our survey to the players' timeline instead of all the population, which greatly saves resources. With the gamification techniques and amplified-asking strategy, together with the spreading effect of social networks, we can greatly enlarge our sample size to obtain a more general result.

An observational study will not be as effective as our approach for topic. For example, the game-playing data from Tencent is a typical observational dataset, but we cannot directly use the it to construct index for addiction. The problem lies in the subtlety that addiction is always related to individuals' internal feelings and certain extent of disorders in life, study or work, and can never be defined solely by explicit behaviors toward games. Even observed long playing hours everyday does not necessarily imply addiction. For metacognitive planning, without special designed tools, it is difficult to estimate from observational data, because to in almost any real-life tasks, a combination of metacomponents instead of a pure single component are involved. Therefore, a survey-based study suits this topic best.

The main source of errors, as in typical psychological research, is from the measurement. It is always tough to precisely measure psychological concepts. Nevertheless, thanks to the existing mature scales, the measurement errors are under control in our study. Furthermore, the potentially large sample also minimize the random error from measurement. Another kind of measurement error may arise when we use digital trace data to amplify the survey data. It highly depends on the fit of the models so it is hard to give a conclusion in advance. However, we could do the analysis based on the imputed data and the original data respectively.

Representativeness will not be a big concern for our study. As we illustrated, restricting our sampling frame will not impair the representativeness, due to the popularity of Tencent's products. Besides, even the selection biases exist, it will primarily affect the estimation of means. No strong evidence or reason suggests the selection based on responsiveness or sampling frame will will have huge influence on the estimation of correlation between addiction and planning.





### Appendix: Sample Questions

For the following items, participants response in a 7-point Likert scale indicating the extent to which they agree with the statement.

### Game Addiction

1. My school work or occupational functions suffer because of the amount of time I spend playing online games.
2. I find myself saying ‘just a few minutes’ when playing online game.
3. I have acted annoyed if someone bothers me while I am doing online game.

### Metacognitive Planning

1. I set specific goals before I begin a task.
2. I hardly failed to fulfil my plan.

## Reference
- Schraw, G., & Moshman, D. (1995). Metacognitive theories. Educational Psychology Review, 7, 351–371. doi:10.1007/BF02212307
- Li, J., Zhang, B., Du, H., Zhu, Z., & Li, Y. M. (2014, September 15). Metacognitive Planning: Development and Validation of an Online Measure. Psychological Assessment. 
- Veenman, M. V. (2011). Alternative assessment of strategy use with self-report instruments: A discussion. Metacognition and Learning, 6, 205–211. doi:10.1007/s11409-011-9080-x
- Gentile, D. A., & Stone, W. (2005). Violent video game effects on children and adolescents. A review of the literature. Minerva pediatrica, 57(6), 337-358.
- Baumeister, R. F. (2003). Ego depletion and self‐regulation failure: A resource model of self‐control. Alcoholism: Clinical and Experimental Research, 27(2), 281-284.
- Sternberg, R. J. (1985). Beyond IQ: A triarchic theory of human intelligence. CUP Archive.
- Trimmel, M., & Köpke, E. (2000). Motivations to control drinking behavior in abstainers, moderate, and heavy drinkers. Pharmacology Biochemistry and Behavior, 66(1), 169-174.
- Whang, L.S. and Chang, G.Y. Psychological analysis of online game users. (81–90)Proceedings of Human Computer Interaction 2002 Korea. vol. 2. ; 2002
- Schraw, G., & Moshman, D. (1995). Metacognitive theories. Educational Psychology Review, 7, 351–371. doi:10.1007/BF02212307
- Hadwin, A. F., Nesbit, J. C., Jamieson-Noel, D., Code, J., & Winne, P. H. (2007). Examining trace data to explore self-regulated learning. Metacognition and Learning, 2(2-3), 107-124.
