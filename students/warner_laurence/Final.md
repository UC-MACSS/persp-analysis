# Perspectives 1 Final: Evaluating Research Designs

### Laurence Warner
Question titles are summarized.

#### Edelman & Luca (2014)

#### Summarize the research design and explain how the research design leverages computational methods to ask and answer a question.

1. Collect observational data on Airbnb listings
I group the variables in the following way:
  * Publicly available numerical variables
   Price, accommodation (bedrooms, no. accommodated), ratings
   Research strategy of Counting used. Presumably web scraping tools are utilized to save human effort.
  * Pictures
    Host picture. Used to determine race categories.
    Property pictures. Used to quantify perceived property quality.
The research design uses human computation for both of those tasks. The writers employ Amazon MTurk workers to perform the task of categorizing race and quantifying apartment quality from pictures. The authors hope that MTurk workers's quantitative assessment of quality are representative of user's assessment of quality.

2. Run linear regression models with price as dependent variable and 'black host' as one of the explanatory variables
This aims to assess the causal effect of 'black host' by controlling for all other relevant factors.
Computer software is used to run the regression.

#### Evaluate the effectiveness of the paper's research design independently. What do we learn from the paper on its own? What are the limitations of the paper on its own?

##### What we learn
We have the powerful result that in the real world, non-black hosts charge 12% more. This result is particularly powerful due to two factors. Firstly, size. The dataset encompasses all listings in New York at a given time. There is no sampling bias here. Secondly, non-reactivity. Users do not have an opportunity to change their behaviour to cover up discrimination.

##### Limitations
There are few limitations in this study. However, the main concern with the result is whether we have adequately controlled for perceived quality. The data is incomplete because it doesn't convey the internal states of the buyer's when they view the photos. We infer them using the MTurk's opinions.

In addition, the study offers no guidance as to whether the discrimination is taste-based or inference-based. Clearly, a few photos are not enough to inform a complete picture of expected quality, so buyers may use superficial information about sellers to form predictions about ex-post quality in an inference-based manner.

#### Edelman & Svirsky (2017)

#### Summarize the research design and explain how the research design leverages computational methods to ask and answer a question.

This is a digital, field randomized controlled experiment, using the existing environment of the airbnb platform. It is controlled because guest accounts are identical except name. It is randomized because which sellers are contacted is random. In terms of Salganik's experimental framework:
Recruit: 6,400 hosts are recruited computationally.
Randomize: between-subject design: hosts randomly chosen
Intervene: messages sent using automatic computation tools
Measure: Yes/no responses directly measured. Other outcome variables scraped too.

In order to assess hetereogeneous treatment effects, the authors collect rich data on the sellers uses data scraping tools, in the same way as they did in their 2014 paper above (using MTurk), although it seems that there have been improvements in their methods: multiple MTurks per photo etc.

#### Evaluate the effectiveness of the paper's research design independently. What do we learn from the paper on its own? What are the limitations of the paper on its own?

##### What we learn
This experiment has pretty strong validity.
Statistical conclusion validity: high sample size.
Internal validity: experiment performed correctly.
Construct validity: there is a question as to whether the name alone captures racial discrimination. This is particularly the case because there is no photo, so it is not a common type of discrimination in the real world.
External validity: the five cities are fairly representative.

We learn about hetereogeneous treatment effects depending on host race, gender, past hosting etc.

##### Limitations
I do question the external validity of the study when photos and other rich information about individuals is included. Hosts may be discriminating more due to the amount of uncertainty about the potential guests due to the lean profiles.

We also don't find out about the causal mechanism. Is it taste-based or inference-based discrimination?

#### Identify the value-added of conducting both research projects.

##### What does experiment add to observational study?
One problem with causal inference from observational studies is we can never be sure the treatment variable is not correlated with unobserved variables. Hence, there is some doubt about making causal inference from the observational data.
The experiment allows us to be more confident that there is indeed a causal link between race and airbnb behavior.

In addition, the experiment allows the authors to fine-tune the variable of interest - race - more, because they create the names, compared to the observational data which is more messy, and race is inferred by MTurk workers.

##### What does observational study add to experiment?
The experiment lacks external validity, because it is an unrealistic scenario of guests with no photos and ethnically extreme names.
The observational study has maximal external validity because it is actually rich data taken from the real-world. This allows us to be more confident about the actual existence of discrimination on airbnb.

It should be noted that the 2017 paper actually includes an observational study as cross-validation in it already.

#### Consider how you could apply a digital survey-based research design.
The primary question of interest is: do airbnb users discriminate based purely on race of other participants.

##### The ideal survey approach
Use enriched asking and Ecological Momentary Assessments: when airbnb users make decisions on the platform - as in the 2017 paper whether to accept a guest - pop up with a survey asking them directly whether race played a role in this decision. This can be gamified using airbnb credits or reputation points to ensure participation.
If people were perfectly honest, we could discern whether race played a role in their decision.
However, fortunately or unfortunately as the case may be, people are not honest about this and the survey would not be revealing.

##### More realistic approach
Use the same approach but don't directly ask about whether race was a deciding factor. Use enriched asking in tandem with data from other studies: the digital trace data we have on users discrimination to discover what the proxy responses are for racial discrimination (e.g. 'concerned about cultural differences'). Then use the survey in the wider population interpreting the proxy responses as signs of racial discrimination.
