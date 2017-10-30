### MACS30000 Assignment 3
### Wikipedia and and its impact on Science Communication (Experimental Study Proposal)
#### Leoson Hoay
#### October 30, 2017


## Contents
* [Introduction and Research Question](#introduction)
* [Computationally-Enhanced Experiment](#experiment)
* [Validity and Heterogeneity of Treatment Effects](#validity)
* [Other Points of Evaluation](#evaluation)
* [Conclusion](#conclusion)
* [References](#references)



## <a name = "introduction"></a>Introduction and Research Question 

The Wikipedia article database is large and spans many disciplines, from the physical sciences to the social sciences and the humanities. It is as easy to find an article on Lin-Manuel Miranda's "Hamilton" as it is to find one describing the Hubble Deep Field. The surprising result of the study by Thompson and Hanley([1]) implicates Wikipedia in many areas where it was previously thought to only play a cursory role, and thus also provides a refreshed perspective on the value of content posted on Wikipedia in the field of science. My previously proposed studies([2])([3]) sought to examine the correlation between new Wikipedia content and science media content, as well as science media exposure at the level of the media consumers. In this study, an experimental method will be used to determine and estimate a causal model between new Wikipedia content and the two dependent variables of new science media content and consumer exposure to the content of interest.

While the correlations between these variables are already being examined in the previous iterations of the study, estimating a causal effect will create a stronger statement about the direction and value of the relationship between Wikipedia articles and science communication. In particular, this study wishes to establish that the observed effect in the two dependent variables can be attributed in a unique manner to an increase in related Wikipedia content. The two hypotheses of primary interest are:

1) An increase in the number of new articles in a particular subfield of science on Wikipedia will result in an increase in occurrence of science media content within the similar field.

2) An increase in the number of new articles in a particular subfield of science on Wikipedia will result in an increase in science media consumers' exposure to media content within the similar field.


## <a name = "experiment"></a>Computationally-Enhanced Experiment

The method to be employed in the experiment follows a traditional pre-post treatment-control paradigm, but as inspired by the Thompson and Hanley study, the treatment and control groups will be based on newly generated articles for Wikipedia describing novel topics in a particular subfield, where the treatment group of articles will be uploaded to Wikipedia, and the control group withheld from submission. There are four general steps to execute this experiment from start to end:

- Gather novel articles for Wikipedia created by recruited assistants
- Computationally randomize treatment and control by first establishing strata via document analysis, and then randomizing within the stratified blocks (to be elaborated on below)
- Upload treatment articles to Wikipedia, and withhold control articles
- Perform analysis of treatment effect (article growth in science media outlets and exposure growth in science media consumers) based on a determined pre-post window

First - with an assumed level of funding - a convenience sample of academics, researchers, and graduate students will be recruited to assist with the creation of Wikipedia articles within a particular topic of science (for the purposes of this proposal, Biology will be chosen). This convenience sample will be obtained via available academic networks and resources at the point of conducting the study. The articles will obviously have to be novel (topics not already covered on Wikipedia), which is part of the reason why graduate-level and above assistants are chosen to write the articles, as most of these topics will have come from the relative forefront of science.

Second, in order to ensure an adequate level of homogeneity between treatment and control articles, document analysis will be performed on the articles and the results used to stratify them across two main characteristics, author and article type. The stratification by author is to control for differences in style, expertise, and article quality between different authors. The stratification by article type makes it so that the distribution of knowledge branches (e.g. plant anatomy, biological processes) and sub-topics will be equitable across the treatment and control groups. Within these strata, randomization using a random number generator will be used to assign half of the articles to the treatment and the rest to control. Document analysis will also reveal document characteristics such as number of words and number of references, which we can then use to check if our randomized groups are balanced across these as well.

Third, the treatment articles will be uploaded to Wikipedia for editing and publishing, while the control group articles will be withheld. In the study by Thompson and Hanley([1]), 43 articles were used in the total sample, which were enough to reveal a significant causal effect. Thus, in our study, we will aim to use as many, and more if they are available. If articles are rejected or require edits, the required adjustments will be made before being resubmitted.

Last but not least, analysis of the results will be observed both in effect size and using ordinary least squares. The dependent variables, as aforementioned, are the change in the number of science media articles that are similar in topic to the Biology articles posted, and the change in density of self-reported exposure to the related topics in Biology in science media. While the pre-post measurement window proposed in Thompson and Hanley includes 6 months before the articles are posted (pre-period), a 3 month delay, and then 6 months after the delay (post-period), I propose that this study extend the delay by another period of 3 months, given that in the hypothesized causal mechanism (Wikipedia article -> read by academics and science communicators -> new studies and articles in the media -> exposure) information will take a slightly longer time to trickle down the chain. Measuring the number of similar science media articles is straightforward. To measure consumer exposure, the survey that was employed in the previous assignment([3]) can be repurposed for this measurement.


## <a name = "validity"></a>Experimental Validity and Heterogeneity of Treatment Effects

The internal validity of the study should hold strongly - as most sources of variability other than the one of interest are being controlled for - unless some mechanism in the process (such as Wikipedia article publishing) does not function as expected (some articles get delayed for extraordinarily long times, or are not accessible due to a technical issue). Variability arising from article disparateness is being controlled for by the randomization of treatment and control groups across strata, and also through limiting the topic range of the articles and the measurement samples. However, the latter might conversely limit the external validity of this study.

How generalizable are the results? They are probably as generalizable as the boundaries imposed by the data of interest and the measurement sample. In this study, only one field of science is being sampled - Biology - and hence the effects may not generalize across different science fields. Moreover, this also prevents the study from comparing and taking into account any differences arising from meta-science characteristics of a particular field (for example, Biology may be a more popular field in science media as compared to Mathematics, and such articles may be marketed better to audiences as well). The sampling of the survey population also limits the external validity of the study to that of already-regular consumers of science media, and does not take into account other types of individuals. However, it can be argued that this is the main population of interest.

The treatment effect is generally not threatened by heterogeneity, given that the science news articles and consumer self-reports are analyzed and treated as aggregates. However, there are some possible sources of error which may slightly bias the results. The first is that it is difficult to control for editor behavior and response towards the submitted articles - the control group of articles would not go through the Wikipedia editing process. To manage this, one could possibly measure the articles as-is at the point of upload while ignoring edited content, or with enough resources, recruit a sample of editors to operate on the unsubmitted articles as well. There may also be error arising from the survey measurements due to data gaps and non-responses, but they should be managed in the same manner as in the survey study proposal([3]), through incentivization and post-hoc adjustments.   


## <a name = "evaluation"></a>Other Points of Evaluation

The experimental method here boasts a couple of advantages over the two observational methods previous proposed for this research topic. First and foremost, it allows for the estimation of a causal relationship between the variables, that was not possible before without controlling for extraneous factors. In the observational studies, a third variable problem is apparent - new science could be generating new Wikipedia articles, while also creating media buzz and generating new science media articles about the same topic. In this experiment, through manipulating the treatment effect of article uploads and including a control group, the direction and causality of the effect can be established (or debunked).

Secondly, it affords greater control over the types of data that we want to include in our measurements, as we now directly control the independent variable input. Hence, there is little or no risk of noise arising from the side of new Wikipedia articles, which may or may not have been a problem in the observational studies where Wikipedia articles were taken and measured as they are created and edited by the Wikipedia community at-large.


## <a name = "conclusion"></a>Conclusion 
In closing, the proposed study attempts to make a statement about the causal effect of Wikipedia content on science communication, much like past studies that have established a similar effect on schoolwork and on academia. The power of the experiment is such that it allows for one to estimate a causal model given the variables in question, but in doing so may risk limiting the context to which the findings can be generalized. Even so, modern technologies may render experiments more accessible and easy to conduct digitally, which can lead to easier replication and verification of study findings. But even if the results of this single experiment may not necessarily be generalizable to other settings where Wikipedia should also have an impact, this study will add to the growing body of literature that seeks to examine and unravel the potential and role of Wikipedia in the knowledge society.


## <a name = "references"></a>References 

- Biddix, J.P., Chung, C.J., & Park H.W. (2011). Convenience or credibility? A study of college student online research behaviors. Internet and Higher Education, 14, 175-182.
- Thompson, N.C., Hanley, D. (2017). Science is shaped by wikipedia: Evidence from a randomized controlled trial. MIT Sloan School of Management Working Paper 5238-17.


[1]: http://www.nature.com/news/wikipedia-shapes-language-in-science-papers-1.22656
[2]: Assignment_1.md
[3]: Assignment_2.md



