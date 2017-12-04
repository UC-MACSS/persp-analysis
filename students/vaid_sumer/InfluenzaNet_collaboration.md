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