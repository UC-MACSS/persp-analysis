    library(tidyverse)

    ## Loading tidyverse: ggplot2
    ## Loading tidyverse: tibble
    ## Loading tidyverse: tidyr
    ## Loading tidyverse: readr
    ## Loading tidyverse: purrr
    ## Loading tidyverse: dplyr

    ## Conflicts with tidy packages ----------------------------------------------

    ## filter(): dplyr, stats
    ## lag():    dplyr, stats

    library(stringr) 
    library(dplyr)
    library(readr)
    library(ggplot2)
    library(downloader)
    library(tidyr)
    library(broom)
    library(knitr)
    library(modelr)

    ## 
    ## Attaching package: 'modelr'

    ## The following object is masked from 'package:broom':
    ## 
    ##     bootstrap

Q1: Kaggle
----------

### Part I (Making an account)

My account can be found [here](https://www.kaggle.com/dangamarnik).

### Part II (exploring a competition)

One interesting competition I found was the DHS's Passenger Screening
Algorithm Challenge. Here the DHS is looking for an algorithm to reduce
false positives (or "false alarms") when detecting threats in airport
passengers using full body scanners. It was not made clear if it
included other scans such as luggage. It does this by giving out photos
of scans and marking which ones are a security violation and which ones
are not.

To participate, teams have to create an image recognition algorithm that
detects security violations in airport scans. Ostensibly, given the
task, the DHS would then use this algorithm on an out-of-sample series
of images and test whether it has a lower false positives. This is based
on two-step process which filters algorithms for their efficacy.

### Part III (exploring some data)

On Kaggle, one dataset I found interesting is the Global Terrorism
Database or GTD, which, like the name implies, measures terrorist
attacks from 1970 to 2016. I downloaded and explored some key aspects of
the data, namely terrorist attacks over time, what regions they occurred
in and what the targets were. While the trends do suggest an increase in
terrorism, it is worth noting that this is highly concentrated in the
Middle East and South Asia, followed distantly by Latin America.

Finally, the plurality of targets tended to be private property and
individuals followed by government targets such as the military and
police.

    # Getting the dataset and saving it as object.

    GTD <- read_csv("globalterrorismdb_0617dist_SMALL.csv") 

    ## Parsed with column specification:
    ## cols(
    ##   eventid = col_double(),
    ##   iyear = col_integer(),
    ##   region_txt = col_character(),
    ##   targtype1_txt = col_character()
    ## )

    # Graphing terrorist attacks over time.

    na.rm=FALSE
    ggplot(GTD, aes(iyear)) +
      geom_bar(fill = "red", color = "black") +
      theme_minimal() +
    labs(title = "Terrorist Attacks by Year", x = "Year", y = "Attacks") 

![](hw5_files/figure-markdown_strict/GTD%20data-1.png)

    # Graphing terrorist attacks by region.

    na.rm=FALSE
    ggplot(GTD, aes(region_txt)) +
      geom_bar(fill = "red", color = "black") +
      geom_rug() +
      scale_x_discrete() +
      coord_flip() +
      theme_minimal() +
    labs(title = "Terrorist Attacks by Region", x = "Attacks (1970-2016)", y = "Region") 

![](hw5_files/figure-markdown_strict/GTD%20data-2.png)

    # Graphing terrorist targets. 

    na.rm=FALSE
    ggplot(GTD, aes(targtype1_txt)) +
      geom_bar(fill = "red", color = "black") +
      geom_rug() +
      scale_x_discrete() +
      coord_flip() +
      theme_minimal() +
    labs(title = "Terrorist Attacks by Target", x = "Attacks (1970-2016)", y = "Target") 

![](hw5_files/figure-markdown_strict/GTD%20data-3.png)

Q2: Using collaboration to improve an article
---------------------------------------------

One paper in political science that could be improved is "[Using
machine-coded event data for the micro-level study of political
violence](http://journals.sagepub.com/doi/abs/10.1177/2053168014539924)."
The paper observes the accuracy of Global Database of Events, Language
and Tone (GDELT)-which captures mico-level political violence events
using machine learning text analysis. To do this, it compares several
years of the GDELT data to other "hand coded" datasets for the same
period. It finds that, while the two hand-coded datasets were highly
correlated and captured more data (such as location) the GDELT was less
correlated to them and had substantially less data captured. That is,
GDELT was significantly less accurate.

While this dealt with a smaller period that was coded by hand, in total,
GDELT has 200 million events going back from 1979 to 2015 that need to
be hand coded to be assessed how accurate it is. This makes it a perfect
candidate to use split-apply-combine methodology to code it by hand then
aggregate it back into a total dataset.

### How I would formulate it

A project with so many data points would be ideal as a human computation
project, or as
[Salganik](http://www.bitbybitbook.com/en/mass-collaboration/human-computation/)
describes, something that "take\[s\] a big problem; break\[s\] it into
simple pieces; send\[s\] them to many workers; and then aggregate the
results." Here, instead of using a smaller time period which people have
coded for, I would use human computation to code a large chunk of the
period and then use machine learning to do the rest. This would be like
the Galaxy Zoo project which coded a million galaxies through 100,000
volunteers and then used that coding as a training set to code a larger
cluster. Here I would similarly use 100,000 volunteers to code 3 million
political violence events (or around 30 events per person). Given that
less time is needed to code a singular event than to code the color of
galaxies, more things can be coded.

I would also use certain filters to try to correct for any systemic
biases among the volunteers such as comparing certain events to the ones
already coded in the other datasets. Ultimately, this would use a
split-apply-combine methodology, each event would be coded independently
but then aggregated back to the total dataset. Finally, like the Galaxy
Zoo, the 3 million coded observations would be used as training data for
machine learning that would fill in the 197 million remaining
observations.

To motivate participants I would frame this as an opportunity to learn
about political violence all over the world, and, given recent political
events, there might be a significant amount of people who would be
interested to do this. The training would be relatively short and easy
to not to strain people doing the work. Likewise, I would try to give
them "achievements" for how many events they coded to try to gamify the
project and have them do more observations.

### How this improves the study

This would help the original study in various ways. First, it would
cover the entire 1979 to 2015 period which can help with better
identifying the accuracy of the project. For instance, it could be that
accuracy dropped off within the period being observed and was relatively
accurate before then. And secondly, this would create a new and improved
version of the GDELT data which can help in this study but can also be
used in various other studies.

Q3: Flu Questions
-----------------

### Part I: Flu systems' Design, Cost and Errors

New methods of measuring the flu such as InfluenzaNet and Google Flu
have created alternative reporting systems to the traditional doctor
reports that are sent to the government. However, each system has its
own costs and benefits.

The first system is InfluenzaNet which is based on voluntary internet
surveys of thousands of people over a several month period (tracking the
same people.) It is designed to ask about flu like symptoms and makes it
optional to report on other home members symptoms (such as spouses and
children) and is used in about a dozen countries, beginning in 2003 in
Belgium and the Netherlands, and is done by each respective govenrnment.
According to Tilsten et al. 2010, it is often said to be "low-cost" and
"inexpensive" insofar as government spending is concerned but would be
incredibly expensive to do as a private researcher. Finally, the errors
related to it are based on the design and survey errors. For instance,
it is optional to track children which has underestimated certain flu
outbreaks and in the British case led to some response biases both in
over and underestimating the flu.

Second, is Google Flu which looks at google searches that are highly
related to flu outbreaks and counts these as indicators of influenza.
When it comes to costs, Google Flu has the lowest cost given the
cheapness of internet data and google searches (which are hosted and
covered by the company). The biggest issue comes with its errors, here
Google Flu was highly effective in the first season it was used but has
since become less accurate as the result of algorithmic drift and
overfitting in the original model. Finally, there are traditional
methods which are based on government reports of doctors and CDC
estimations of disease from government reports. These are somewhat less
costly (assuming governments and major organizations are doing them) but
have their own errors. As the case of the United Kingdom showed, changes
in access to doctors reduced patient visits which underestimated the
severity of the disease. Thus, the errors are based on how effective the
healthcare system of the country is.

#### Compairsons and Contrasts

Generally speaking, these are very different systems. The first relies
on internet surveys of patients, the second is based on Google searches
while the last is from doctor's reports. Likewise, there are huge
divergences in the cost of each system, while Google Flu costs very
little (since it is a system to analyze search results), the costs of
running an internet survey of thousands of people over several months
for around a decade are considerable for researchers (with surveys of
doctors reports perhaps being in the medium range).

However, there are interesting similarities in design and errors. Both
InfluenzaNet and traditional methods are essentially government-run
medical surveys, with the former tracking possible patients while the
latter tracks doctors. Likewise, there can be similar errors. For
instance, both the Google Flu and InfluenzaNet programs at certain
points overestimated flu prevalence (at least the latter in the UK).
This was for different reasons, Google Flu was skewed by algorithmic
drift since Google implemented similarity suggestions based on search
terms (like suggesting "flu" if someone searched for "cough"), while
InfluenzaNet in the UK had issues with response bias that in some cases
overestimated flu prevalence. Ultimately, all three methods have
trade-offs when it comes to using flu measurement.

### Part II: Errors if an outbreak occurs

In the event of an outbreak there could be all sorts of errors.
Beginning with the traditional system, one issue is how effective the
healthcare system already was when it came to reporting. For instance,
if there is a situation like in the UK where reaching a doctor becomes
difficult, than doctors' reports will underestimate flu prevalence since
not enough people are going to see them. However, this is likely to be
the case anyway since not everyone who gets sick with the flu goes to
see the doctor if they recover, lowering estimation already.

When it comes to InfluenzaNet, there are certain ways that it can both
over and underestimate a flu outbreak. First, because it covers adults
and reporting for children and spouses is optional, it could
underestimate the disease if it hits children. For instance, in Spain, a
flu outbreak mostly affected children but because they are optional to
report on, the data barely captured it. In other cases, such as a health
scare, it is possible that people might over-report their symptoms
resulting in an overestimation of how many people have the flu.

Finally, Google Flu would likely overestimate the reports of flu for
many reasons. First, because of Google's algorithms it might recommend
search suggestions that are similar to the ones Google Flu uses to
estimate how many people have the flu. Secondly, because the original
models overfitted on certain search terms that were highly spurious (for
instance related to March Madness since it coincides with flu season),
those might not be used as often, or used in different contexts in
different times of the year when flu season is not occurring, to be
useful now. Finally, because of the possibility of a health scare, many
more people than usual might search for that particular flu and it might
reduce the accuracy in finding out who has it.
