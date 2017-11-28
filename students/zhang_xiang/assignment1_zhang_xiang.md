## Do Physicians' Financial Incentives Affect Medical Expenditure: Evidence from China

#### Perspective in Computational Analysis, Assignment 1
#### Name: Xiang Zhang
#### October 12th, 2017

### Introduction

In almost every country, health-care costs have been rapidly rising as a share of Gross Domestic Product (GDP) in recent years. In the United States, for example, the share was 5.2 percent in 1950, 9.4 percent in 1975, and 17.1 percent in 2014 (Hall and Jones, 2007; World Bank). China also experience a fast rising of health expenditure in recent years. In 2007, the country spent 4.35% GDP on healthcare system, however, by 2015, the share increased by 38% and reached 6.0% (China NHFPC). In academia, critics contend that fee-for-service reimbursement policy leads to high medical expenditures without improving patient health (for example, Ginsburg, 2008). Thus, a key empirical question to be tested is, do physicians do have incentives to gain more profit by writing more prescriptions?

Although this question is extremely important, evidence is scant in how physicians’ financial incentives influence the quantity, composition, and value of health care they provide. Studying whether physicians' financial incentives may affect their treatment patterns has proven to be difficult. On top of this, it is difficult to access large data sets on medical claims. Traditional survey data do not have record on physicians' diagnosis and therapies, nor do they have precise records on patients' expenditures. Using such low-quality survey dataset, researchers are not able to directly test this hypothesis.  

In this research, I exploit the remarkable richness of **New Rural Cooperative Medical Insurance Claim Dataset** of Sichuan Province, China, to study how changes in physicians’ financial incentives influence the quantity and value of health care they provide using a quasi-experiment design. In 2010, Sichuan province carried out a reform which increased the reimbursement rate of several medicines on chronic disease, and then by taking a standard difference-in-difference specification, I'm able to detect whether such financial incentives (the increased reimbursement rate) will change the treatment patterns of physicians.

### Dataset
The dataset I use is the de-identifies New Rural Cooperative Medical Insurance Claim Dataset, provided by Health and Family Plan Commission of Sichuan Province, China. The New Cooperative Medical Scheme (NCMS) is a heavily subsidized voluntary health insurance program established in 2003 to reduce the risk of catastrophic health spending for rural residents in China (Ma et al. 2012). The data documents all claims associated with all NRCMI beneficiary population (**668.5 million** rural residents in Sichuan) for each year from 2006 through 2014. The data contain itemized reports of the services purchased for them by NRCMI, and I can obtain demographic information (age, gender, education) in it.

### Research Design
#### Identification
In 2010, Sichuan carried out a reform on its NCMS system. From 2010 on, Sichuan province started to reimburse its rural residents' chronic medication expenditures. In 2010, the reimbursement rate was set to be 50% and fourteen different types of medicines used for controlling blood pressure are reimbursed, and this change offered us a great chance to detect how financial incentives will affect physicians' therapies and the amount of medicines they prescribe for. By comparing the medical expenditure changes in these fourteen types of medicine with other chronic medication not reimbursed (both before reform and after reform), we can see the distortion of physicians' therapy patterns and detect how financial incentives may affect physicians' therapy.

#### Econometric Model
The main research design is the commonly used difference-in-difference model in economics. In our specification, the "treatment group" is the chronic medicines that are reimbursed, and the "control group" is consists of chronic medication that are not reimbursed. By comparing the outcome of treatment group with control group both before and after reform, we can study the impact of financial incentives on physicians’ therapy.

To illustrate my specification, I briefly introduce my empirical strategy here. In my specification, I could estimate the following equation at physician level:

          y_it = beta_0 + Treatment_i + Post_i + \delta Post_i * Treatment_i + theta*X_it' + e_ist

where the outcome variable is the amount of each type of medicine each physician prescribes in year t; the Treatment_i is a dummy on whether the medicine is in control group; the Post_i is a dummy indicating whether the outcome is observed after the reform; X_it is a set of control variables at individual level; the coefficient "delta" of the interaction term is of my interest.  

### Critiques and Discussion
#### How does this project illustrate the good characteristics of big data
My research exploit two great characteristics of big data, big, and non-reactive. In this section, I will explain in detail how my research design takes advantage of these two characteristics and how big data will help me make some contribution on testing the existence of incentive-driven prescriptions.

First of all, my research design makes use of a province's NRCMI medical claim data, which is a extremely big dataset with rich information. On the one hand, since I can observe the therapy of the same physician on the same medicine for multiple times, such longitudinal nature of this dataset could help with drawing causal inference. As I have explained, I can use a quasi-experiment design to try to get something causal. On the other hand, the data have pretty detailed information on physicians' diagnosis and personal background (e.g. years of education, seniority), and this would help me detect the heterogeneity of the prescription of different physicians. For example, it could help me detect when will physicians, or what kind of physicians, are more likely to prescribe more medication, which is of great policy importance. Moreover, this dataset allows me to observe a large population's medical expenditure over a long time-period (668.5 million participants during 2006 and 2014), which could significantly improve the statistic power and the precision of my estimation.

Also, it has a great nature of non-reactive. If you surveyed a physician about whether she had the incentive to earn more by prescribing more medication, then we are sure to get a biased estimation (under estimation) since physicians with such incentive are likely to say no when they are asked about it. However, in the NRCMI dataset, all what physicians do are recorded and physicians cannot respond to it. Conceptually, if a physician wants to get reimbursed from the government, she must write the prescription and thus I can directly observe the amount of medication she prescribes.

#### How this project illustrates the bad characteristics of big data
Although the data shares some good features of big data, there are also two evident shortcomings of this dataset, namely, dirty and sensitive.

The first to mention is dirty. The dataset itself is just so large and all data are collected from different hospitals and clinics. So a problem here is, the ways they code medicine are quite different. For example, in some area, they may use ICD-10 coding system (The 10th version of International Statistical Classification of Diseases and Related Health Problems, ICD10), and in some area, they may use China's National Standard Code. Under these two different systems, the same medicine might be assigned two totally different codes. In order to overcome this problem, I may need to match the code for the same medicine in these two different systems (like writing a dictionary). What is more important is, there might be some coding errors in the system and decrease the quality of this dataset. The fact is, China have not introduced digital coding system until recent years, thus, some physicians might be unfamiliar with it and make some errors when using it, which might result in some coding errors and lower data quality. Since the dataset is pretty large, and it is collected from numerous hospitals and clinics from a large number of physicians, such coding error is no longer negligible. Thus, before I start using the data, I may need to justify the quality of the data. Following standard economic literature, I may aggregate the data, compute the distribution of key variables and compare it with existing government surveys or statistics.

The second problem regarding this dataset is sensitivity. Although the dataset is de-identified, but since it still contains very specific individual information (address, health insurance ID, etc.), so it is still quite sensitive. To make sure my research will do no harm to those people, before using it, I will prepare a report for ethic review, and only by doing so can I lower the probability of embarrassing or doing harm to someone.

### Reference
China NHFPC, https://www.nhfpc.gov.cn

Ginsburg, Paul B. "Reforming provider payment—the price side of the equation." New England Journal of Medicine 365, no. 14 (2011): 1268-1270.

Hall, Robert E., and Charles I. Jones. "The value of life and the rise in health spending." The Quarterly Journal of Economics 122, no. 1 (2007): 39-72.

Ma, Yuqin, Lulu Zhang, and Qian Chen. "China’s new cooperative medical scheme for rural residents: popularity of broad coverage poses challenges for costs." Health Affairs 31, no. 5 (2012): 1058-1064.

World Bank, https://data.worldbank.org/
