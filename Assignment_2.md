**Trends in Student Stress and Sociability Levels Over An Academic Term**

*by Sumer Vaid* 

**Research Question and Plan**

How do student sociability and stress-level fluctuate over an academic term? I intend to use a digitally enhanced survey to answer this question. I will deploy my survey in an urbanized region of India that has seen accelerating rates of suicide due to academic stress. 

[^1]: http://www.hindustantimes.com/india-news/engineering-aspirant-commits-suicide-in-kota-after-failing-to-clear-jee-main/story-H7troM8YJYSQFkb5JBfL6H.html

The ultimate goal would be to use overall sociability and stress level trend fluctuations to determine vulnerable moments that potentially lead to self-harm so appropriate interventions can be staged. 

**Data Collection Method **

I will use the StudentLife application and Qualtrics to administer daily surveys and collect mobile sensing data, employing an EMA design.

[^2]:  http://studentlife.cs.dartmouth.edu/

The StudentLife app collects relevant mobile sensing data that can supplement the survey self-reports. The researchers who developed StudentLife will allow me to use the application as this cross-cultural research design facilitates the project’s mission of “spurring human behavior data mining research”. 

The students will use the app for a full academic term that lasts 2 continuous years. They will not use the app during holidays. The students will be incentivized to participate in the experiment as a final assignment for their classes will require them to use their own generated data from the survey. Each student will receive a pdf report showing them their trends of sociability and stress nearing the end of each year that composes an academic term.  The teaching institution will not oppose this idea or the project itself as it ultimately seeks to temper rates of suicide, solving a key problem for the institutions and alleviating concerns of other parents. 

Sociability will be assessed through 1 explicit self-report questionnaire administered daily.   This explicit sociability questionnaire will be borrowed from A.R. Gilliland and colleagues and will be optimized for an EMA design.

[^3]: https://www.researchgate.net/publication/232565963_A_measure_of_sociability

 These data will be supplemented through the use of the audio-classifier in StudentLife that can distinguish between noise, silence, and voice in the microphone input. The classifier “taps” into phone-based conversations every 2 minutes to determine the proportion of noise, silence, and voice for a fixed duration of the phone call. Increased voice-based conversations are concluded as being indicators of sociability. In the event that StudentLife does not grant us access to their software, we will still be able to locate and use an audio classifer with relative ease, as extensive computer science research has delinated and constructed such a feature priorly. 

[^3a]: https://dl.acm.org/citation.cfm?id=1555834

The Perceived Stress Scale will be used as the explicit self-report questionnaire administered daily to measure stress levels.

[^4]:  http://www.mindgarden.com/132-perceived-stress-scale

To supplement these data, an additional single-item questionnaire will be administered to the students - The Mobile Stress Meter.

[^5]:  http://studentlife.cs.dartmouth.edu/mpsm.pdf 

**Justification for Digital Enhancement**

The present research design is digitally enhanced because it relies on smartphones, mobile sensing and machine learning methods to infer and track behavioral trends over long time frames. It would be difficult and expensive, if not impossible, to conduct a non-digitally enhanced version of this research. 
Stress and sociability are psychological concepts that are difficult to infer from purely observational data. The biosensing technology required to detect increased stress level purely from biomarkers (i.e heart-rate) is currently not available cheaply and easily. Moreover, collecting this type of data would only be plausible for those students who have an expensive, modern smartphone equipped with a host of sensors, thereby introducing selective sampling errors. Other observational indexes of stress vary largely from person to person and are often disguised beneath an outward social impression. These problems make stress particularly difficult to infer from means other than self-report, surveying and physiological measures such as saliva samples.

 
**Comparitive benefits over purely observation study**

Sociability can be inferred from observational Facebook data, but the social network does not see sustained, consistent and high usage in the Indian region in which the study will be deployed. This is primarily because Facebook is considered a distraction in the Indian culture, and viewed as antithetical to work and study, discouraging students from regular use. Hence, digital footprint data cannot be used to infer sociability in this specific case. By using a survey-design instead of an observation design, we limit sampling errors originating from variations in smartphone sophistication, individual differences in social media use and are able to operationalize psychological constructs like stress, that are near-impossible to infer from pure observation. Note that while our design requires that individuals have smartphones so they can complete our surveys, we do not utilize other smartphone features (i.e accelerometer, gyroscope) in our design. Even the most basic smartphone contains a microphone, allowing us to collect our voice-data equally well from participants with a wide range of smartphones. 

Secondly, this research deploys the amplified asking method which seeks to enrich self-reported data with observational data. We employ this technique in developing trends of student sociability over an academic  term. Hence, this mixed design takes advantage of the strengths of both methods to generate good quality data. 


**Potential Weaknesses in Survey Design and Solutions**

The weaknesses of our design originate primarily from the EMA component. The administration of the EMA survey requires knowledge of smartphone use which disqualifies non-technologically advanced students from our survey. This reduces the external validity of our research.  However, the proportion of students without a smartphone is very low compared to those who owned one. Hence, we expect our data to have high external validity in technologically savvy populations. Additionally, our research is based on a cross-cultural premise, to begin with, anyway enriching the existing psychological literature on stress and sociability by examining traditionally underrepresented populations in a small Indian city. 

We rely on Qualtrics to administer our daily survey, making us dangerously dependent on the website for the sound collection of our data. This is not a major concern as the service has a history of high reliability and dependency, with little to no downtime. 

Reporting levels of sociability and stress daily may introduce the Hawthorne effect in our participant pool, by urging them to change their natural behavior because of daily introspection. This will limit the external validity of our trends. Our design, however, minimizes the amount of time required to take the survey, thereby tempering the level of introspection insinuated by the survey. For instance, the Mobile Stress Meter is only a one-item questionnaire which takes less than 5 seconds to complete. Our reliance on the audio-classifier to infer sociability trends eliminates the need for two explicit measures of sociability, thereby minimizing the time students spend taking actual surveys and thinking about their responses and behavior. 

We collect a host of personal data from students which has a high potential for harm. The data will require careful management to ensure that these risks are minimized. Measures such as anonymizing the data at the point of creation will be required to alleviate privacy concerns. Furthermore, we will allow students to turn off their data-stream at any given time to alleviate concerns of unwanted data sharing. Students can choose to skip daily EMA measures whenever they like. 

While we intend to use informed consent to conduct this research, the nature of this consent remains unclear as students are required to use the survey data for a class assignment. Hence the extent to which they are being coerced through academic pressure in the assignment will need to be delineated. We intend to hold discussion sessions of consensual agreement with students to adequately deal with the complicated nature of consent in this study. Importantly, we will offer alternatives assignment options for those students who do not wish to partake in the study. This will ensure that the informed consent to participate in this study is truly given after access to relevant information about the study. 

We predict that as sociability tapers off and stress levels rise, we will see increased likelihood for self-harm. We attempt to provide third-party counseling help for students at times when we see these variations in sociability and stress levels. The ethical question of discouraging self-harm in students invades the personal freedom of said individuals is a relevant one. For instance, some students may believe that by offering automated help to them during times they are susceptible to self-harm is a violation of their personal freedom of action. We will clarify this ethical dilemma in the sessions for obtaining full consent so students are able to express concerns such as these. Additionally, we approach this survey deployment first as scientists and then as ethicists. We are primarily interested in the knowledge gain resulting from our data collection, but we would also like to reduce suicide rates if we can. To that extent, we will allow students to turn off the counseling feature if they so wish. This will allow us to collect data from all students, regardless of whether or not they seek the counseling that will help them reduce potential self-harm. This will increase the diversity of our sample, increasing external validity. 

Lastly, this is a good time to do this study as attempted suicide is no longer a crime in India.

[^6]: **https://www.thenational.ae/world/attempted-suicide-no-longer-a-crime-as-india-changes-attitude-to-mental-health-problems-1.55290**

This alleviates student concern of potential legal ramifications of predicting an instance of future attempted suicide, which may have had legal consequences in the past. 