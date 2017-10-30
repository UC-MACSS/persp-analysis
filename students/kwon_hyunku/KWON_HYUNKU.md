Preaching to the Choir: Partisanship, Political Echo Chambers, and the Diffusion of Fake News
---------------------------------------------------------------------------------------------

Hyunku Kwon
-----------

Introduction
------------

The unexpected election of Donald Trump has garnered scholarly and
popular attention, for his populist claims which demonstrated his
ability to tap into the underlying, latent demands of mass public. In
explaining this phenomenon, some authors focused on the uncommon
proliferation and success of Fake News. Such prevalence of Fake News
notwithstanding, the causal mechanism behind the **diffusion** of fake
news is still not clear: who reproduces and circulates the Fake News?

Fake News is usually made up of incomplete, one-sided, and provocative
information, circulation of which indicates a biased, stereotyped, and
dogmatic cognitive process. Thus, we can theoretically draw on political
behavior literature to understand the mechanism behind the diffusion of
Fake News. Some authors point to partisanship as the culprit behind
cognitive bias. Partisanship is not a mere political affiliation: it is
a framework upon which individuals make sense of the political and
social world; a way of dividing the world into us-and-them; a social
identity, which binds individuals with others. Others have focused on
the impact of network on development of political beliefs, deliberation,
and cognitive process (Mutz 2002; Klar 2013). Once individuals’
political networks are comprised of homogeneous, cohesive networks, then
they develop similar, somewhat dogmatic belief system, while
cross-cutting, heterogeneous networks engender more sophisticated,
complex, and hesitant political attitudes.

Drawing on such theoretical insights, this research examines the
conditions upon which individuals disseminate Fake News. In particular,
**do partisan identity and network structure influence the diffusion of
Fake News?**

Against this background, this article conducts a digital experiment to
understand the causal mechanism behind the diffusion of Fake
News???digital in the sense that I recruit, randomize, deliver
treatments, and measure outcomes by using digital infrastructure. Via
experiment methods, this research examines the impact of partisan
identity of interactant and network structure on the diffusion of Fake
News. I collect a sample of Twitter users who follow either Republican
or Democratic Twitter account, assuming that following a partisan
account indicates their partisan identity. I construct Republican,
Neutral, and Democrat accounts (“bots”), tweet at the subjects via those
“bots” to deliver them a piece of Fake News, and, after 24 hours, tweet
them a counterargument that the Fake News is actually a faux. By varying
the political identities of the “bots”, this experiment shows how the
partisan identities of the interactant influence the diffusion of Fake
News; by taking into account the impact of network structure in this
process, this experiment shows the heterogenous effect of treatment on
the subjects???that political echo chambers increase the likelihood of
diffusion of Fake News.

This digital, randomized field experiment provides better analysis of
the mechanism at issue: unlike lab-experiment, the naturalistic nature
of this experiment provides more realistic results; unlike observational
studies, this study creates various treatments.

Experiment Design
-----------------

### Recruitment and Randomization: Using the streamR package in R, I randomly select 2,000 Twitter users who follows either Republican party or Democratic party (1,000 Republican users and 1,000 Democrat users). I only selected Twitter users (1) whose accounts were at least 6 months old, and (2) who regularly tweets more than 10 times a week.

### Treatments: this part is comprised of two stages. (1) The “bots” deliver Fake News (2) After 24 hours of the first treatment, the “bots” notify that the Fake News is a faux, by sending the subjects an article which debunks the credibility of the Fake News. In this process, I varied the political identity of the bots, resulting in a 3 (Republican, Neutral, Democrat) x 3 (Republican, Neutral, Democrat) experimental design. To approximate the treatment to the “real life” experience in Twitter, each bot follows typical characteristics of Republican, Democrat, and Neutral accounts. For example, the Republican bot follows Republican account, Christian account, Trump, or conservative pundits as Ben Shapiro; Democrat bot follows Democrat account, Hilary, or liberal pundits such as Paul Krugman; Neutral bot follows random, neutral accounts such as Kendrick Lamar, meme pages, or Uchicago account. The number of followers of each bot should be similar, to control for the impact of popularity on the process.

the Fake News contains malicious, provocative information about the
opposing party, and thus the content of the treatment varies from the
partisan identities of the users: to Republicans, the Fake News is
mainly constructed around the allegation that Stephen Paddock is a
Democrat, Hilary voter; to Democrats, the Fake News is mainly
constructed around the allegation that Stephen Paddock is a Republican,
Trump voter. The correction article argues that Paddock has no political
affiliation with either party or either candidates.

### Measure outcomes: Using streamR package in R, scrap tweet history and see whether one retweeted, or mentioned the Fake News. This research uses **dictionary methods** to measure the number of tweets that mention the Fake News: to Republicans, “Paddock”, “Democrat”, “Hilary” are the keywords; to Democrats, “Paddock”, “Republican”, “Trump” are the keywords. When the word “Paddock” appears with “Republican” or “Trump” (to Democrats), or with “Democrat” or “Hilary” (to Republicans) in tweets, then we count it as one. However, if some keywords such “Fake” appear with those tweets, I personally read the tweet and decide whether such tweets are circulation of the Fake News or not.

Analysis 1. Partisanship and the Diffusion of Fake News
-------------------------------------------------------

We first examine the relationship between partisan identity of
interactant and the diffusion of Fake News. Political behavior
literature suggests that individuals show more trusting tendency towards
copartisans. Thus, partisans who receive information from copartisans
would be more likely to believe the given information. On the other
hand, partisans who receive information from bipartisan would be less
likely to believe the given information.

Drawing on such theoretical insights, this research assumes that the
partisan bias happens at both stages of the experiment???receiving the
Fake News itself, and the correction of the Fake News. Thus, (1)
partisans would be more likely to believe and circulate the Fake News if
it was delivered by copartisan. Also, (2) partisans would be more likely
to believe and circulate the Fake News if it is corrected by bipartisan.
If bipartisan-user corrects and debunks the Fake News, then it would
make partisan users more protective about the Fake News; if copartisans
deliver the counter argument, partisan users might actually accept the
counter argument and choose not to circulate the Fake News.

### Hypothesis 1.1 users who receive the **Fake News** from **copartisan** would be more likely to disseminate the Fake News (copartisan &gt; neutral &gt; bipartisan)

### Hypothesis 1.2 users who receive the **counter argument** from **bipartisan** would be more likely to disseminate the Fake News (bipartisan &gt; neutral &gt; copartisan)

Analysis 2. Network structure and the Diffusion of Fake News
------------------------------------------------------------

“The same treatment can have different effects on different kinds of
people” (Salganik 2017). I expected to find heterogenous treatment
effects in the degree of network structure: individuals with homogeneous
network structure would be more likely to believe and circulate the Fake
News, in all nine (3x3) groups. In other words, if individuals are
surrounded by **echo chambers**, they are more likely to develop
righteous mentality, falling easy prey to Fake News.

To empirically investigate the relationship between network structure
and the diffusion of Fake News, we need a measure of homogeneity of
political networks: the number of ties directed to users who share
political orientation, divided by the total number of ties. This index
ranges from 0 to 1. Using OLS regression where the dependent variable is
the tweets that contain the information about the Fake News, this
research traces the impact of network structure on the diffusion of Fake
News.

### Hypothesis 2. The degree to which one’s political networks are homogeneous is positively related with the diffusion of Fake News.

Challenges

There are some pitfalls inherent in this approach. First of all, (1)
construct validity: this research counts the diffusion of Fake News via
dictionary methods, which might fail to correctly count the political
behavior at hand. For example, some authors may have paraphrased the
exact words, and some others might have used the combination of words
(such as “Paddock” and “Hilary”) for other reasons. In this case, we may
deploy Automated Text Analysis methods, which enables classification of
“texts into a set of categories” (Grimmer 2013), with “minimiz\[ing\]
the amount of labor needed to classify documents.” to detect the
political behavior at hand. Researchers might read the tweets that
disseminate Fake News, elicit key terms, and then deductively find
additional terms related to the key terms. Drawing on this method, we
can better detect the reproduction of Fake News.

Also, the generalizability of the results might be controversial:
whether the results can be generalized within Twitter, and whether the
results can be generalized to real-world. Though such issue of (2)
external validity is very hard to address from the methodological
perspective, similar works which examine the same theoretical issues
with lab-experiment or survey methods have been published (Mutz 2002;
Klar 2014), from which we can theoretically extend the insights of this
research.

There are some (3) ethical problems, for the experiment itself delivers
Fake News, the process of which might lead to unexpected, detrimental
consequences. However, this experiment also corrects the Fake News in 24
hours, and, recruits limited users, both of which would ameliorate the
ethical problems. Also, since this experiment does not directly deal
with human object, relaxation of ethical standards is expected.
