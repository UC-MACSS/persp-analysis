# Digital Enhanced Survey on New Job Opening
Author: Xinyu Cao
Assignment 2

## Research Question
In finance and macroeconomics, job opening data is a very important measure of  labor market conditions. Thus, this measure generally reflects economic prosperity and can impact future monetary and fiscal policy, as well as assets pricing in the financial industry. The new job opening data for the labor market is collected by the Bureau of Labor Statistics’ Job Openings and Labor Turnover Survey (JOLTS). However, this large-scale survey is expensive, lags behind the real labor conditions, and provides information only at the aggregate level. Blumenstock et. al (2015) described  a low-cost, digitally enhanced survey method that used phone call data to estimate localized and timely information of income distribution. We propose to apply this method to estimate job opening data by using sequential employment history data contained in CVs posted on LinkedIn.

## Digital Enhanced Research Design
The main part of this survey enhanced research is to collect job market digital trace data, i.e. what is the job most related other job. We could observe the pattern of how job market is related. So that, we know how those jobs are connected. Thus, by exploiting the information of connectedness of the job market contained this digital trace data, we could build a job market network. In the meantime, we could conduct a wiki survey of the job market to ask employer what is latest job opening, so that we can get the most timely information. Using the job market network and updated job market open information by wiki survey, we can obtain a detailed and timely job market opening data.

1 Wiki Survey Question Asking: \
Our definition of job opening is similar in the sense of the job vacancies in Hall (2003), we define it as the specific position that exists and is available within 30 days and is actively recruiting from outside to fill the position similar.To collect a sample data for prediction, we conduct a wiki survey on the internet to ask the question of job opening from firms. The question should be framed as the same of JOLTS as "how many job positions do you have within 30 days", while in the same time, in order to identify the job, the following information of new job opening will be asked:
   1. name: job title, job type, company name
   2. qualification: required educational background, license, or certification requirement, experience requirement
   3. compensation: seniority level, wage range
   4. demographic information: location, sector/industry

2 Digital Trace Data Collection: \
The second step for this research is to collect curriculum viate information of the user in LinkedIn. The main information to be collected is the following: the first parts of this information should be the same of the survey question part. Thus, we are able to match all those job in the survey with those jobs in the curriculum vitae. Second part, of the information to be collected is the preceding order of the job they had. we could assume that a particular job that is before or after another job is closely related to another in the labor market network.

3 Amplified Asking Matching Wiki Survey and Digital Trace: \
Combining both the small sample survey of the future job opening and the digital trace, we can build a large network for the job market in LinkedIn. By utilization of this system, we are able to build a job opening statistics in a large scale based on enhanced survey data. Because similar job position in the this job market should have similar job opening overtime, we could make prediction of a more detailed, i.e. district level, and more timely job market condition based on fewer data, comparing to the traditional JOLTS.


## Why Digital-Enhanced Survey is better than Observation Data?
There are several potential problems that might arise from this question. But some of them I already talked about when I was doing my observation data problem. Thus, I will only briefly mention them in here and talk something particular important to this research design and tried to compare strength and weakness of both methods. \

1 Cheaper, more detailed, and more timely:\
  By using digital enhancement method, we could get a much cheaper, more detailed and more timely data compared to JOLTS survey data. Although we might only collect a fraction of JOLTS's sample. But we could use the digital trace of the job market to enhance the results. Since in the CV, we have employee's life time work position data, we could construct a network of job market. Since the positions are close in the network will have similar job opening, we could estimate the whole network by limited sample. This is simialr in the network structure of Blumenstock et. al (2015), where they estimate the income distribution network based on the phone call data and a small sample survey of income.

  Similar to their results, by using a low cost sample of the survey and CV data in LikedIn, we can obtain not only an timely overall job market situation, but also a detailed a district level job market situation. This detailed statistic could not only will have impact on overall monetary and fiscal policy implication, but also could be used as job market micro-intervention policy evaluation as well.

2 More representative:\
  As mentioned in my observation paper, potential problem of observation data might arise from the fact the job market website might not able to represent the whole economy, and the user base might shift across the time. Using sectors and industries and size of the company, we are able to see if and how the data becomes more or representative over time. \

  We could using the same method to compare the representative over time to see if this hypothesis, CV data is more representative, is true or not. In my prediction, the CV data should have a better representative compared to the job posting. Two reasons for this: 1) if the employer uses LikedIn, the employee also has a large probability use LikedIn, as job seeker usually have less bargaining power; 2) the CV data contains the whole the employee's whole career information, thus have a greater coverage, both in times and sample, compared to current job posting data itself. 


## Potential Errors and Methods to minimize
1 Representation Error: \
  This method might suffer from the representation error for the following two reasons. First, the target population should be the whole labor market's human resources employee. But this online wiki survey asking might not able to reach all the companies. Tradition industries might have less access to the internet. Thus the data is suffered  from coverage error. Second, compared to the survey distributed by the Bureau of Labor Statistics, our survey might have higher non-response rate, this is problematic because larger company might less reluctant to answer, since their time are more valuable. This bias might increase the fluctuation, because larger company may hold up some of its employee.\

  In order to tackle this problem, we use our digital enhanced method to link the company in the digital trace. By linking the survey answer with sequential employment history information in CV, we are able to construct a job network. By exploiting the fact that similar industry's similar positions might have similar job opening number. we can make a prediction based on smaller and less complete data-set. This exactly shows why we could benefit from the amplified asking method. 

2 Measurement Error:\
  Compared to observational data, the survey data might subject more to the measurement error when we conduct the survey. The way we ask the question matters, company will have contradicate and different idea about what job opening means compared to us. In order to address this issue, when we need to use build survey tricks such as ask question in indirect or repeated way.

3 Sensitive:\
  Compared to job posting data on Linkedln, the Curriculum Viate(CV) is more sensitive. However, this practice generally should be of less of concern. We depersonalized those data,i.e. we filter out the personal information such as name, and address, when we collecting the data. So that, the data is not sensitive anymore. Besides, Curriculum Viate data on Linkedln is in the form of semi-public available information, thus less sensitive. Second, the issue we concerned is about the network structure of the job market. Thus, this data collecting process will focused more collective pattern rather than behavior of indiviudals.


## Conclusion
This method enables us to estimate the job opening statistics on a timely and detailed manner with much lower cost. It can provide deeper insight into different district or demographic employment situations, which potentially can provide micro cost-benefit evaluation tools for labor market micro-intervention policy. In this era of populism, to understand deeper of unemployment of at local level and different demographic subgroup rather than the overall statistics can be a better approach for us to tackle the most salient problem in our era. Academia and society can benefit from this digital enhanced survey of job opening.



## Reference
1. Blumenstock, Joshua, Gabriel Cadamuro, and Robert On. "Predicting poverty and wealth from mobile phone metadata." *Science* 350, no. 6264 (2015): 1073-1076
2. Kuhn, Peter, and Kailing Shen. "Gender discrimination in job ads: Evidence from china." *The Quarterly Journal of Economics* 128, no. 1 (2012): 287-336.
3. Tang, Shiliang, Zhang, Xinyi, Cryan, Jenna, Metzger, Miriam J., Zheng, Haitao, and Zhao, Ben Y. "Gender Bias in the Job Market: A Longitudinal Analysis.", *Proc. ACM Hum.-Comput.Interact*, 1,2, Article 99, Nov.(2017)
4. Hall, Robert E. "Modern theory of unemployment fluctuations: Empirics and policy applications." *The American Economic Review* 93, no. 2 (2003): 145-150