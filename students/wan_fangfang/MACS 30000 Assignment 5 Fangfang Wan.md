##### MACS 30000 Assignment 5

##### Fangfang Wan

###### Kaggle open call project

​        The "Text Normalization Challenge - English language" is an open call project for linguistics research, which requires participants to normalize English text to a string that represents the spoken form. The goal is to provide English texts in the spoken form for linguistics applications such as text-to-speech synthesis (TTS) and automatic speech recognition (ASR). To be specific about what participants are supposed to do, if we take an example from the website, "12: 47" should be converted to "twelve forty-seven", and any discrepancy in the actual string and submitte string for a given text will result in error of that term. To make a submission, I would have to do the normalization for English texts as accurately as possible. 

###### Improving a journal article

Journal Article: Liu, G. G., Dow, W. H., Fu, A. Z., Akin, J., & Lance, P. (2008). Income productivity in China: On the role of health. *Journal of Health Economics*, *27*(1), 27-44.

​	In this article, the authors used China Health and Nutrition Survey (CHNS) (UNC Carolina Population Center) dataset to investigate the correlation between health status and household income, and figured out that higher household income is associated with better health status of household members. 

​	I plan to implement the human computation methods in the data collection process, and the process contains two layers of human computation. In the original research, they used CHNS dataset, which comprises information much more than needed, but information is not targeted specifically to this research. We only need a few variables in this research. Therefore, the dataset is not of satisfying quatlity, and needs substantial cleaning before researchers start using it. To collect cleaner and more specific data, on the first layer, we can assign a project to economics and other relavant fields Ph.D. students all over universities in China. With a much shorter survey designed than the survey in CHNS, We can assign those students to various regions in China, and their mission is to train staffs in community committee in cities and townships, and village committees in rural regions on how to properly conduct the survey. Then on the second layer of human computation, staffs in community committees and village committes send out the survey to households, and then collect data back to those Ph.D. students, The data collection process can last for years to build a panel dataset. 

​        The study will benefit from the human computation design in the following aspects. First, it allows researchers to collect much cleaner datasets, since there are much fewer questions than the CHNS survey, thus participants will be more attentive when they answer every specific question. Second, since the quantity of qualified Ph.D. students is large, and each of them can in charge of several community and village committees, we can collect data on a much broader range of households, and we can cover all provinces and municipalities in China, rather than only a few households in each community and 15 provinces in total in CHNS (UNC Carolina Population Center). 

###### Alternative assignment

###### 1. Comparison of InfluenzaNet, Google Flu Trends, and traditional (CDC) influenza tracking system

​	InfluenzaNet is a non-traditional flu tracking system in Europe, which relies on reports from volunteers on Internet. Residents of covered countries may sign up freely on the website and report their influence-like-illness once a week. The system then infer the flu epidemiology from the sample they collected from the volunteers. Errors may arise from selection bias, while the direction of bias is unclear. Since this website collect data from volunteers, the cost should be pretty low. Residents who found the InfluenzaNet and are volunteering may have higher education, of younger age, etc. than other people, and their social economic status may positively correlated with their health status, since they might be better informed and better prepared for health shocks, thus resulting in higher report. For example, they may be more likely to receive flu shot than other residents, since they are more risk-awared. However, people who do have flu, especially serious flu, may not even have the energy to report their infection, thus inducing lower report. 

​	Google Flu Trends (GFT) is a predictive system that Google used to predict the Center of Disease Control and Prevention (CDC) reported flu incidents from users' search terms, using big data, maching learning, etc. Costs involves algorithms development, which should be higher than that of InfluenzaNet, but should be lower than the traditional tracking system. Potential error has arised from algorithmic confounding, since the searching algorithm will suggest related terms such as "fever", which increases the predicted amount, as pointed out in Salganik (2017)

​	The traditional CDC influenza tracking system relies on data reported from expertised institutions, such as clinics, emergency care, clinical laboratories, health care providers. Since this method involves collaborations with experts and various specialized institutions, it should be the most expensive but the most accurate one. However, likely inaccuracies may result from the fact that some residents who caught flu might not seek medical treatment, so no trace of their infection has been recorded. Also, as pointed out in Salganik (2017), it is lagged for 2 weeks.

###### 2. Unsettle time description

​	During an outbreak of flu, as indicated in Salganik (2017), traditional flu tracking system can result in lag of 2 weeks, which can seriously delay the conductions of necessary measures. The fact that some people don't seek medical help may also result in underestimation of flu infection cases. Google Flu Trend may suggest even more related search terms during outbreaks due to its algorithmic confounding, and a significanlty larger population are concerned about flu, so the increase in the related terms searching might be much higher than the actual increase in flu incidents. Furthermore, as for the InfluenzaNet, during outbreaks, people who are seriously ill may not even have energy to report, thus resulting in underestimation of acutual flu infection. 

##### References:

Centers for Disease Control and Prevention. *Overview of Influenza Surveillance in the United States*. Retrieved from https://www.cdc.gov/flu/weekly/overview.htm

Ginsberg, J., Mohebbi, M. H., Patel, R. S., Brammer, L., Smolinski, M. S., & Brilliant, L. (2009). Detecting influenza epidemics using search engine query data. *Nature*, *457*(7232), 1012-1014.

Google. *Google Flu Trends*. Retrieved from https://www.google.org/flutrends/about/

Lazer, D., Kennedy, R., King, G., & Vespignani, A. (2014). The parable of Google Flu: traps in big data analysis. *Science*, *343*(6176), 1203-1205.

Liu, G. G., Dow, W. H., Fu, A. Z., Akin, J., & Lance, P. (2008). Income productivity in China: On the role of health. *Journal of Health Economics*, *27*(1), 27-44.

Salganik, M. J. (2017). *Bit by Bit: Social Research in the Digital Age*. Princeton University Press.

UNC Carolina Population Center. *China Health and Nutrition Survey*. Retrieved from http://www.cpc.unc.edu/projects/china

InfluenzaNet. Retrieved from https://www.influenzanet.eu/

