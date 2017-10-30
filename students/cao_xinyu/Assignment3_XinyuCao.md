# Racial and Gender bias and Job Market Tightness
Author: Xinyu Cao
Assignment 3

## Research Question
In classical Mortensen & Pissarides (1994) paper, the concept of labor market tightness is job seekers find job more quickly and employers take longer to fill jobs. It is not difficult to imagine, at the time when or the place where the economic situation is severe, the racial and gender bias are more likely to outbreak. In Bertrand and Mullainathan’s (2004) paper, they studied the labor market discrimination using fictional resumes for different jobs posting in Chicago's newspaper. Similar method is used in Doleac & Stein (2013), where they studied the racial bias in online market sale. 

Using their methodology combined with the CVs in the LikedIn and digital methods, I propose a longitude experiment study to analyze following questions: 
1. whether racial and gender biases still exist in labor market? \
This is a question which is fundamental to the second one. Since if we want to study whether labor market tightness will affect the racial and gender biases, we must first study the existence of the biases. We try to measure this issue by the analyze the variations of response rates of similar qualified CVs due to the effects of racial and gender identifiable name. That is to say, we want to measure this discrmination by seeing if Lucas is more to accept response after sennidng the same CV compared to Tyrone.

2. how those biases are affected by labor market tightness? \
In economic downtime, minority suffers the most. For example, Krosch & Amodio (2004) paper documented the effect that the economic resource scarcity causes decision makers to perceive African Americans as "Blacker". We want to use our measure of racial and gender inequality to see if the extent of discrimination is affected by the labor market downwards and upwards, particularly we measure this by the labor market tightness.


## Digital Experiment Research Design
In our experiment, we first generate a standardized CV database according to the CV information posted on the LinkedIn for randomly selected job posting in LinkedIn. And based on those standardized database, we generate a sample of fictional CVs. Using those fictional CVs, we change the name information as the racial and gender treatments. Since other information is randomly selected from a standardized CV database, it is reasonable to assume that the response rates changes of fictional CVs is due to the treatment of the racial and gender information.

1. Randomized CV generalization: \
In our method, we first try to generate a standardized CV database according to the company's typical employee's CV. By saying a standardized CV database, I mean a CV database with a list of typical degree type, a list of typical previous experience, a list of typical language and other skills. Using those standardized CV database, we could randomly generate a sample of CV.

2. Identities Treatment - Rich Experiments: \
After we get a series of randomly generated CVs, we could introduce racial and gender treatment of the fictional CV. Thus, we yield a full factor design. First, we could try to use a racial and gender-neutral name. For example, for racial treatment, we could assign, according to the figure the 2016 population statistic by United States Census Bureau, very White sounding name to 61.3% of the CVs and African-American sounding name to 13.3% of the CVs, when we conduct the first experiment at 2017. Using the similar procedure, we will also do a gender treatment, and a racial and gender treatment. 

3. A Field Experiment Panel Data Collection: \
In order to explore the second component of study, we try to collect a panel data. So that we are able to use the randomization of labor market tightness in different industry to analyze whether those biases are affected by the labor market tightness. Basically, we have an overall labor market tightness across time, and we have a labor market tightness in different industries across time. Although gender and racial bias reduced across time, which is not caused by labor market condition. But changes of gender and racial bias in different industry are likely to be partly caused by the labor market tightness in different industries across time. This variation of the cross industry labor market tightness could help we make the causal inference of racial and gender biases.


## Assessment of the research design
1. Racial and Gender Bias change overtime - Statistical Validity: \
One of the main concern is the racial and gender bias is changed overtime. For example, gender bias in the United States reduced cross time according to Tang et. al (2017) paper. To single out the time variant effects. We will try to exploit the variation of labor market tightness across industry to estimate how local treatment effects. If change of the bias is not systematic correlated with the labor market tightness, then our method suffices the randomization. 

2. Names are related with social background - Internal Validity: \
The second of the concern of source of discrimination of randomly generated name is that it is possible that the employer discriminate against the individual solely by the name hints they comes from a disadvantage social background rather than racial discrimination. For example, if they named a typical black name, employer will infer they come from a disadvantaged social background. Thus, the employer has low responsive rate not because he/she is black, but because he/she comes from a disadvantaged social background. To distinguish between the effects of racial discrimination and the discrimination against disadvantage social and economic background, we could use the social background and name connection results from Fryer and Levitt (2003) paper. In their paper used the birth certificate data for women born in 1973-1974 and for when they give birth themselves in 1989-2000 to estimate the effect of potential Black name might be able to refer the social background.

3. External Validity: \
Since our research results could answer the question if the labor market tightness will affect the extend racial and gender bias. The answer could potentially generalize to all market behavior, is that in any market, for instance car dealer market, the supply and demand tightness, the ratio of potential second hand car and potential buyer, will affect the consumer choice, i.e. to less trust a Black dealer in situation of less demand of second hand car? This could turn into a further research using the same method thanks to the digital field experiment. 

4. Heterogeneity of treatment effects: \
Heterogeneity is taken care by our experimental design. First, I divided the employer into different industries. Second, as the experiment specifies, I developed full factorial analysis for 4 set of experiment of control group, racial treatment group, gender treatment group, and racial and gender treatment group. Third, since people of different age might also have different extent of gender bias, in my experiment, I will take the HR's demographics as control variables to estimate different treatment effects.

5. Causal mechanism: \
Even though we are possible to observe those gender biases from our experiment. But to draw a causal inference of a racial or gender biases should be more careful. There are several alternative explanations to proposed mechanism of racial or gender bias. Because, although employer response differently to the same set of observable signals. It might because that Black people and women benefits from affirmative action, they get those credential in our randomized generated CVs. Therefore, employer value less of the credential in those CVs. 



## Reference
1. Mortensen, Dale T., and Christopher A. Pissarides. "Job creation and job destruction in the theory of unemployment." *The review of economic studies* 61, no. 3 (1994): 397-415.
2. Hall, Robert E., and Sam Schulhofer-Wohl. The Pervasive Importance of Tightness in Labor-Market Volatility. working paper, Stanford University, 2017.
3. Krosch, Amy R., and David M. Amodio. "Economic scarcity alters the perception of race." *Proceedings of the National Academy of Sciences* 111, no. 25 (2014): 9079-9084.
4. Tang, Shiliang, Zhang, Xinyi, Cryan, Jenna, Metzger, Miriam J., Zheng, Haitao, and Zhao, Ben Y. "Gender Bias in the Job Market: A Longitudinal Analysis.", *Proc. ACM Hum.-Comput.Interact*, 1,2, Article 99, Nov.(2017)
5. Lavergne, Michael, and Sendhil Mullainathan. "Are Emily and Greg more employable than Lakisha and Jamal? A field experiment on labor market discrimination." *The American Economic Review* 94, no. 4 (2004): 991-1013.
6. Doleac, Jennifer L., and Luke CD Stein. "The visible hand: Race and online market outcomes." *The Economic Journal* 123, no. 572 (2013).Harvard	
7. Fryer Jr, Roland G., and Steven D. Levitt. "The causes and consequences of distinctively black names." *The Quarterly Journal of Economics* 119, no. 3 (2004): 767-805.
8. Racine, Jeff, Qi Li."Nonparametric Estimation of Regreesion Functions with Both Categorical and Continous Data", *Journal of Econometrics* 119, no. 1(2004) 99-130


## Note
1. This assignment is largely based on the framework proposed by Prof. Salganik in his book, Bit by Bit: Social Research in the Digital Age. Princeton University Press.
2. Much of the research internal design of how to estimate the racial and gender bias is draw from Michael and Mullainathan (2004), but the method for digital age and the idea of testing the relationship of labor market tightness and the extent of racial gender bias is new.
