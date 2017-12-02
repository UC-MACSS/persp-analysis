# Assignment 1: Proposing an observational study

## Laurence Warner

### General Research Question
Which venues in Chicago are most associated with extreme binge drinking?

### Topic of interest
The [CDC](https://www.cdc.gov/alcohol/fact-sheets/binge-drinking.htm) describes binge drinking as "the most common, costly, and deadly pattern of excessive alcohol use in the United States." They also describe it as a "preventable" public health problem. One idea is "Dram Shop Liability" which "refers to laws that hold alcohol retail establishments liable for injuries or harms caused by illegal service to intoxicated or underage customers."

Underlying this concept is the more general principle that alcohol vendors should regulate their sales to highly inebriated people.

The problem is that this is not in the economic interest of the vendors. They make sales by serving such customers and often don't incur the costs, which are incurred by the customer as well as other individuals who they interact with and the public health system more generally.

##### Self-reporting

If we want to investigate which venues are serving extremely drunk people, it will be very difficult to research using traditional methods. Obviously, it is not in the interest of offending establishments to report on this accurately. How about asking the consumers? As discussed by the [National Institute on Alcohol Abuse and Alcoholism](https://pubs.niaaa.nih.gov/publications/assessingalcohol/measures.htm) self-reporting data on alcohol consumption by consumers is unreliable for this purpose. Alcohol consumption tends to be under-reported in surveys. Firstly, heavy drinkers under-participate, and secondly, due to the nature of the problem, respondents often forget information (think "Which bar was it we had the 5 tequila slammers at??"). Thirdly, I believe that many people would deny that they were too drunk even if they in fact were, due to social desirability of "handling your liqor". In addition, even in clinic populations which answer accurately in general, people don't respond accurately to specific questions like "did you get drunk last night?". This implies that they would also not respond accurately to "where did you get drunk last night?".

Hence, an alternative approach is necessary to identify the offending venues.

### Specific Research Question

Which start locations for Uber rides are most associated with cleaning fees in Chicago?

##### Discussion

One possible side-effect of binge drinking is vomiting. This may occur in a vehicle on the way home from a drinking establishment. In the specific case of Uber, which is heavily used by party-goers - who are too drunk to drive, and often go out at times not served by public transport - drivers are able to claim compensation from Uber when a passenger vomits in their car, and passengers may be charged a cleaning fee. As the amusing [case](https://www.aol.com/article/finance/2017/07/21/why-one-uber-driver-loves-picking-up-puking-passengers/23041254/) of Uber driver Curtis Preston shows, this is not an uncommon occurrence if drivers operate late-night in party districts.

I hope to utilize these Uber cleaning fees as a signal of unobservable activity: namely vomiting due to binge drinking.

### Research design

Within Salganik's framework, my research will use the method of Counting.

##### Data source

Uber have recently made moves towards more open sharing of their vast wealth of data on rides, with the launch of [Uber Movement](https://movement.uber.com/cities?lang=en-US) in 2017, with the stated aim "to help urban planners make informed decisions about our cities". Initially, this was only shared with urban planning groups, but this summer was made freely available to the public. Currently it only covers six cities - Bogota, Boston, Johannesburg & Pretoria, Manilla, Sydney and DC - although Uber soon hopes to extend this to every city in which they operate.

However, this public data only includes the following three variables for rides: start location, end location and journey time.

My strategy to get hold of data on cleaning fees - i.e. was a cleaning fee claimed by the driver in each given ride- would be as follows. In the same way that urban planning groups got hold of the Movement data initially, I would seek to work with an interested third party to encourage Uber to share information on this variable with us to conduct this research to better understand extreme binge drinking in cities with the aim of targeting prevention at suspect locations. Such organizations could include public health organizations - such as the National Institute on Alcohol Abuse and Alcoholism - or more localized urban groups such as U Chicago Urban Labs's Health Lab.

##### Data analysis

The most basic analysis would be as follows. Simply count the % of rides involving cleaning fees at each possible start location for Uber rides. Describe this amount as a location's "Puke Index". This index is approximate and only useful for relative comparisons.

Location can be defined with differing degrees of precision. If we defined location broadly at street or neighborhood level, the information would be probably not be very enlightening: it might tell us that Rush & Division rides end with more puke than leafy Hyde Park. Where this analysis has its power is in the precision of Uber location data - we can define location as specific addresses. The default setting in Uber is to call the ride on the street outside the venue from which people are calling. Although there will be some statistical noise (e.g. adjacent and opposite addresses), we hope to be able to identify specific hotspot addresses.

This counted data could be useful in itself. It could act as a first step to identifying venues with the highest Puke Index. Also, geospatial visualizations could begin to display interesting patterns.

##### Ideas for extensions

* Analyze end locations to explore destinations of binge drinkers

* Underage drinking could be considered. Either through considering age data, or looking at end locations such as college campuses

* Extend to other ride sharing apps, such as Lyft. Uber was chosen due to Uber Movement

* Extend to other cities

### Critical analysis of research proposal

##### Comparison to alternative observational methods

There is no sense in which this situation approximates a natural experiment. In addition, we cannot match users other than their start location.

Forecasting is not particularly relevant - we are more interested in broad patterns rather than changes over time.

Down the line, efforts could be made to try to use cleaning fees to accurately measure alcohol abuse. I admit that cleaning fees are a blunt instrument for measuring binge drinking - clearly there are other possible causes for vomiting: notably sickness. A more refined study could probably develop statistical tools for estimating the % of clean ups which are alcohol related based on variables including time of day, season etc.

However, in this study, we are mainly interested in comparing relative vomit rates between locations rather than trying to infer absolute rates. We implicitly assume that a constant proportion of cleaning fees are alcohol related. This is particularly valid if we restrict attention to party hotspots on Friday and Saturday nights, when I would wager this proportion is very high.

##### Comparison to alternative data sources

One could argue that we could just analyze alcohol purchases/sales at different venues. However, this merely gives us aggregate information. It does not tell us specifically about the propensity of such venues to serve this alcohol to highly inebriated (at risk of vomiting) individuals.

Why not simply physically survey the streets outside venues for vomit? Firstly, good luck finding willing researchers. Secondly, it is difficult to quantify (I won't go into gory details!).

##### Good characteristics of big data (in decreasing order of importance)

* Non-reactive

Cleaning fees objectively reveal behavior (drunk vomiting) that would not otherwise be observable (see 'self-reporting').

* Big

Vomiting in Ubers is a rare event (we hope). However, due to the sheer volume of Uber rides (more than 200,000 per day in one city (San Francisco)) we hope to pick up enough cases to create statistically significant variation between locations.

* Always-on

Uber record cleaning fee claims automatically, so we do not have to go to any extra effort to gather this data.

##### Bad characteristics (in decreasing order of negativity)

* Inaccessible

Data on cleaning fees is currently privately held by Uber.

As discussed, I would hope to overcome this through a partnership with a third party and Uber to get hold of the data.

* Incomplete

We miss data on binge drinking from people who do not subsequently travel (i.e. at, or near, home), so we will underestimate binge drinking.

However, as discussed, our study is not interested in accurately measuring vomit rates, but rather at comparing relative rates between locations, so this is not a major problem.

* Non-representative

The population of the study is Uber users, whereas the population of interest is all binge drinkers. Firstly, Uber users may not be representative. For example, being richer than average, they may frequent 'nicer' bars, thus overestimating their Puke Index compared to, say, dive bars.

However, Uber is remarkably widespread (see 'Big'). Thus, our population is probably more representative than a traditional study which under-surveys problem drinkers.

* Drift

Uber's policy on cleaning fees [has](https://www.aol.com/article/finance/2017/07/21/why-one-uber-driver-loves-picking-up-puking-passengers/23041254/) changed over time. Specifically, the cleaning fees have decreased over time. This may have led to changes in the propensity of drivers to claim cleaning fees. Such changes may occur going forward.

As discussed, we are interested in relative Puke Index between locations rather than measuring absolute rates of binge drinking, so this is not a major problem.

* Algorithmically confounded

Given their popularity, party hotspots are particularly prone to surge pricing. This may lead us to underestimate the Puke Index from vomit hotspots.

The highly drunk are probably not particularly price sensitive, so this is a minor concern.

### Conclusion

This research proposal represents a use of big data in an original way. It is surprising that ride sharing data could reveal information about such a topic as binge drinking. If it were possible to get hold of this data, it could be very revealing about behavior that is considered impolite to discuss and is generally unobservable to researchers. The Puke Index would probably generate amusement and interest from most, and discomfort for the implicated venues.
