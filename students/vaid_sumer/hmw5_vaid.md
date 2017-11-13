Student: Sumer S. Vaid 

Assignment #5

Collaboration


##Kaggle Open Call Projects

###Part 1:
 
My username on Kaggle is sumervaid. 

###Part 2:

**Describe one competition that is of interest to you:**
 
I am interested in Corporación Favorita Grocery Sales Forecasting Competition.
 

**What is the goal of the competition? **

Grocery forecasting is a precarious business as success is contigent on accurately forecasting purchases and sales so items do not sell out (creating a loss due to lost sales) or are left in overstock (creating a loss due to perishable goods). This problem is magnified when one has to deal with stocks across many supermarket branches.  The goal of the competition is to build a model that accurately predicts product sales. The grocery chain currently uses a subjective and data-sparse method of predicting future forecasting. The goal of the competition is to replace this existing system with a better predicting, data driven machine learning model that can make accurate grocery predictions across locations. 


**What would you have to do to make a submission?**

I will have to enter into the competition before January 2018.  I will have to use the training data and supplementary information files to develop a machine learning model that can accurately forecast grocery sales for multiple locations of the grocery store, and for some items that were not present in the training data. Then I will have to test my model on the test data, and submit this .csv file to Kaggle. This .csv file will contain predictions about inventory requirements for the future. My predictions will be evaluated against a metric developed by the grocery chains that especially rewards correct predictions for perishable items. Following months in which grocery store sales were projected, the project with the closest match in quantity forecasted will win the competition. 

##Improving Journal Article


**"Find a paper that you think could have been reformualted as a human computation project. "**

Paper Title: Tifferet, S., & Vilnai-Yavetz, I. (2018). Self-presentation in LinkedIn portraits: Common features, gender, and occupational differences. Computers in Human Behavior, 80, 33-48.

The paper describes an analysis of 480 LinkedIn portraits which were analyzed for common features, gender and occupational differences. The goal of the study was to highlight variability in how men and women present themselves on their Linkedin portrait. A team of three coders analyzed nearly 500 LinkedIn portraits to extract similarities, based on a questionnaire 

**"How would you formulate the data collection as a human computation project"**

After portraits have been scraped from the appropriate LinkedIn profiles, I will use human computation to replace the three coders in the study. The researchers used only 480 portraits as they had three coders at their disposal, and were forced to optimize their resources under a constrained time frame. I will increase this number to 2000 portraits. Then, I will use human computation to collect data about the specific features of the portraits using the same questionnaire employed by the researchers. This project lends itself particuarly easily to human computation as coders do not need too much training to identify the overt physical features of LinkedIn portraits. For instance, the item that required the most training "face symmetry", in which participants had to determine if faces were skewed to the left or right direction in the photo. In this research, volunteers will first undergo a 19-photo training session in which they will learn to classify each of the 19-items used by the researchers. Then volunteers will complete a 20-item quiz in which they classify 20 portraits, each along the 19 portrait variables used by the researchers. A >90% accuracy performance on this quiz would transition volunteers into classifiers for the experiment. All coders will code all the 2000 portraits to maximize *redundancy*.

The collected data would first be filtered to remove responses from manipulating participants. Then a series of bias deduction studies will be implemented in which classifiers will code monochrome and physically altered versions of the LinkedIn portraits. The detected biases will be adjusted for. Finally, an iterative weighting procedure will be used to give greatest weighting to coding from best classifiers. 

**How might this improve the study?**

A human computation approach will allow the study to have a larger sample size. This will bolster the study as the present weakness of this research is its lack of cultural plurality. That is, the authors make it clear that their clustering of LinkedIn portraits is not applicable to non-Western cultures. Using the present human computation approach, we are able to sample a larger number of portraits that can be taken from LinkedIn profiles in India and Indonesia. Therefore, this approach will help generalize the authors' claims to other cultures. Second, this approach utilizes many more coders than those used by the authors. Hence, the resulting coding will reduce the likelihood of systematic biases possessed by the three specific coders in the initial study.Overall, if workers from cheap-labor markets are employed, this approach may save the costs assosciated with having full-time RAs to do the coding in the USA.

##Alternative Assignment: InfluenzaNet

**Compare and contrast the design, costs, and likely errors in InfluenzaNet, Google Flu Trends, and traditional influenza tracking systems.**

**InfluenzaNet:**

*Design*
Influenzanet relies on self-reported data to track the influenza trends in the general population. They do this by administering an ecological momentary assessment task to users weekly, who have to report influenza-like symptoms through a questionnaire. 

*Likely Errors*

First, this digitally-enhanced survey generates extremely sensitive data from patients which requires careful handling. Second, the accuracy of the patient's self-report data cannot be determined and hence it is difficult to exclude participants attempting to manipulate the study. Third, this type of a survey may induce healthy behavior in participants because of daily reminders, and therefore, a healthier sample than the population might be being sampled, reducing the accuracy of the trend. Fourth, it is possible that influenza manifests in different people with a range of different symptoms. Hence, predicting influenza onset from a description of ILI symptoms is an error-prone process. Fifth, it is likely that only those with any symptoms are more proactive users of the survey. This would bias the survey response towards symptomatic individuals.

*Cost*

The monetary cost of deploying ILI survey is greater than the cost of tracking influenza through Google Trends, but is lower than the cost of employing traditional data collection from participants. This is because while survey data-collection is expensive, it is not as resource-heavy as traditional reporting methods which are labor intensive. Google trends is cheaper to run than ILI because it capitalizes on an existing, dynamic database to track flu trends.  

**Traditional Influenza Tracking:**

*Design*

Traditional influenze tracking methodologies are chiefly reliant on data coming in from physicians and hospitals dealing with influenza-infected patients. This is different from the other two flu-tracking systems: physicians are collecting the data vs self-reports in InfluenzaNet and Google Trends does not rely on data collection to begin with.

*Likely Errors*

The chief weakness of this design is the time lag between the hospital treating influenza-based patients and sending a report of these patients to data collection agencies. This means that the traditional influenza tracking methodology is not in real time: it is always tracking influenza levels in the past. Second, this data is time consuming to compile and send on a regular basis, which increases the risk of human error. Third, infected patients who do not seek medical attention remain uncounted by this methodology, making it somewhat inaccurate. However, as a qualified physician is making assessments, this data is also more accurate than Google Influenza trends and subjective self-reported data. Moreover, this data is usually cleaner than the other two methods as this data is generated specifically with intent for analysis, which is not the case with Google Flu Trends or survey data. 

*Cost*

This is the most expensive method of collecting data about influenza as constant and careful coordination is required in between numerous hospitals and data collection agencies to track tehe trends. 


**Google Flu Trends**

*Design*

Google Flu Trends relies on search-term counts to track the level of flu-like illness in the population, in coordination with CDC data. It is unlike the other two flu-tracking systems because its design does not rely on overt data collection from patients. 

*Likely Errors* 

This data is usually heavily biased, as it assumes that search-terms directly correlate with ill-users. Moreover, the publicization of certain "flu periods" by the government could artificially cause trends to indicate a spike in ILI, whereas the underlying mechanism is the caution and alertness of the population to avoid getting sick. Second, the constantly dynamic nature of the Google search engine can produce system drifts that require vigilance in detection so the flu trend algorithm can be modified as the search engine is modified. Tweaks in Google's search algorithm can affect user behavior and thus influence potential future searches as well as current searches of flu-related terms. Furthermore, the "black-box" nature of this method prevents us from understanding the mediating factors that are causing increases in influenza. This can cause overfitting errors to arise, thereby making the trend tracker inaccurate. The reliance on CDC data brings the weaknesses of that design to Google Flu Trends. The tracker is suspectible to errors being caused by the CDC, which is a significant weakness. 

*Costs*

However, Google Flu Trends is the cheapest way of tracking influenza levels, albeit with a lot of noise, as it does not rely on overt data collection methods like the other flu-tracking systems. 



**Consider an unsettled time, such as the swine flu outbreak. Describe the possible errors in each system.**

**Google Flu Trends**

This tracking method will display inaccurate trends for two main reasons. First, the wide range of symptoms (ranging from sore throat to bad stomach) of Swine Flu will necessarily co-vary with symptoms of other illnesses. Hence, given that swine flu has large symptomatic variability, GFT will have to extract swine-flu specific trends in a mixture of trends tracking various syptom-specific illnesses. This will be difficult and will introduce noise in the trend. Second, as the government announces a pandemic of swine flu, baseline searches for its symptoms will increase. This will make it hard to delinate which search term frequency actually relate to instances of illness vs. instances of caution. Hence, GFT will likely produce a lot of false positives. 

**InfluenzaNet**

Based on the strain of the virus, quick onset of Swine flu might dissuade infected patients from answering weekly services so they can take care of their health instead. Hence, these surveys might show a slight increase in symptom one week and then record a large number of no responses the following week because the patients are sick. The time lag caused between analyzing which of the no responses were caused due to illness will cause a time delay in the trend tracking. It is also likely that patients stop responding after they have been sick and treated over a two week cycle. This will lead to the exclusion of partial data that would have otherwise revealed higher rates of swine flu. 

**Traditional Tracking Systems**

Swine flu is tricky to diagnose because its symptoms co-vary with many other flu-based illnesses. Hence, it is likely that there will be a lot of false positives and false negatives as doctors confuse flu-based illnesses with swine flu and vice versa. Second, swine flu's onset may be confused by patients as a case of bad stomach and/or food poisoning in which case there will be a time lag between onset of symptoms and doctor visit. This would delay the trend's indicative timeline. This delay would be made worse by the fact that hospitals would update the CDC in 2 week cycles. Hence, this system would be able to track swine flu rates, but there would be a lot of noise in the system and the trend would be delayed. 




