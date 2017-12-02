---
title: "Collaboration Assignment"
author: "Yilun Dai"
date: "11/11/2017"
output: github_document
---

# 1. Kaggle

## II.

    I am going to describe the Porto Seguro's Safe Driver Prediction. Porto Seguro is one of Brazil's largest auto and homeowner's insurance companies. The company wants to improve the auto insurance claim prediction, because inaccurate predictions make safe drivers pay a high cost while giving bad ones a lower price than they should pay. The goal of this competition is to build a more powerful model that predicts the probabiltiy of a driver initiating an auto insurance claim in the next year. This improved prediction will be used to enhance their pricing strategies. \
    To make a submission after having built my model, I must first make sure that my submission is in the CSV format. For this specific competition, I must predict a probability in the target column for each id in the test set, and contain a header in the submission file. Then, I should go to the "overview" tab, click on the "Submit Predictions" button and accept the competition's ruls. Then, I should click on "upload submission file" to submit my entry.\
    
## III. (See scripts, data file, and the plot)

```{r}
index <- subset(indexdata, Day == 1)
interest <- ts(index$Effective.Federal.Funds.Rate, start = c(1954, 07, 01),  freq = 12)
unemployment <- ts(index$Unemployment.Rate, start = c(1954, 07, 01), freq = 12)
ts.plot(interest, unemployment, col = c("blue", "black"), ylab = "percentage")
title(main = "Interest Rate and Unemployment Rate from 1954 to 2017")
legend("topright", c("Interest Rate", "Unemployment Rate"), col = c("blue", "black"), lty = 1)
```

    Description: this is the data from the Federal Reserve on the interest rate and the unemployment rate from 1954 to 2017. I plot the monthly data of two time series, and we can see that interest rate reaches its peak when unemployment rate is at its trough. Trends of interest: 
    * interest rate and unemployment rate are likely to be negatively correlated 
    * we might want to examine interest rate as a predictor of unemployment rate.
    
# 2.

    The paper that I am going to discuss is "American Learners of French and their Stereotypes of the French Language and People: A Survey and its Implications for Teaching" written by Isabelle Drewelow. This study recruits 47 students enrolled in 4 sections of a first semester French language class in an American university (Drewelow, 752). The students were given a survey on their assumptions on french language and culture on the first day of class. I would like to reformulate the study as a human computation project in the following ways: I will recruit volunteers from iLearn, a online learning center complementing common language learning textbooks used by second-language learners who attend language classes, and Duolingo, a learning website. The initial surveys will be distributed to them via their sign-up email to collect their geographic, age, and education data and data on their perceptions of the French language and culture. Follow-up surveys will again be distributed via email asking about their perceptions on French language and culture periodically. This will improve the study in the following way: first, the data is more large-scale, and less biased, since number of volunteers will be much greater than 47, and have a wider range of geographical, educational and cultural patterns. Second, the data will be constantly updated by follow-up surveys.
    
# 3.

## 1.

### Design

    Influenzanet is a Europe-wide monitoring network that collects ILI from volunteers (Van Noort et al). It mainly uses survey methods stated by Salganik. It recruits volunteers from the general public who complete an initial survey on lifestyle and geographic information. These volunteers will receive a weekly email that leads them to an online survey link asking them about the possible symptoms they might be having since their last report. Volunteers from the previous season will be invited to participate at the beginning of the new season.\
    Google Flu Trends utilizes stream of queries from search engine input their users and collects the queries relevant to flu into a database. It mainly uses observational methods stated by Salganik.\
    Traditional influenza tracking systems uses information reported by doctors. According to L Tilston et al, traditional systems relies on "networks of physicians to diagnose and report ILI". \
    
### Costs:

    Influenzanet and Google Flu Trends are relevantly low costs and can collect large cohort of data. Traditional influenza tracking systems require higher costs. \

### Errors: 

    Inluenzanet: Volunteers who participated only once in the survey and those who seem more likely to be seek might bring biases to the result (L.Tilston et al). \
    Google Flu Trends: those who search for flu relevant keywords do not necessarily have ILI, and those are ill do not necessarily search for flu relevant keywords. \
    Traditional influenza tracking systems: there are individuals who do not visit physicians when they are ill. We do not know the proportion of these cases, and the social groups they belong to may vary and do not have a definite pattern. In addition, patients might alreay get better when they are waiting for medical attention, and thus their symptoms were not observed. \
    
## 2. 

    Influenzanet: Those who are under the influence of illness might have limited access to the internet so that the surveys that reaches to those who are ill are not all completed; those who report symptoms might not have the epidemic. \
    Google Flu Trends: Those who are under the influence of illness might have limited access to the internet so that the surveys that reaches to those who are ill are not all completed; those who search for remedies of flu might not be ill. \
    Traditional infkuenza tracking systems: The proportion of patients who do not attend physicians is unknown, and both the proportion and the pattern might change during an epidemic. The breakout might be too soon to be reacted by the medical care system, and some patients might not have timely access to health care, so the scale and the seriousness of the endemic might be underestimated. \

<div class="pagebreak"></div>

# References

Drewelow, I. (2011). American Learners of French and their Stereotypes of the French Language and People: A Survey and its Implications for Teaching. The French Review, 84(4), 748-762. Retrieved from http://www.jstor.org/stable/25800244 \

Salganik, Matthew J. 2017. Bit by Bit: Social Research in the Digital Age. Princeton, NJ: Princeton University Press. Open review edition. \

Sander P. van Noort, Cláudia T. Codeço, Carl E. Koppeschaar, Marc van Ranst, Daniela Paolotti, M. Gabriela M. Gomes, Ten-year performance of Influenzanet: ILI time series, risks, vaccine effects, and care-seeking behaviour, In Epidemics, Volume 13, 2015, Pages 28-36, ISSN 1755-4365, https://doi.org/10.1016/j.epidem.2015.05.001.
(http://www.sciencedirect.com/science/article/pii/S1755436515000638) \

Natasha L Tilston, Ken TD Eames, Daniela Paolotti, Toby Ealden and W John Edmunds, Internet-based surveillance of Influenza-like-illness in the UK during the 2009 H1N1 influenza pandemic, BMC Public Health, Volume 10, 2010, https://doi.org/10.1186/1471-2458-10-650 \












