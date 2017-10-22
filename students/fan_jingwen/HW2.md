# Proposing A Survey Study```HW2Title: Supplementing Observational Study with EMA and Traditional SurveyClass: MACS 30000Instructor: Dr. Benjamin SoltoffAuthor: Jingwen (Fiona) Fan```## Research Question
### Background
In *Proposing An Observational Study*, the study of interest was to uncover what demographic factors have the causal power over patients' compliance, which has been documented to be a strong predictor of the clinical outcome of Type II diabetes patients (Demlamater, 2006). In my study, the lack of compliance was operationalized as the no_show rate of patients' scheduled appointments, recovered by a big dataset of physician visit time stamps. The **Research Design** part of the study mainly focused on running regressions, but also included building predictive models like neural net, linear SVM and random forest to supplement the explanatory study. 
Nowadays, with the advance of mobile technologies and telemedicine, diabetic management has been made easy. Apps like *Glooko* and *Health2Sync* allow patients to track their diabetic and other health features continuously, allowing patients to better evaluate and manage their own health. Also, forums like *diabetes daily* help patients understand the importance of diabetes management and being compliant with their doctors' orders, and provide peer support for Type II diabetes patients. Helping patients with their tech-savviness will help them bridge the gap between their perceived health and their actual health, a factor that might contribute to their decision to be compliant. 
### Research Question and HypothesesThere is one integral piece of our explanatory model that cannot be unearthed from our big data study: Why are the patients not showing up for their appointment? 
Instead of leaving it as an open-ended question (although I will include open-ended questions as a part of my survey), I will try to operationalize this question by primarily focusing on the gap between patients' *perception* of their diabetic health and their *actual* diabetic health. It has been established that there is a self-fulfilling relationship between people's perceived health and their ultimate clinical outcome (Hunt et al., 1980; Kaplan et al., 1983). My hypotheses hold that the difference between patients' *perceived* and *actual* diabetic health (the *wedge*) will be an influential predictor of their clinical outcomes, and that compliant patients have less of a wedge than non-compliant patients. I also hypothesize that the more tech-savvy patients will have less of a wedge, and thus be more compliant and have better clinical outcomes. 
To summarize, my research questions are three-fold: How does the difference between patients' *perceived* and *actual* diabetic health influence their decision to be compliant and their clinical outcomes? Does tech-savviness help bridge the aforementioned wedge? How do these result compare across different demographic groups?
### MotivationBeing able to answer these questions will enhance the explanatory power of my observational model, and help policy makers better direct their resources. For example, if tech-savviness and perceived diabetic health are indeed crucial factors, then the policy makers will have the theoretical support for spending money on a preventative care program that educates patients on technological diabetes management tools (or having the insurance companies covering their membership fees), to help them close the gap between their perceived diabetic health and real diabetic health, and thus resulting in better clinical outcomes.
## Research Design

### Overall Design and RationalizationThe *perception* of one's own health is an internal state not reflected by big data, and can only be accessed by a survey study. Thus, survey studies serve my purpose well. As mentioned above, the two key components of interest in the survey part of research that can supplement my obtained model from the observational study are *perceived* diabetic health and tech-savviness. The flow of logic here is that more tech-savvy patients have less of a wedge between their perceived and actual diabetic health, and thus will be more compliant and have better clinical outcomes.
Here, I divide my survey study into two parts: one will be a digitally-enhanced Ecological Momentary Assessment (EMA), distributed to major technological channels for diabetes management; the other will be a traditional survey conducted on the patients we have on record from our previous observational study. 

To operationalize the wedge, it is necessary to compare the survey-reported perception of diabetic health and actual ones documented during physician visits, which require linkage between survey data and observational data via Patient ID. The traditional survey will allow me to do this. Phone and in-person interviews are common practice for survey studies in the field of medicine for privacy considerations, and mine will be no exception to IRB protocols. Another benefit other than sample-matching to traditional survey is that it can be always-on and longitudinal. As mentioned in my observational study proposal, the study can continue for as long as Joslin Diabetes Center is open for business. 

The rationale behind using EMA to study tech-savviness is threefold. First, by definition it targets my target population perfectly -- Type II diabetes patients who are tech-savvy. Second, it measures the current state of my respondents (current perception of health and intention to be compliant) at the appropriate time (e.g, time to take the medicine or measure a1c level) and place (diabetes-related platforms). Third, the necessity in conducting this survey instead of asking respondents in the traditional survey to self-report their tech-savviness is to 1) avoid self-reported bias 2) obtain a larger sample size for more generalizable results. 


### Survey Design#### Question Design
The surveys will be created on Qualtrics.
##### EMA
For the EMA study, the respondents will be prompted to answer the following questions, supplemented by demographic information (the most explanatory features identified in the observational model) filling at the end. All respondents will be filtered by a gate-keeping question: *Are you a Type II diabetic patient?* Only answering yes to this question will allow the respondent to answer the ensuing ones.

1. When was your last visit to your physician?
1. What was your a1c and BMI level measured during that visit?
1. Were you diagnosed of any complications during that visit?
1. What a1c and BMI level do you think you have right now?
1. Do you think you have any complication now?
1. Have you ever missed your physician visit? 
1. If yes how many?
1. Will you comply by your future scheduled doctors' appointments? 
1. If no, why not?
1. Do you use any other diabetes-related channels?

***This survey will be designed so that no respondent will have to spend more than 3-5 minutes on it.***

##### Traditional Survey
Similarly, the respondents of the traditional survey will be prompted to answer the following questions:

1. What is your perceived a1c and BMI level?
2. Do you think you have any complications? Or do you predict there to be any complications during your next physician visit?
1. Will you comply by your future scheduled doctors' appointments? 
1. If no, why not?
2. Do you use technological diabetes management tools? 


#### Distribution Channels

##### EMA
Sponsored advertisements will appear on technological diabetes management tools like Glooko, Health2Sync, major US diabetes forums like *diabetes daily*, and major newspapers on diabetes, and etc. 
##### Traditional Survey
Research assistants will be paid to conduct in-person and telephone interviews. In addition, we will also send encrypted emails containing links to the survey.
*---The exact scope of sample population and magnitude of monetary surveys will be dependent on fundings.*### Population Definitions

| Population Type   |      EMA Survey Study      |  Traditional Survey Study  |
|:----------:|:--------:|:------:|
| Target Population   |  Type II diabetes patients in the US | Type II diabetes patients in the US  |
| Frame Population   |    Type II diabetes patients that are tech-savvy and use the platforms described in **Distribution Channels**.    |   Patients on record at Joslin Diabetes Centers from the *Observational Study* for any number of years.   |
| Sample Population   | Users of the aforementioned channels who read our sponsored messages for the survey. |   Portion of the sample population that research assistants are able to contact.

### Analyses

#### Data Integration and Cleaning
I will create a new dataset linking the patient response form the traditional survey to their clinical measures and complication outcomes from the big dataset described in my first assignment, via Patient ID. For both surveys, I will also code the response into dummy variables (save the open-ended questions). 

#### Quantitative Data analyses

***Are tech-savvy patients more likely to be compliant? Do they have less of a wedge?***

The two populations that I will compare the measures between are 1) the respondents to the EMA study 2) the respondents to the traditional survey who report not to use the technological tools for diabetes management. Descriptive statistics and statistical tests will be performed to see if there are significant differences between the two populations in their self-reported decisions to be compliant (Q8 for EMA and Q3 for Traditional Survey), and the wedge (Q2-5 for EMA, and Q1-2 + observational data for Traditional Survey). 

***How do the above-mentioned results differ amongst different demographic groups?***

With the reported demographic data, I can repeat the statistical analyses mentioned above across different demographic groups identified from my previous big-data study.

***How does the wedge influence their decision to be compliant and their clinical outcomes?***

Within the population of traditional survey respondents, I will integrate the *wedge* as a feature into the regressions and predictive models described in my previous assignment, and see if it is a significant causal factor.


#### Open-ended QuestionsI will do a qualitative summary of the responses to the open-ended questions, for supplementation and for directions of future research.### Error Evaluation
#### 1. Coverage Error
As addressed in my previous assignment, the target population is Type II diabetes patients in US while the participants in my traditional survey study will be patients in Massachusetts. Given the demographic information of US and Massachusetts provided by US census, I can do non-probability sampling by putting different weights in different demographic groups, if such geographical difference turn out to yield bias.

For the EMA study, the most salient coverage error is that the participants in the study are more tech-savvy. However, that is exactly the design of this research.
#### 2. Sampling Error
Little sampling error will this study have because the messages will be prompted randomly for the EMA study, and the research assistants will call randomly with hopes to cover all 25000+ patients. 
#### 3. Non-response Error
Monetary rewards will be offered upon completion of the survey. I am also making the survey short enough so that no self-selected free people are much more likely to answer the survey. The number of research assistants will decide the scope of respondents the study will be able to reach, and how much effort will be put into recruiting each respondent. Thus, reducing non-response error will be dependent on fundings. 

#### 4. Measurement Error
Patients might interpret the questions in assessing their current perception of diabetic health differently. I will adjust the wording if measurement error proves itself to be salient. 
### Budget Proposal
The most conspicuous components of costs for this study includes sponsorship for advertisement on the various channels, Qualtrics services, research assistant recruitment, and offered monetary rewards. The possibility of getting enough funding will be dependent on how renowned the professor who I am proposing this study to is within the healthcare industry, and how bad a fiscal year America is experiencing.
*Of course, the ideal case is such that someone should pay me for writing this proposal, but life is not perfect.*## BibliographyDelamater, A. M. "Improving Patient Adherence." Clinical Diabetes 24, no. 2 (2006): 71-77. doi:10.2337/diaclin.24.2.71.
Hunt, Sonja M., S. P. McKenna, J. McEwen, E. M. Backett, Jan Williams, and Evelyn Papp. "A quantitative approach to perceived health status: a validation study." Journal of Epidemiology & Community Health 34, no. 4 (1980): 281-286.
Kaplan, George A., and Terry Camacho. "Perceived health and mortality: a nine-year follow-up of the human population laboratory cohort." American journal of epidemiology 117, no. 3 (1983): 292-304.
