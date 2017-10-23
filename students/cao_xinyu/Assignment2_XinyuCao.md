# Digital Enhanced Survey on New Job Opening
Author: Xinyu Cao
Assignment 2

## Research Question
In finance and macroeconomics, job opening data is a very important measure of  labor market conditions. Thus, this measure generally reflects economic prosperity and can impact future monetary and fiscal policy, as well as assets pricing in the financial industry. The new job opening data for the labor market is collected by the Bureau of Labor Statistics’ Job Openings and Labor Turnover Survey (JOLTS). However, this large-scale survey is expensive, lags behind the real labor conditions, and provides information only at the aggregate level. Blumenstock et. al (2015) described  a low-cost, digitally enhanced survey method that used phone call data to estimate localized and timely information of income distribution. We can apply this method to estimate job opening data using sequential employment history data contained in CVs posted on LinkedIn, for example.

## Digital Enhanced Research Design
The main part of this survey enhanced research is to collect job market digital trace data, i.e. what is the job most related other job. We could observe the pattern of how job market is related. So that, we know how those jobs are connected. Using this digital trace data, we could build a digital job market network. In the meantime, we could conduct a small sample survey of the job market to ask them what is their own job opening. Using this feature, we could obtain a large sample by combining a small sample survey with this network way of digital enhanced method.

1 Ask question: 
Our definition of job opening is similar in the sense of the job vacancies in Hall (2003), we define it as the specific position that exists and is available within 30 days and is actively recruiting from outside to fill the position similar.To collect a sample data for prediction, we conduct a survey of small sample that are part of the labor market. The question should be framed as the same of JOLTS as "how many job positions do you have within 30 days", while in the same time, in order to identify the job, the following information of new job opening will be asked:
   1. name: job title, job type, company name
   2. qualification: required educational background, license, or certification requirement, experience requirement
   3. compensation: seniority level, wage range
   4. demographic information: location, sector/industry

2 Digital Trace Data Collection: 
The second step for this research is to collect curriculum viate information of the user in LinkedIn. The main information to be collected is the following: the first parts of this information should be the same of the survey question part. Thus, we are able to match all those job in the survey with those jobs in the curriculum vitae. Second part, of the information to be collected is the preceding order of the job they had. we could assume that a particular job that is before or after another job is closely related to another in the labor market network.

3 Amplified Asking Matching Survey and Digital Trace: 
Combining both the small sample survey of the future job opening and the digital trace, we can build a large sample system for the job market in LinkedIn. By utilization of this system, we are able to build a job opening statistics in a large scale based on enhanced survey data. Compared to the traditional JOLTS, the amplfied asking enables us the make specific geographic regions or demographic groups prediction. 


## Potential Problems and Remedies of the method
There are several potential problems that might arise from this question. But some of them I already talked about when I was doing my observation data problem. Thus, I will only briefly mention them in here and talk something particular important to this research design and tried to compare strength and weakness of both methods.

1 Cheaper, more detailed, and more timly:
  By using digital enhancement method, we could get a much cheaper, more detailed and more timely data compared to JOLTS survey data. By using a small sample of the survey, we could achieve not only an overall job market situation, but also a detailed a district level job market situation. This detailed statistic could not only will have impact on overall monetary and fiscal policy implication, but also could be used as policy evaluation statistics as overall.

2 More representative and less drift:
  As mentioned in my observation paper, potential problem might arise from the fact the job market website might not able to represent the whole economy and the user base might shift across the time. By applying non-parametric categorization strategy in Racine & Li (2004) JOE paper, and matching strategy in Pimentel et.al (2015) JASA paper. What's more, the CV data should have a better representative compared to the job posting. Two reasons for this: 1) if the employer uses LikedIn, the employee also has a large probability use LikedIn, as job seeker usually have less bargining power; 2) the CV data contains the whole the employee's whole career information, thus have a greater coverage, both in times and sample, compared to the job posting data itself.  

3 More Measurement error:
  Compared to observational data, the survey data might subject more to the measurement error when we conduct the survey. For example, comapny will have contradicate and different idea about what job opening means compared to us. In order to address this issue, when we need to use traditioanl survey tricks such as ask question in indirect or repeated way.

4 More Sensitive: 
  Compared to job posting data on Linkedln, the Curriculum Viate(CV) is more sensitive. However, this practice generally should be fine. This is because when we collecting the data, we de-personalize those data,i.e. we filter out the personal information such as name, and address so that the data is not sensitive anymore. Besides, Curriculum Viate data on Linkedln is in the form of public available information, thus less sensitive. Second, the issue we concerned is about the network structure of the job market. Thus, this data collecting process will focused more collective pattern rather than behavior of indiviudals.

5 Less Dirty:
  Survey data and CV data are more standardized; therefore, it is much easier to clean compared to the counting job posting data by using observation data. However, this method still needs non-trivial amount of work on natural language processing. That said, we could still utilization of method of Tang et.al (2017). 

 
## Conclusion
This method enables us to estimate the job opening statistics on a cheaper, timely and more detailed method with much lower cost. It can provide deeper insight into different district or demographic employment situations, which potentially can provide micro cost-benefit evaluation tools for unemployment micro-intervention policy. In this era of populism, to understand deeper of unemployment of at local level and different demographic subgroup rather than the overall statistics might be a better approach for us to tackle the most salient problem in our era. Academia and society might able to benefit from this digital enhanced survey of job opening.



## Reference
1. Blumenstock, Joshua, Gabriel Cadamuro, and Robert On. "Predicting poverty and wealth from mobile phone metadata." *Science* 350, no. 6264 (2015): 1073-1076
2. Racine, Jeff, Qi Li."Nonparametric Estimation of Regreesion Functions with Both Categorical and Continous Data", *Journal of Econometrics* 119, no. 1(2004) 99-130
3. Kuhn, Peter, and Kailing Shen. "Gender discrimination in job ads: Evidence from china." *The Quarterly Journal of Economics* 128, no. 1 (2012): 287-336.
4. Tang, Shiliang, Zhang, Xinyi, Cryan, Jenna, Metzger, Miriam J., Zheng, Haitao, and Zhao, Ben Y. "Gender Bias in the Job Market: A Longitudinal Analysis.", *Proc. ACM Hum.-Comput.Interact*, 1,2, Article 99, Nov.(2017)
5. Hall, Robert E. "Modern theory of unemployment fluctuations: Empirics and policy applications." *The American Economic Review* 93, no. 2 (2003): 145-150
6. Pimentel, Samuel D., Rachel R. Kelz, Jeffrey H. Silber, and Paul R. Rosenbaum. "Large, sparse optimal matching with refined covariate balance in an observational study of the health outcomes produced by new surgeons." *Journal of the American Statistical Association* 110, no. 510 (2015): 515-527.