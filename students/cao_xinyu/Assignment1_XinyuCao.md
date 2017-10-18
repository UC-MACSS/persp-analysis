# "Now-casting" Job Opening Statistics
Author: Xinyu Cao

## Research Question
In finance and macroeconomics, job opening data is a very important measure for of labor market conditions., Tthus, it has siginificantsignificant impact on the economical prosperity and future monetary policy, fiscal policy implication as well as an important parameter for assets pricing purposes. The new job openning data for the labor market is collected by Bureau of Labor Statistics's Job Openings and Labor Turnvoer Survery (JOLTS). However, JOLTS is a monthly survey, and therefore, it has a four- weeks lag. Indeeded we are now facing a "now-casting" type of problem regarding job openningopening data in the US. This is a typical question that we are facing in traditional methods where there is a time gap between data collection in traditional method of data collection and reporting period. However, the jobp posting data in the websites like Llinkedin or Iindeed are always on. Rachine and Li (2004) describe a nonparametric method about categorical data, we We should could use this nonparametric method described in Racine & Li (2004) to exploit the information on the internet of job posting to make a forecast about the real job opening on in the labor market. 

## Research Design
The main part of the data generating process is to collect the job posting in the job website such as Linkedin and Indeed. By simply counting the new job postings each day, we could understand know how many new jobs are posted on the internet. But this naive counting of job postings on the internet might not able to reflect the whole situation of the economy. There The counting might suffer from at least three problems 1) the internet job posting might be non-representative for the US labor market; 2) the sample using the internet to post their job advertisement might drift from time to time; and 3) the textual data of the internet job postings are not standard, thus requiring a significant amount of time to develop natural language processing techniques to capture the information we need.

1 Data Collection: In order to facilitate our research, the following feature of the job posting will be used:
  1 name: job title, job type, company name
  2 qualification: required education background, license or certification requirement, experience requirement
  3 compensaion: seniority level, wage range
  4 demographic information: location, sector/industry.
2 Pre-processing: Usually the job advertisement on the internet is not a standard text. Thus, we need to develop algorithms to capture those features so that we can ready to exploit them. Natural Language Processing is an eminent field which that is emerging. Few interdisciplinary papers about the Gender Discrimination and online job opportunity postings are published on in the field both in economics, such as Kuhn & Shen (2012), and in applied computer science, such as Tang et.al (2017).
3 Counting things: By In our definition of job opening in the sense of the job vacancies in Hall (2003), we define it as the specific position that exists and is available within 30 days and is actively recruiting  from outside to fill the position similar. For our own purpose, we try to "now- casting" this these statistics by counting new job posted in the job searching website of the last 30 days.
  

## Potential Problems Rising from Big Data 
1) 1. Non-representative: 
   The first problem we might face is that the Linkedin or Indeed website are not representative of the U.S labor market. We might need to merge multiple websites’ data to construct a representative job market sample. Besides, some larger companies might have more channels to put advertisement, therefore more likely to remain digital trace. The sectors and industries might also be an important factor, since some sectors might be more traditional and thus have access to less internet coverage. Some are more innovative and therefore have more internet coverage.
2) Drift:
   The second problem is that the website of job posting might suffer from drift of population. For example, there might be more and more companies that use online job marketing, therefore the holistic index we expolit might be subject to change. But this drift might also turn to a good thing for measuring the whole labor market. Because this increasing “internetlize” of job posting might remedy part of our concerns for the non-representative issues.
3) Dirty:
   This Big Data is quite dirty in terms of the textual difference it has. It might need significant amount work on textual analysis to get clean categorical information, such as sector/industry and location.

## Remedies of the Potential problems
1) Large data: 
   For the non-representative problem, we could exploit the fact that the data are large. Therefore, we might be able to divide the labor market into sectors or industries and forecast relevant ones with sufficient data. This categorical sampling at worst could help us to identify a significant fraction of those industries and could give a us a good foresee prediction before the publishing of the official survey data. One of the most recent methods is the Racine & Li (2004) JOE paper, where they studied the nonparametric method of categorical data. 
2) Matching:
   For drift problem, we could exploit the method of time series of drift to estimate the trend of the drift. Thus, when we get new data, we could already separate out the difference of the trend effects in the drift and the shock in the job posting data. We could use the method Pimentel et.al (2015) to match those companies who have different potential to post their job advertisement on the internet with different propensity scores.
3) Casting:
   After we adjust for the potential problem, now we should be able to produce the right casting of the job opening according to the adjusted number of the job post on the job website.

## Conlusion
This research could shed light on how to adjust expectation of the labor market at current time, help policy maker and financial industry to price asset more timely. We choose also using a matching method to category different industry and different company might have the different potential to publish their job opening on the internet, so that they could be able to adjust the systemic difference of the sample. Naturally, we might still subject to potential omitted data problem. But at least we could able to get a partial statistics of the job opening.


## Reference
1. Racine, Jeff, Qi Li."Nonparametric Estimation of Regreesion Functions with Both Categorical and Continous Data", *Journal of Econometrics* 119, no. 1(2004) 99-130
2. Kuhn, Peter, and Kailing Shen. "Gender discrimination in job ads: Evidence from china." *The Quarterly Journal of Economics* 128, no. 1 (2012): 287-336.
3. Tang, Shiliang, Zhang, Xinyi, Cryan, Jenna, Metzger, Miriam J., Zheng, Haitao, and Zhao, Ben Y. "Gender Bias in the Job Market: A Longitudinal Analysis.", *Proc. ACM Hum.-Comput.Interact*, 1,2, Article 99, Nov.(2017)
4. Hall, Robert E. "Modern theory of unemployment fluctuations: Empirics and policy applications." *The American Economic Review* 93, no. 2 (2003): 145-150
5. Pimentel, Samuel D., Rachel R. Kelz, Jeffrey H. Silber, and Paul R. Rosenbaum. "Large, sparse optimal matching with refined covariate balance in an observational study of the health outcomes produced by new surgeons." *Journal of the American Statistical Association* 110, no. 510 (2015): 515-527.

