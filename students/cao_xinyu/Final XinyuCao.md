# Part1 Edelman and Luca (2014)
Question1: Digital Discrimination: Case of Airbnb.com
### Research Question:
Are black landlords being discriminated against at the online rental marketplace Airbnb? Is there a price gap among hosts of varying races? More precisely, is non-black hosts can charge higher rent compared to black hosts for an equivalent rental? Will black hosts receive a larger price penalty for having due to some poor rating, such as a bad location score, relative to non-black hosts?
## Research Design and Computational Enhancement
This paper first collected a dataset of the property’s characteristics and price on Airbnb, and a dataset of photo of the landlord. Then they hired a group of Mechanical Turk workers to rate for the quality of the picture of the property and the category the landlord’s race by their profile photo. By using the matching method with the quality of the property, the researchers can make a fair comparison of the renting price of landlord of different race. In the end, they identified that black host charge 12% less compared to nonblack.

They utilized the several methods to digital enhanced the observation study. First, three datasets of the characteristic property, profile photo of landlord and price of the property are the themselves digital trace data. They large digital trace make the analysis possible. The author collected the price, charateristic of the house, customer review and profile photo of the landlord to identify race. Without digital trace, it is very hard to collect all those informtion. Second, the data cleaning process evolved with human computing involved of Mechanical Turk Workers. Where researches pay very lower cost to clean data. In this case, the author asked the Mechanical Turk to rate the quality of the photo of the property and category the race of landlord by their profile photo.
### Digital Trace Data Collecting: 
the researchers collected a data set consists of a snapshot of listings contained on Airbnb for the New York City on July 17, 2012. 
1. Basic characteristics of the housing, combined data of the listed price the host is asking, the characteristics of the host, and the characteristics of the apartment. 
2. rating information, how many guests have left reviews, and the average rating for each host characteristic in Airbnb's structured rating system (location rating, checking rating, communication rating, cleanliness rating, and accuracy rating). 
3. Control for the Quality of the house: hired workers on Amazon Mechanical Turk to examine each listing's photos for a seven-point scale for the quality of the apartment, ranging from “This is a terrible apartment. I would not stay here at any price” to “This is an extremely nice apartment. I would stay here even if it were a lot more expensive than a nice hotel room. 
4. Racial Identification: downloaded all public profile pictures of New York City hosts and hired other group of workers to code the race of the hosts into one of the following categories: White, Black, Hispanic, Asian, Unclear but Non-white, Multiple Races, Not Applicable (no people in picture), or unclear/Uncertain.
### Counting and Matching:
1. Baseline Price Determinant Model: \
After collecting the data of the determinants of demand, they author analyzed the main factors will affects the prices on Airbnb, those include number accommodated, location rating, whether it is a safer place or not, social network presence, access to the whole apartment, and listing photos.
2. Baseline Racial Difference: \
at the beginning the author analyzed the different of non-black and black hosts, they author estimated significant rents different. 144 us dollar per nights vs 107 us dollar per nights.
3. Detangle Racial difference and racial discrimination: \
Because many factors influence the rents received by hosts and race is likely to correlated with some of these factors. The author then controlled all the information is public on Airbnb searching. They basically controlled the factors of price determination in baseline price determinants model. This allows research to remove the effects of non-racial factors. Controlling for these factors, non-black host ear roughly 12% more for a similar apartment with similar ratings and photos relative to black hosts.
## Strength and Weakness of the Paper
### Assessment of ten characteristic of digital data
1. Big:(Strength) \
the digital trace data is big. Therefore, the author can collect them collect data of feature of property, and hosts. With the big data, the author can model the price determinant utilizing rich features such as number of bedroom, bathroom, and location score. Thanks to the large data set, a precise racial gap of the black landlord and non-black landlord are identified.
2. Non-reactive: (Strength) \
This feature is the key factor when we are using digital trace data. Because if we conduct a survey people might subject to pressure and thus unlikely to reveal their true choice. However, in this case, the pricing is in a real-life situation, where their action reflects their true behavior.
3. Inaccessible:(Limitation) \
The big data held in hands of government and corporation are very likely unavailable. Partly due to the fact this could cause potential moral and legal issue for the institute. Partly because for company, they are not willing to release their property data without potential profitability. In this research, ideally both demand and price effects should be considered, however Airbnb are not willing to share data for this project. As a result, the paper foregoes analysis of consumer demand, and focus on the role of race in listing prices.
4. Sensitive: (Limitation) \
The digital trace data are public available on the internet. However, this does not mean everyone could use it. Certain issue should be addressed, such as ethnic concern, leaking data might cause emotional harm, such as embarrassment for guests who discriminate black landlord. Besides, it also could lead to litigation for violating terms of agreement, breaking privacy concern for both individuals and companies. 
5. Dirty: (Overcome of the Limitation) \
The digital data is dirty. In this research design, it explicitly showed this feature. Many variables in dataset are not directly available for use. However, the author encounters this feature wisely. The hired Mechanical Turk Worker to deal with the data, thus successfully dealt with the problem with low cost.
6. non-representative: (Overcome of the Limitation) \
This case study focuses on for this online market design, i.e. the Airbnb's trust building design. Therefore, even user of Airbnb is more likely to be young generation living in the city, and does not represent US population of short term rent market. The study still valid due to a narrow-defined research question.
### Assessment of Validity, heterogeneity of treatment effects, and causal mechanism
1. Causal mechanism:(Strength and Limitation) \
On the one hand, this paper makes a good case that black landlord are being discriminated and price 12% less compared to white landlord of comparable property. Furthermore, this paper further discussed why such gap exist, what is the factor could be most related. This paper find that black host are most largely penalized by a poor location rating, which indicating a place is not safe. This might be interesting to further exploit for people might have prejudice linking black people with violence and unsafe, thus lower the score.
On the other hand, this paper lack of demand data makes the case incomplete and less justified. I would guess that might be one of the reason this paper has not published in a well-recognized economics journal as (Edelman and Luca) 2017.  Because, it is possible that black landlord pricing lower and have a higher demand, thus they still earn a higher profit. It could be alternative explanation that it is not people are discriminate black landlord, rather black landlord employed a different “low pricing high sales” strategy compared to their peers.
2. External Validity:(Limitation) \
This paper narrows down the question into whether mechanism design, sharing racial information of buyer and sellers before the deal is done, exhibits racial discrimination. Thus, this research results are only likely to be reproduce at online market, rather than all online market, such as eBay where people could not see racial information.
3. Internal Validity:(Limitation) \
names are related with social and economic background. This paper observed a discrimination against black names, this might be that host are not discriminated against black people but rather against people from disadvantaged social background. Thus, the lower responsive rate may not be explained as racial discrimination, rather a social economical background discrimination. The author is fully aware of Fryer and Levitt (2004) paper while did not test for robustness of the issue, this might be interesting for further investigation. 
4. Heterogeneity of treatment effects:(Limitation) \
This paper does not take good care of heterogeneity of the treatment effects. The study does using matching strategies to make a fair comparison for the black and non-black hosts, thus a valid argument for there is a difference price of similar quality property are priced lower than their counterpart owned by nonblack. However, this paper does not further exploit if the property is in the high-end price quantile or low-end price quantile might have different treatment effects. Also, this paper could have considered if the landlord is women would this influence the results.

# Part 2 Edelman and Luca (2017)
Question 2: Racial Discrimination in the Sharing economy: Evidence from a field Experiment
## Research Question
While Edelman and Luca (2014) paper made a lengthy discussion of racial discrimination of the demand side of the online rental market, Edelman and Luca (2017) paper studied the supply side of the online digital market. They tried to answer the question, will African American guest in Airbnb be discriminated against by the hosts? They designed a research operationalized the discrimination by the difference of response rate by hosts of the guest with African American name compared to guest with White American name.
## Summary of Research Design and Computational Enhancement
In the experiment of the author, they first collect the digital trace data of properties' characteristics and then applied the human computing method by hiring a group of Mechanical Turk workers to assess those digital trace data for race, gender, and age information. After collecting the basic feature data of the properties, the team created 20 accounts and conducted a digital experiment using existing platform to measure the responsive rate of same profile associated with black or white name. With controlling all the feature, the author documented a consistent discrimination among different groups of hosts, yield 8% gap of response rate of guest with white and black name.

This paper is digital enhanced in several ways. First, it has a component of digital trace data as Edelman and Luca (2014) paper. Second, it also employed a group of people from Mechanical Turk to help clean the dirty big data. Third, it utilized the existing digital environment to conduct digital experiment. They send message via Airbnb’s website, this makes the study much cheaper compared to traditional method involved with more labor such as phone call or presented in person. Fourth, it utilized a facial recoginization techiques to identifies the race of the profile photo of the landlord.
### Digital Trace Data: 
The author collected all properties offered on Airbnb in Baltimore, Dallas, Los Angeles, St. Louis and Washington, DC as of July 2015. To reduce the burden of landlord, each landlord will only receive one Email for a randomly selected property. The following data are collected:
1. Host's profile page data: collected the profile image, hired Mechanical Turk Workers to assess each host image for race, gender, and age, and roughly categorized hosts by race, gender, and age.
2. number of properties each host offers, number of reviews the host has received, the image of past guests who previously reviewed the host. And use Face++ to categorize past guests by race, gender, and age.
3. information of each list: price of the listing, the number of bedrooms and bathrooms, the cancellation policy, cleaning fee, and rating from past guests, entire unit versus a room in a larger unit.
4. longitude and latitude for location of neighborhood's demographics
5. whether hosts were ultimately able to fill openings. The guests inquired about the reservations eight weeks in advanced, and the team checked again on the day before the reservation day if this property is still available or not.
### Randomized Control Trial: 
The author created 20 accounts to contact hosts for five different cities in Airbnb. The accounts were created almost identifcal, expcet their name are different. Each five of them are created with names that signaled African American males, African American females, white males, and white females from birth certificates of babies born between 1974 and 1979 in Massachusetts.This form a randomized control trial which is highly regards in many social science and medical research where precise lab controlled experiment like experiment physics is not possible.
### Digital Experiment: 
1. hypothetic accounts creation, identical in all respects except for guest names. It has ten distinctive African American and ten white names, each have five male and five female names within group. To avoid confounds, the paper only uses names and no picture of the putative guest. 
2. messages sending, roughly 6,400 messages are send between July 7,2015 and July 30, 2015. Each message inquired about availability during a specific weekend in September. When a host replied to a guest, the team send a personal message clarifying that the guest was still not sure to reduce the likelihood of a host holding inventory for hypothetical guests. The response was 1 of 6 groups: “No response” (if the host did not respond within 30 days); “No or listing is unavailable;” “Yes;” “Request for more information” (if the host responded with questions for the guest); “Yes, with questions” (if the host approved the stay but also asked questions); “Check back later for definitive answer;” and “I will get back to you.” 
3. Regression: the author estimated the gap across these specification, controlling for the host's gender, race and an indicator for whether the host has multiple listings, an indicator for whether the property is shared, host experience (whether the host has more than ten reviews), and the log of the listing price.
## Strength and Weakness of Design
### Assessment of 10 characteristics of big data
1. Big:(Strength) \
the digital trace data is big; therefore they author could collect on a large data set and are able to do categorical analysis based on the characteristics of the landlord. For example, they study that the discrimination against black people is consistent among different group of people. 
2. Inaccessible and Sensitive:(Limitation) \
To begin with the ethnic issue is of much a concern when we trying to utilize digital trace data or apply randomized trial on human subjects. In general, I think that to stop the racial discrimination, sending hypothetical information is within the framework of the law of US and supported by many cases. But still the data collection process showed to us that the big data are in nature sensitive and sometimes even inaccessible. 
Judging from the paper, we know that there are many more data are held by Airbnb and not willing to share with the researchers. On one hand, this might due to the fact of users' term of agreement of the Airbnb website, which make Airbnb has limited ability to share data with third party and are bounded by potential legal concern. On the other hand, this might due to the fact there will no business interest or even adverse interest in this case, where the author argued the unique mechanism design of Airbnb is problematic, for Airbnb. 
Without the permission of the Airbnb, the web crawling and message sending using hypothetical account of the website of Airbnb might be a violation of terms of agreement of the website. The event upgraded when the Airbnb stopped their account from accessing Airbnb’s data. They did not further conduct the analysis after five cities, which is helpful for avoiding further legal consequences.  
3. Overcome of the issue of non-representative:(Strength) \
This is because this paper is focused on this online market mechanism design, i.e. the trust building process of sharing information, which the author think could lead to potential discrimination results. Thus, though the sample which on website is not a representative of us population, it does not harm the validity of the research that much. 

### Assessment of Validity, heterogeneity of treatment effects, and causal mechanism
1. Causal mechanism:(Strength) \
this paper clearly identified the discrimination from the fact there is 8% gap between the difference of hosts' response rate to the white and African American. This paper applied the golden standard of social science of randomized control trail. Thus, undoubtedly showed to the reader that there exists a bias against black name in online digital market. It is clear the reason why some people receive a lower responsive rate is because their name could be associated with black. 
2. External Validity:(Both strength and Limitation exist) \
first, this paper is clearly narrow down the problem to the mechanism design of the Airbnb and argue that the method Airbnb use facilitate the racial discrimination. Thus, the results should only apply to similar website which also provide information of the racial profile, rather than all online short-term rental platform like expedient all together. 
3. Internal Validity:(Limitation) \
names are related with social and economic background. This paper observed a discrimination against black names, this might be that host are not discriminated against black people but rather against people from disadvantaged social background. Thus, the lower responsive rate may not be explained as racial discrimination, rather a social economical background discrimination. The author is fully aware of Fryer and Levitt (2004) paper while did not test for robustness of the issue, this might be interesting for further investigation. 
4. Heterogeneity of treatment effects:(Strength) \
This paper taken good care of heterogeneity of the treatment effects. This study examined different effects among different group of hosts. The results are remarkably persistent, both African American and white hosts discriminate against African American; both male and female hosts discriminate; both male and female African American guests are discriminated. Both high end and low-end units, both diverse and homogenous neighborhoods.


# Part 3
Comparisons of the two papers
## Why we should use both method?
To begin with, we should note that usually in any filed experiment design, it requires supplementary design of observation data collection. Take Edelman and Luca (2017) as an example, the author conducted a field experiment to get a responsive rate data of different race on one hand, and collected the digital trace data of the landlord, and the property to matching with the responsive rate difference in order to enhance their digital experiment design.  
### What could we learn from the observation? 
From the public available information of Airbnb, we can utilize the information of all the property such as price, location rating, and picture quality etc., and the profile picture of the landlord. Thus, it is possible for the author to categorize the data into different racial group. Simply by counting things and a tiny bit of categorize, we can say that the property listed by a Black host on average have much lower price compared to the property of a non-black host. 
### What could we learn from the experiment?
Ideally, big data is big, it could help us identify the small differences. With the full digital trace, if the team has the data from Airbnb, the team could observe the difference of the responsive rate between guest who could be identified as white and the guest who could be identified as black. By using the matching strategies, the author should be able to make causal estimation of the existence of racial and responsive rate.

However, in this case, the actual responsive data is withheld by Airbnb.  To get an estimation of the difference of responsive rate, the author conducted a field experiment by using existing platform of Airbnb to test if they will have a different rate of response for the same Message of a profile one with a distinctive black name and one with a distinctive white name. From this experiment, we know not only the black host has to charge a 12% of price lower in the market as the observation method suggested, but also the black guest is subject to an 8% higher of refuse rate. These two ways of discrimination showed to us that the market design of Airbnb is suffered from critics of racial justice.  
## Digital Survey Based Research design
If I were to implement a research design for survey study of racial discrimination. I will implement a pricing game at Amazon Turk. Because we already have the data of Airbnb, we could use those data to randomly generate characteristics of a property. For example: 
~~~~

        An apartment 
        Bed rooms: 3 
        Location rating: 8
        Checking rating: 8.5 
~~~~
One of the thing we need to consider is we should be careful about matching photo with those properties. Both profile photos of landlord and photo of the property are very important for decision making. However, those photos are highly sensitive. In order to avoid those ethic and legal concerns, instead of using the photo of Airbnb website directly, we could apply a machine learning technique in (Dosovitskiy, et. 2016)  to match the photo with property, then we could randomly generalize a photo with those features using machine learning method.

After we generate our desired property and linking it with photo with the feature, we could ask the Amazon Turk workers to rate on the quality photo and then give an estimation of the price of house. Then we could collect the pricing information they give to study both the price and demand of the problem. 

Ideally, we could use a wiki survey, so that we could ask why they price the property in that way. Through this process, we might be able to increase our survey and find some more reason why people pricing differently. This could exploit the advantage of survey, that is we could only know what people think by asking them questions.
### Drawbacks
1. Reactive: \
The biggest drawback is that when you conduct a human administrated survey, people are unlikely to tell you that they will discriminate against black people. Their behavior is responsive in the survey unlike the real behavior in non-observed manner. This phenomenon could obscure our research design.
2. Expensive: \
Compared to the big data in the observation and experiment design. The survey method will be more expensive. Because recruit people to hand in survey will be more expensive than letting people to answer a question in their daily setting with disguise.
3. Non-representative: \
Compared to the whole population of the observation and experiment design, the survey method suffers from a high non-responsive rate problem. Thus, leads to the sample population different from the population we are targeting, the people who use online short-term rental tools.
4. Sensitive: \
Undoubtedly, the research design is sensitive, because use the information could be identifiable is problematic. Especially when we randomly generate a sample of property. Even if we already depersonalize the information. Such as we do not use the profile photo, and we use self-taken photo or photo purchase for our research in the market.

### Overcome
1. Survey Using Amazon Turk: \
First, Amazon Mechanical Turk is an inexpensive way to collect survey information. it is much cheaper compared to the traditional method. Because the worker on Amazon Turk are more flexible and have no cost for stopping by or hiring people to conduct survey sampling, we could attract survey respond with a very much low price compare to traditional method. \
Second, MTurk is far better compared with traditional method in terms of representatively. The population on Amazon Mechanical Turk is younger and thus fit better to the target population, people who rent or lease property on Airbnb, compared to traditional survey method. Thus, we could at least overcome part of non-representative issue. \
Third, MTurk is better to reduce the reactive issue, because in anonymous computer administered survey, people are more likely to reflect their real belief without afraid of embarrassment of being viewed as racists if they showed racial prejudice in the survey.
2. Gamification: \
Traditional survey method is problematic because people are reactive towards the survey, in this case, people might conceal their true intention of racial discrimination. My research design utilizes the gamification strategy to let the participant to evaluate the price for the rent. Thus, they are more attracted by other characteristics and making a price decision based on their true intention.
3. Machine Learning photo generating: \
On one hand, using original photo is very sensitive; on the other hand, photo is one of the critical factor that decided the pricing of the property listing on the website. For example, we could apply the convolution network method in (Dosovitskiy, et. 2016) paper first to match the feature with the photo and then randomly generate the photo with our desired feature without the concern of privacy. 
4. Poststratification: \
For non-representative issue, we could try to use post stratification to adjust the weight of the sample, so that we are able to construct a representative sample. Although this might not be a large issue, since the author observed a persistent discrimination among all groups.



## Reference
1. Edelman, Benjamin G., and Michael Luca. "Digital discrimination: The case of Airbnb. com." (2014).
2. Fryer Jr, Roland G., and Steven D. Levitt. "The causes and consequences of distinctively black names." *The Quarterly Journal of Economics* 119, no. 3 (2004): 767-805.
3. Edelman, Benjamin, Michael Luca, and Dan Svirsky. "Racial discrimination in the sharing economy: Evidence from a field experiment." American Economic Journal: Applied Economics 9, no. 2 (2017): 1-22.
4. Dosovitskiy, Alexey, and Thomas Brox. "Generating images with perceptual similarity metrics based on deep networks." In Advances in Neural Information Processing Systems, pp. 658-666. 2016.
5. Salganik, Matthew J. Bit by bit: social research in the digital age. Princeton University Press, 2017.