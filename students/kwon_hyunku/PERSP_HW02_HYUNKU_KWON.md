### Intro

The unexpected election of Donald Trump has garnered scholarly and
popular attention, for his populist claims which demonstrated his
ability to tap into the underlying, latent demands of mass public. What
made this election more interesting was that most of the pundits and
scholars have failed to predict the results, though drawing on various
scientific methods of polling. Such fiasco implies that the conventional
public opinion polling, which draws solely on survey methods, is not
successfully capturing the recently changing political landscape in the
U.S.

Meanwhile, some scholars have developed ingenious methods to trace such
ongoing transformation of American political reality, political
polarization in particular. Combining surveys with Big Data analysis,
this line of approach successfully shows how partisans develop
internally homogeneous, and externally heterogeneous cultural and
network patterns, uncovering the cultural and social foundations of
partisan polarization via observational data such as patterns of online
book co-purchase (Della Posta et al 2015; Shi, Yongren et al 2017; Shi,
Feng et al 2017). Seen this way, some characteristics of Big Data, such
as ‘big’ and ‘always-on’, enables us to better capture the dynamics of
the latent mechanisms underlying American electorate than traditional
polling methods.

Building on such methodological breakthrough, this project investigates
the elusive Trump voters by combining computational and survey methods.
This project focuses on Facebook users. Scholars have shown that
patterns of Facebook Likes are related with various latent
psychological, cultural, and social characteristics (Kosinski et al
2013). Combining Survey Methods with observational data (Facebook
Likes), we can better understand the underlying, latent characteristics
of Trump voters that are not susceptible to easy demonstration via
conventional survey methods.

This research project is comprised of two parts: first, this article
looks at the patterns of Facebook Likes in the American voters. The
first part is comprised of both macro-and micro-analysis: In the macro
level, I divide the Facebook users into Trump voters and non-Trump
voters, and investigate the patterns of Facebook Likes in each group.
This macro analysis shows how Trump and non-Trump voters develop
systematically divergent patterns of Facebook Likes. In the micro level,
this article conducts logistic regression to examine the impact of
Facebook Likes on Trump voting.

The second part of this project considers the potential pitfalls
inherent in this approach: Facebook users are not directly
representative of the American voters. Taking into account such
structural problem immanent in Big Data analysis, we test the external
validity of this approach. Using Multilevel Regression and
Poststratification (MRP), this article estimates voting behavior from
both Facebook Dataset and American National Election Studies 2016,
compares these two models, and tests which of the two models better
predicts the actual results.

### Research Design

### Part 1. Investigating the Like Patterns of Trump voters

What is the driving force behind the heated, confrontational, and
unpredictable political landscape in the election 2016? Whether such
polarization stems from political cleavages (Abramowitz and Saunders
2008; Fiorina et al 2009), culture (Hunter 1991; Della Posta et al
2015), or psychological factors (Hetherington and Weiler 2009) has been
discussed in recent years. By combining the observational data (which
reveal the latent characteristics of the mass public) and survey data
(which reveal manifest characteristics such as viewpoints and
demography), this project provides methodological framework upon which
the recent changes in American political reality can be better
explained.

This research project randomly selects participants among Facebook Users
who voted in the election 2016, trace the patterns of how they “like”
Facebook pages, and conduct a survey. I copy American Nation Election
Studies (ANES) questionnaire for two reasons: first, as question form
and wording affect the participants’ responses (Schuldt et al 2011),
copying a well-acclaimed, tested, and credible survey questionnaire
would help us avoid distortions originating from questionnaire design.
Second, using ANES’s questionnaire, we can compare the responses with
ANES and test the external validity of this research. However,
considering the lengthy, complicated nature of ANES questionnaire, I
would only select some indices that are pertinent to my research
interest—such as demographic factors (e.g. race, age, gender, income,
education level, religion, or region), political and social identities
(e.g. partisanship and ideological identification), political viewpoints
(e.g. government intervention, international politics or abortion), and
voting behavior. This selection process would facilitate the research,
lowering the cost of survey and reducing Non-responses. Those selected
indices are used not only to analyze the mechanisms of voting behavior,
but also to conduct Multiple Regression and Poststratification.

Keeping this background in mind, I first take on macro analysis, by
dividing the population into Trump voters and non-Trump voters, and
looking at the patterns of Facebook page Likes of each group. Two
methods can be used: first, we can simply measure the correlation
between ‘Liking a Facebook page’ and voting behavior; second, within
each cluster (Trump voters and non-Trump voters), we can investigate the
constellations of Facebook Likes, by drawing on Network Analysis.
Understanding each Facebook pages as ‘nodes’ and the associations
between Pages as ‘ties’, we can succinctly describe the relational
properties of Facebook Likes, and understand the central-periphery
structure of Facebook Likes (Boutyline and Vaisey 2017).

Building on the macro analysis, I then investigate the impact of
structure of Facebook Likes on voting behavior, controlling for
demographic, political, and social characteristics. To this end, this
article uses Logistic regression modeling. This regression modeling
includes variables such as patterns of Facebook Likes, demographic
factors (including age, gender, income, education, religion, or region),
political and social identities (including partisan, ideological, Tea
Party, or Evangelical identification), and political viewpoints
(including government intervention, international politics, private
insurance, or abortion). The dependent variable is a dichotomous
variable coded either 1 (voted for Trump) or 0 (voted otherwise). This
regression model would uncover the mechanisms behind Trump voting,
taking into account both manifest and latent characteristics.

Gauging the impact of patterns of Facebook Likes on Trump voting
requires a measurement of structure of Facebook Likes. If one’s
composition of Facebook Likes is more comprised of Trump-leaning pages,
then one’s likelihood of supporting for Trump would increase. Thus, I
measure the degree of Trump-leaning structure of Facebook Likes as
follows: The number of Likes on pages that are statistically correlated
with Trump voting/The total number of Likes on page.

### Methodological Limits of Facebook Data

This approach has some methodological pitfalls. First, a substantial
segment of Trump voters regrets their decision and withdraws their
original choice. Considering the rising unpopularity of Trump,
dissatisfied ex-Trump voters might have modified their patterns of
Facebook Likes. Such changes of big data systems, or, “drift”, might
undermine the validity of this analysis. To ameliorate this problem,
this project should limit the scope of the research and trace the
patterns of Facebook Likes up to the election of Donald Trump, excluding
the modifications of Facebook Likes after the election of Trump. Since
the purpose of this project is to uncover the Facebook Like patterns
which facilitated the support for Trump, the excluding modifications of
Facebook Likes after his election would better shed light on the exact
mechanism behind Trump voting.

However, there is a more fundamental problem inherent in the Facebook
Data: non-representativeness. While understanding the systematic
difference between Trump and non-Trump voters requires us to target
American voter in general, the frame population (the population on the
sampling frame) in this research is Facebook users; and such discrepancy
between the target population and frame population would cause
methodological problems such as coverage error. Thus, instead of merely
assuming the validity of my approach, this research tests whether the
Data and modeling drawn from Facebook are valid.

### Part 2. External Validity

In this section, I test the external validity of the model against two
standards: First, I compare the results from those of the other Dataset,
ANES; second, I test whether which of the two models better predict
electoral results. I draw on MRP (Multilevel Regression and
Poststratification) to take on this task.

MRP is a method deployed to undo the distortion originating from the
sampling process, by assigning weights to each person lying in the
intersections of various categories. Following Wang et al (2015), this
article would “partition the data into thousands of demographic cells,
estimate voter intent at the cell level using a multilevel regression
model, and finally aggregate the cell-level estimates in accordance with
the target population’s demographic composition.” Since our
questionnaire copies that of American National Election Studies, we can
elicit two MRP-adjusted estimates (one from Facebook Data, the other
from ANES) with exactly same methods and parameters. Comparing each
estimate, we can look at whether each estimate is similar with another,
and whether which model better predicts the electoral reality.
