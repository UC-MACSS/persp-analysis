# "Now-casting" Job Opening Statistics

1. Research Question
In finance and macroeconomics, job opening data is a very important measure for labor market condition, thus has siginificant impact on the economical prosper and future monetary policy, fiscal policy implication as well as an important parameter for assets pricing purposes. The new job openning data for labor market is collected by Bureau of Labor Statistics's Job Openings and Labor Turnvoer Survery (JOLTS). However JOLTS is a monthly survey, therefore it has a four weeks lag. Indeeded we are now facing a **forecasting problem** or **"now-casting"** type of problem regarding job openning in the US. This is a typical question that we are facing time gap in traditional method of data collection and reporting period. However the jop posting data in the website like linkedin or indeed are always on. We should find a way to exploit the information on the internet of job posting to make a forecast about the real job opening on the labor market.

2. Research Design
The main part of the data collection process is to collect the job posting in the job website such as linkedin and indeed. By simplying counting the new job posting in each day, we could know how many new jobs are posted on the internet. But this posting could not reflect the whole situation of the economy, therefore we need to use categorical sampling method to adjust empirical bias of different industry.  

1) Data Collection:
   The following feature of the job posting will be used: job title, job type, education background, license or certification requirement, experience requirement, senority level, wage range, company name, location, sector/industry. 
2) Pre-processing:
   Usually the job advertisement on the internet is not a standard text, we need to develope algorithms to capture those features so that we can ready to exploit them. Natural Language Processing is a eminent field which is emerging. Few interdisciplinary papers about the Gender Discrimination and online job opportunity posting are published on the field both in economics, such as Kuhn & Shen (2012), and in applied computer science, such as Tang et.al (2017). 
3) Counting things:
   By our definition of job opening, we define as the a specific position exists and is avilable within 30 days, and is actively recruiting from outside to fill the position similar as the JOLTS longtitude survey data (2017). For our own purpose, we try to "now- casting" this statistics by counting new job posted in the job searching website.  

3. Potential Problems Rising from Big Data 
1) Non - representative:
   The first problem we might face is that the website of linkedin or indeed are not representative of U.S labor market. We might need to merge multiple website's data to construct a representative job market sample. 
2) Drift:
   The second problem is that the website of job posting might suffer from drift of population. For example, there might be more and more company that uses online job marketing, therefore the holistic index we expolit might subject to change. But this drift might also turns to a good thing for measure the whole labor market. Because this increasing internetlize of job posting might remedies part of our concerns for the non representative issues.

4. Remedies of the Potential problems
1) Large data: 
   For the non-representative problem, we could exploit the fact that the data are large. Therefore we might be able to divided the labor market into sectors or industies and forecast relevant ones with sufficient data. This categorical sampling at worst could help us identifies a siginificant fraction of the those industries and could give a us a good foresee before the publish of the offical survey data. 
2) Matching:
   For drift problem, we could exploit the method of time series of drift to estimate the trend of the drift. Thus that when we get new data, we could already spearate out the difference of the trend effects in the drift and the shock in the job posting data.  

5. Conlusion
This research could shed light on how to adjust expectation of the labor market at current time, help policy maker and financial industry to price asset more timely. We choose a matching method to category different industry and different company might have the different potential to publish their job opening on the internet.
