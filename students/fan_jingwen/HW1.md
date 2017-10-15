# Proposing An Observational Study
```
Title: Path to better diabetes management based on clinical big data
Class: MACS 30000
Instructor: Dr. Benjamin Soltoff
Author: Jingwen (Fiona) Fan
```

## Motivation

National Health Expenditure Accounts (NHEA) reports that healthcare spending accounted for a staggering 17.8% of US GDP in 2015, totaling $3.2 trillion for the whole industry. The growing momentum continues on. A recent study conducted by Center for Medicare and Medicaid Services (CMS) (Keehan et al., 2017) reports that by 2025, healthcare spending is projected to reach $5.5 trillion. 

Diabetes has been recognized as a major contributor to both the volume and the trend of the growth of healthcare spending. According to a report by WebMD (Thompson, 2016), diabetes tops the chart of *the most costly health diseases* in 2013. In addition, its sustained growth rate from 1997 to 2013, averaged to be 6.5%, overshadows the 3.5% average growth rate of the healthcare spending. 

The latest report in a longitudinal study done by the American Diabetes Association (ADA), which tracks the components of healthcare expenditure on diabetes care across years, reports that out of the $245 billion total costs, hospital inpatient care (43% of the total medical cost), prescription medications to treat the complications of diabetes (18%) and physician office visits (9%) top the chart, and together account for a majority of the costs. Studying what can lead to less healthcare and subsequently less healthcare spending in the field of diabetes can thus contribute to reducing healthcare spending in the US as a whole.


## Research Question
In this study I will mainly look at Type II diabetes, mainly for two reasons. First, Type II diabetes dominates in its prevalence, affecting 95% of the population with diabetes. Second, Type I diabetes is genetic, with its onset usually during a patient's childhood and lasts throughout adulthood. Including Type I diabetes will confound our results by negatively biasing the clinical outcome.

In the field of Clinical Diabetes, patients' compliance has long been identified as one of the most salient contributing factor to their clinical outcome (Demlamater, 2006). Patients who choose to obey their doctors' orders and show up for subsequent clinical visits tend to have better clinical outcomes. This observational study aims to utilize patients' clinical records and insurance data to uncover what demographic factors has the causal and predictive power over patients' compliance. By answering that question, policy makers can more efficiently direct their budgets to the right places as a method of preventative care, which can hopefully reduce patient rehospitalization frequency and complication occurrences and thus save the associated costs.

## Data 
### Data Description
The data comes from Joslin Diabetes Center, a premiere diabetes clinic in Boston, MA. The data span across a period of 8 years, from 2007-2014. The dataset consists of three parts, one is the time stamp record of a patient's visit to the doctor's office, one is the clinical record of her hospitalization during the 8 years, and one is the insurance data which include her demographic and insurance information. The time stamp record includes a unique ID for each patient (allowing us to track the patient longitudinally across 8 years), the time stamp for her scheduled visit, the time stamp for when she actually showed up. The clinical record includes the patient ID, the time stamp of her hospitalization and rehospitalization, and clinical measures like Body Mass Index (BMI), blood sugar level (a1c), and detailed description of their complications if they have one, like ophthalmic, renal and neurological manifestations. Finally, the insurance data, also available at the clinic, includes the patient ID, demographic attributes like race, zipcode, income, education level, insurance company name, whether they are in a diabetes management program, and etc.

### Data Manipulation and Operationalization
Ultimately I want to arrange the dataset into a set of panel data for data analyses. There are some hurdles to overcome with data manipulation. 

First, since the final dataset will have to be merged from three separate data sources linked by patient ID, the data cleaning process will be painstaking before merging the data. Different insurance companies keep records in different formats, so the first step is to organize the data across insurance companies and across years to be in uniform format. 

Second, there will be missing data. Some can be remedied by making trips to the Center and asking for them. However, upon inspection, only 5000+ out of the 25000+ patients persist through all 8 years. The way I plan on approaching this problem is to partition the dataset by the number of year that the patient has on record. I will make separate dataset for patients that appear on record for 2-8 years respectively, and perform longitudinal data analyses on all such datasets.

Finally, to operationalize compliance I will create a variable calculated as $$$NoShowRate = {number \ of \ missed \ appointments \over number \ of \ total \ appointments}$$$ to reflect how uncompliant the patient is with her doctor's orders. 

The operationalization of outcome can be twofold. One will be the continuous healthcare outcome variables like BMI, a1c and rehospitalization frequencies. The other will be a number of binary variables coding for different types of complications. To do that, I will parse the variable that describes the patient's complications, and create dummy variables for the most economically salient (as in whether the complication costs a lot) complications, like renal complications, which could lead to dialysis for life.  

### Data Evaluation
#### Positive
The dataset conform to all three good characteristics of big data. First, our dataset consists of the clinical records of 25000+ patients across the span of 8 years. Granted, the population, mostly consisting of Massachusetts residents, cannot stand for the general American population, but since Type II diabetes does not bias upon gender, race, income level or etc., the diversity of Boston population should suffice to represent the demographics in most major cities. Second, the dataset is always on, as long as Joslin Diabetes Center is still open for business. We can extend the horizon years into the future as long as IRB allows. Third, the subjects in our study are non-reactive, unaware their clinical data has been approved by the IRB for research use. Thus their decision to be compliant, or, more apparently, their clinical outcomes are not dependent on their awareness of whether they have been a subject of research.

#### Negative
The dataset also reflects certain negative attributes. First, it is inaccessible and sensitive by nature. Since the data contains sensitive patient information, both demographic and clinical, most certainly it will not be available for public consumption. Only personnel who have gone through HIPAA Law training can have access to it. Secondly, it is incomplete. Only a portion of patients are on record for all 8 years (5000+ out of 25000+), a problem that I have addressed above. Third, as mentioned in the **Data Manipulation and Operationalization** section, the data is very dirty as the insurance companies keep different styles of recording information, and the styles can change across years. Thus, a lot of efforts will be put into making the data in uniform format. Fourth, the ACA Reform took it precedence in Massachusetts in 2008. A lot of patients switched their insurance plan, or were mandated to be enrolled in one, which could affect their decision to be compliant, given the reduced or increased costs of their healthcare. To address this instance of drifting, I can exclude data from 2007 and 2008 and see if the results stand robust. 


## Research Design
Here, I am trying to find what factors have the most explanatory power over patients' decision to be compliant. Thus, compared to running descriptives (counting things), I will use linear regression models to account for the causal relationship, and rely on various predictive models to supplement and validate the discovered causal relationships. 


### Linear Regressions
#### Standard Linear Regressions
I will first run standard linear regressions for each year to see what factors have the most explanatory power over the outcome variables within each year, and if the most significant ones stay the same over the years.
#### Fixed-effects Linear Regression Model
A fixed-effects linear regression model will serve my purpose well in that it accounts for omitted variable bias for variables that remain unchanged over the 8 years. The health of individual person can be one example. Some people are healthier for genetic or habitual reasons, which can affect the clinical outcome. We can assume that such overall health condition remain constant over the period of 8 years. The fixed-effects model will help control for such unobserved variables.

As mentioned in **Data Manipulation and Operationalization** section, I will repeat the fixed-effects regressions on all datasets partitioned by the number of years the patients are on record, and see if the results agree for patients in various durations of treatment. 

### Predictive Models
To validate my findings with my linear regression models, I will build predictive models and see if the most predictive variables agree with the ones my regression models yield. To build the models I will use temporal cross-validation, namely using data from 2007(or 2009 if considering the effect of drifting)-2011 to build the model and data from 2012-2014 to validate the data. I will use neural net model to predict continuous variables like a1c, BMI and rehospitalization frequency, and use linear SVM and random forest to predict binary variables such as the range of if_complication dummy variables. 

### Comparison
The final step of my data analysis would be to compare the variables identified as statistically significant from my regression models and the most predictive variables from my predictive models and see if they agree. The root cause of patients' decision not to be compliant with their doctors' orders will most likely lie underneath the overlapped variables, and that would be where policy makers should devote their energy and money to.



## Bibliography
Delamater, A. M. "Improving Patient Adherence." Clinical Diabetes 24, no. 2 (2006): 71-77. doi:10.2337/diaclin.24.2.71.

Keehan, Sean P., Devin A. Stone, John A. Poisal, Gigi A. Cuckler, Andrea M. Sisko, Sheila D. Smith, Andrew J. Madison, Christian J. Wolfe, and Joseph M. Lizonitz. "National Health Expenditure Projections, 2016–25: Price Increases, Aging Push Sector To 20 Percent Of Economy." Health Affairs 36, no. 3 (2017): 553-63. doi:10.1377/hlthaff.2016.1627.

Thompson, Dennis. "Diabetes Care Tops U.S. Health Care Spending." WebMD. December 28, 2016. Accessed October 14, 2017. https://www.webmd.com/health-insurance/news/20161228/diabetes-takes-biggest-bite-out-of-us-health-care-spending#1.
