---
title: "Proposing an Experiment"
output: pdf_document
---

By: Bethany Bailey

# Research Question
The rate of savings in the US is extremely low. A 2016 [survey](https://www.gobankingrates.com/saving-money/data-americans-savings/) found that one-third of Americans had no money in their savings accounts, and 69% had less that $1,000. I propose conducting research to measure the effects of normative messaging on individual savings levels among different population segments. Specifically, I wonder how three treatments - (1) providing tips on how to save, (2) providing a comparison to one's peers, and (3) providing a comparison to a suggested target savings - might change the level of savings in the population. Further, I ask how these treatments differ in their effects on individuals with different ages, net worth, and pre-treatment savings ratios. In asking this question, I hope to shed light on the most effective means of getting people to save. Much like the Schultz et al. (2007) and Allcott (2011, 2015) energy experiments, I predict that the treatment will on average cause people to save more, and there may be a boomerang effect that causes people who are already saving more than their peers to slow their savings.

# Research Plan
This research design will utilize computational methods at each step of the process, allowing for nearly zero variable cost and easy scalability. Below, I outline the details of this research method.

## *Recruitment*
The research will be conducted on the population of individuals who have checking and savings accounts at one of the [five largest US banks by assets](https://www.relbanks.com/top-us-banks/assets) and utilize online or mobile banking (for a discussion on this selection and how it effects validity, please see the "Validity" section). To find participants, I would contact the banks and request partnerships. Banks have an interest in understanding how to create higher savings among their customers, so this research would be mutually beneficial. Thus, as long as no personally identifying information about participants is released to the researchers, I believe the banks would be willing to participate. In order to effectively and easily measure treatment effects, the pool of participants would be chosen from individuals who have both checking and savings at the same institution. These participants would be chosen utilizing anonymized digital bank records. This selection would yield millions of potential participants, allowing me to randomize treatment among many different subgroups.

## *Randomization*

Among the participants, groups would be broken out based on savings-to-checking-ratio (SCR), wealth/net worth (as measured by the combined value of savings and checking), and age. Proposed breakouts for age groups are below. In order to determine appropriate breakouts for the SCR and net worth, I would collect aggregate digital data from the banks, calculate the variation in the population, and create the groups using this information (such as average, below-average, and above-average SCR).

Age groups:

  1. 18-35 year olds
  2. 35-49 year olds
  3. 50-64 year olds
  4. 65 and above

Among each subgroup, participants would be assigned to different groups in a full factorial design in order to study the separate and combined effects of each treatment. Each group would be the same size. The treatments would consist of (1) tips on how to effectively save, (2) a comparison to how much people are saving relative to their peers (people in the same age and wealth categories), and (3) a comparison to a recommended savings amount (target savings):

  1. Control
  2. Tips
  3. Peer Comparison
  4. Target Comparison
  5. Tips + Peer Comparison
  6. Tips + Target Comparison
  7. Peer Comparison + Target Comparison
  8. Tips + Peer Comparison + Target Comparison

## *Treatment Delivery*

The treatment would be delivered via a pop-up message the first time each individual logged onto their accounts on mobile or online banking over a one week period. In order to standardize the effect, each individual would receive the treatment only once. Individuals who do not log in over the one week period would not be included in the research. Though this would skew the sample, the previous randomization step would ensure that equal groups of people in the control and treatment group would log in; thus, the comparisons among different groups would still be viable. However, this might mean that any effects from the study could be muted or overblown, and further research could be done using other mechanisms (e.g. statements or letters mailed to individuals with social messaging, emails from banks, etc.) to study effectiveness of different means of communication.

## *Analysis/Measuring Outcomes*

In order to measure the treatment outcomes of this research, I would collect pre- and post-treatment data. First, I would measure pre-treatment savings contribution (the percentage of savings inflows in proportion to overall inflows, e.g. dollar amount added to savings per month divided by total inflows into checking and savings) for 6 months prior to study using anonymized digital bank data. After treatment was given, I would measure post-treatment savings contribution (using the same calculation method) for 1 month, 6 months, 1 year, and 2 years. I would compare each individual's pre- and post-treatment data to determine the percent change in savings. 

# Assessment of Experimental Design

## *Validity*

### *Internal Validity*

There are a few potential internal validity issues in this study: (1) measuring false treatments and (2) confounding variables. The research depends upon participants effectively receiving treatment by reading the pop-up when they sign onto online banking. However, many individuals might close the message before reading it. This might mute the effects of the experiment and threaten its internal validity. In order to attempt to counteract this, the pop-up will be brief and will include a checkbox that says "I understand" that each individual much check before closing. Additionally, further research using different types of messages (e.g. a direct mailing, email, or message on statements) could be done to increase the validity of this research.
Repeated trials of this experiment are could also help account for any unseen confounding variables. For example, if interest rates rise, the overall wealth of American families increases, or there is a bank savings promotion during the course of the experiment, this could cause a change in individual savings unrelated to the treatment.

### *Construct Validity*

This experimental method enhances construct validity because it allows the research to tailor its treatment messages to specific questions, such as whether social normative messaging is more effective than advice. However, there are multiple other constructs which may be flawed. For example, savings level could be difficult to compare across wealth groups, because higher income people might have more flexibility to save. Savings level could be skewed if inflows outweighed savings, there were no inflows, or there was a major change in inflows. However, this issue would remain no matter how savings level was operationalized, so a tradeoff needs to be made in order to easily measure the level among groups with different inflows. Further, by using a large sample, breaking the population into groups, and measuring savings level for 6 months prior to treatment, I would hope to minimize the potential adverse effects. 

Additional constructs with potential issues include savings-to-checking ratio and wealth. These measures don't account for savings accounts at other institutions, retirement savings, home ownership, or brokerage accounts. This potential sacrifice of construct validity is necessary to conduct the experiment without linking records from multiple institutions, which would cause anonymity issues. Further research into other forms of savings could be done to counteract this.

### *External Validity*
Potential threats to external validity include: (1) selection of the top five US banks by assets and (2) only measuring tech-savvy users. By using the biggest banks, the research might inadvertently study effects on a specific type of consumer (e.g. one who lives in big cities where the banks are prevalent). Additionally, selecting people with checking and savings at the same institution would leave out individuals without savings accounts or people who have savings and checking at different institutions. This research would only be done using US banks, so it may not be generalizable to other countries. In an effort to control the treatment, this research only reaches the population of tech-savvy users, which may skew it towards a younger population. 

However, because no population of banks or method of communication will produce a perfectly representative sample of the population, these issues will be present in any research. My methodology trades some external validity to create a low-cost study that would be easily scalable, and additional research should be conducted to address external validity concerns. Further, I hope to minimize these potential errors by using multiple banks, randomly assigning treatment, having a control group, dividing the research population into segments, and only giving treatment to half of each population segment in order to measure different effects.

## *Heterogeneity of Treatment Effects*
This research attempts to understand how the same treatment can have varying effects among different populations. Specifically, this research measures treatments among different age groups, SCRs, and lower and higher wealth. This is possible because the pool of participants is large and banks have the required data to accurately assign individuals to population groups. This research may reveal a boomerang effect in which messaging causes high SCR or wealthy individuals to save less, contextualizing the usefulness of such treatments. This study would fall short in that it would not look at injunctive messaging (such as the emoji in the Schultz et al. 2007 study). Further research could include a message conveying social approval/disapproval to study whether this has any effect on the boomerang effect.

## *Measuring Causal Mechanisms*
By using slightly different versions of the treatment in a full factorial design, I hope to understand the causal mechanisms behind changes in behavior. Using each combination of components would help determine which types of treatment, bundled or unbundled, cause target groups to change their behavior. I could determine whether social triggers, advice, suggested "good" behavior, or any combination thereof is most effective at causing target groups to save more. As previously stated, the ability to measure a causal mechanism might be threatened by confounding variables. I hope to minimize this issue by having a control group and different variations of treatment, which would allow me to shed light on interventions that can create healthy savings patterns. 

