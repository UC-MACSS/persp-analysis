# "Now-casting" Job Opening Statistics

## Research Question
In finance and macroeconomics, job opening data is a very important measure for labor market condition, thus has siginificant impact on the economical prosper and future monetary policy, fiscal policy implication as well as an important parameter for assets pricing purposes. The new job openning data for labor market is collected by Bureau of Labor Statistics's Job Openings and Labor Turnvoer Survery (JOLTS). However JOLTS is a monthly survey, therefore it has a four weeks lag. Indeeded we are now facing a **"now-casting"** type of problem regarding job openning in the US. This is a typical question that we are facing time gap in traditional method of data collection and reporting period. However the jop posting data in the website like linkedin or indeed are always on. We should could use nonparametric method in Racine & Li(2004) to exploit the information on the internet of job posting to make a forecast about the real job opening on the labor market.

## Research Design
The main part of the data collection process is to collect the job posting in the job website such as linkedin and indeed. By simplying counting the new job posting in each day, we could know how many new jobs are posted on the internet. But this naive counting of job posting on the internet might not able to reflect the whole situation of the economy. There might suffer from at least three problems 1) the internet job posting might be non-representative for the US labor market. 2) the sample using internet to post their job advertisment might drift from  time to time. 3) the texual data of the internet job posting are not standard, thus require significant amount of time to develop natural language processing technique to capture the information we need.

1) Data Collection:
   In order to facilitate our research, the following feature of the job posting will be used: 
   1) name: job title, job type, company name, 
   2) qualification: required education background, license or certification requirement, experience requirement, 
   3) compenstaion: senority level, wage range,
   4) demographic information: location, sector/industry. 
2) Pre-processing:
   Usually the job advertisement on the internet is not a standard text, we need to develope algorithms to capture those features so that we can ready to exploit them. Natural Language Processing is a eminent field which is emerging. Few interdisciplinary papers about the Gender Discrimination and online job opportunity posting are published on the field both in economics, such as Kuhn & Shen (2012), and in applied computer science, such as Tang et.al (2017). 
3) Counting things:
   By our definition of job opening, we define as the a specific position exists and is avilable within 30 days, and is actively recruiting from outside to fill the position similar in the sense of the job vancancies in Hall(2003). For our own purpose, we try to "now- casting" this statistics by counting new job posted in the job searching website.  

## Potential Problems Rising from Big Data 
1) Non - representative:
   The first problem we might face is that the website of linkedin or indeed are not representative of U.S labor market. We might need to merge multiple website's data to construct a representative job market sample. Besides, some companies are larger might have more channel to put advertisment, therefore more likely to remian digital trace. The sectors and industries might also be an important factor, since some sector might be more traditioanl thus less internet coverage. Some are more innovative, therfore more internet coverage.
2) Drift:
   The second problem is that the website of job posting might suffer from drift of population. For example, there might be more and more company that uses online job marketing, therefore the holistic index we expolit might subject to change. But this drift might also turns to a good thing for measure the whole labor market. Because this increasing internetlize of job posting might remedies part of our concerns for the non representative issues.
3) Dirty:
   This Big Data is quite dirty in term of the textual difference it has. It might need significant amount work on textual analysis to get a clean categorical information, such as sector/industry and location.

## Remedies of the Potential problems
1) Large data: 
   For the non-representative problem, we could exploit the fact that the data are large. Therefore we might be able to divided the labor market into sectors or industies and forecast relevant ones with sufficient data. This categorical sampling at worst could help us identifies a siginificant fraction of the those industries and could give a us a good foresee before the publish of the offical survey data. One of the most recent method is the Racine & Li (2004) JOE paper, where they studies the nonparametric method of categorical data. 
2) Matching:
   For drift problem, we could exploit the method of time series of drift to estimate the trend of the drift. Thus that when we get new data, we could already spearate out the difference of the trend effects in the drift and the shock in the job posting data.  We could using the method Pimentel et.al (2015) to mathcing those comapny who has different ponteial to post their job advertisment on the internet with different propensity scores. 
3) Casting:
   After we adjust the potential problem, now we should be able to produce the right casting of the job opening according to the adjusted number of the job post on the job website.

## Conlusion
This research could shed light on how to adjust expectation of the labor market at current time, help policy maker and financial industry to price asset more timely. We choose also using a matching method to category different industry and different company might have the different potential to publish their job opening on the internet, so that they could be able to adjust the systemic difference of the sample. Naturally, we might still subject to potential omitted data problem. But at least we could able to get a partial statistics of the job opening.


## Reference
1. Racine, Jeff, Qi Li."Nonparametric Estimation of Regreesion Functions with Both Categorical and Continous Data", *Journal of Econometrics* 119, no. 1(2004) 99-130
2. Kuhn, Peter, and Kailing Shen. "Gender discrimination in job ads: Evidence from china." *The Quarterly Journal of Economics* 128, no. 1 (2012): 287-336.
3. Tang, Shiliang, Zhang, Xinyi, Cryan, Jenna, Metzger, Miriam J., Zheng, Haitao, and Zhao, Ben Y. "Gender Bias in the Job Market: A Longitudinal Analysis.", *Proc. ACM Hum.-Comput.Interact*, 1,2, Article 99, Nov.(2017)
4. Hall, Robert E. "Modern theory of unemployment fluctuations: Empirics and policy applications." *The American Economic Review* 93, no. 2 (2003): 145-150
5. Pimentel, Samuel D., Rachel R. Kelz, Jeffrey H. Silber, and Paul R. Rosenbaum. "Large, sparse optimal matching with refined covariate balance in an observational study of the health outcomes produced by new surgeons." *Journal of the American Statistical Association* 110, no. 510 (2015): 515-527.

