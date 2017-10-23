# Perspectives Assignment 2: Proposing a survey study

## Laurence Warner

### General Research question

Which Chicago venues are most associated with extreme binge drinking?

I have decided to use the same research question from my [observational study paper](https://github.com/UC-MACSS/persp-analysis/blob/master/students/warner_laurence/Assignment_1.md). For discussion of topic of interest, and why traditional survey methods are ineffective, please see that paper.

To summarize: using a traditional survey would be ineffective. People understate binge drinking. It would be costly to obtain the data too, as people would not volunteer this information.
### Specific Research question

Which Chicago venues are attended by young males who are considered most likely to have engaged in binge drinking?

### Survey description

##### "Beer King"

I propose to create a Facebook app called "Beer King". I will describe this app through a typical example.

Consider a young male Facebook user Adam. Adam has today been tagged in a post (photo, check-in) with a friend Brian and the location ZeBar (a hip Franco-African themed nightspot, zebra print sofas). In addition, a few days previously he was tagged with another friend Charlie, with a location tag at Your local (a more down-to-earth place, baseball on TV, PBR on tap).

A post pops up on Adam's timeline: Are you the Beer King of your friends? Take this quiz to find out if you reign supreme across the drinking land. One lucky Beer King wins a free pint at Buffalo Wild Wings for him and all of his subjects who take the quiz!
David and 6 other Friends say that you are a Beer Peasant. Prove them wrong!

Adam clicks on the app, consents to use of data and is taken to the following survey:

1. Who would win a game of beer pong?
You or Charlie?

2. Last time you went out with them, who got more wasted?
Brian or Charlie?

3. Who is best at flip cup?
You or Brian?

4. Who is more likely to get so wasted at a bar that he pukes in their bathroom?
Brian or Charlie?

Results:
Brian: Beer Prince
Charlie: Beer Peasant
You: Beer Prince

Will Brian and Charlie agree? Share with them, and see if they rate you a Beer King!

##### Data analysis

Associate user B with bar Z, and user C with bar Y. Throw away answers 1 and 3. Consider the answers to questions 2 and 4. Interpret a choice of a bar as implying that it is associated with binge drinking. If Z is answered twice, then add one to Z's tally in the pairwise Z-Y comparison. If Y is answered twice, then add one to Y's tally in the pairwise Z-Y comparison. If they are answered once each, leave tally.

After thousands of surveys have been completed, we will have obtained a pairwise ranking for every bar in the sample. We can then hope to create a city-wide ranking of bars, in terms of their association with binge drinking, which I call the bar's Puke Rank.

### Survey design

##### Representation

* Population
Young male bar-goers in Chicago.

* Frame population
Population who actively use Facebook

* Sample population
Frame population who have recently been tagged at two separate bars with two separate friends.

* Respondents
Sample population who choose to complete the Beer King app.

##### Digital enhancement

The survey mode is the an internet based app and the survey is computer administered. In terms of Salagnik's benefits of digital enhancement, "Beer King" displays the following:

1. Gamification
"Beer King" is inspired by "Friend Sense" (2010), a Facebook app which gathered masses of data which people would usually be reluctant to give (i.e. their friend's controversial political opinions) by packaging it in a game including light-hearted questions.

As discussed, people are generally reticent to give survey information on binge drinking. "Beer King" aims to make people *want* to give this information *for free*, due to the following reasons. It specifically targets young men (you might expect a certain type) who are susceptible to its methods of persuasion.

* Competitiveness.
The name "Beer King" draws users in to want to publicly display to their friends their drinking process. They will share it with their friends to make it more likely to go viral.

* Rewards.
The partnership with a bar encourages people to share with their friends to make it more likely they will become a Beer King, and will increase the number of friends who will win free pints.

* Positivity
In a serious scientific study, there will be social desirability bias to understating binge drinking. Beer King actually encourages people to be proud of their binge drinking.

2. Enriched Asking

The study combines the digital trace data of tagged bar locations and friends, with the survey data to ascertain drinking behavior.

With the digital trace data alone, we would only know that some people visited a bar.

With survey data alone, as discussed, people do not reveal specific information about their drinking habits accurately.

Combining the two forms, we are able to reveal data about binge drinking at locations. This is done in the following clever way: the survey reveals information about the behavior of friends last time they went to a bar. The digital trace data attempts to ascertain which bar this probably was.

Obviously, this linkage is not perfect. It may actually be the case that after checking-in at Your local and have a glass of lemonade, Adam and Charlie went to XXX-bar and got hammered. Then Your local would get an unfairly high Puke Rank. However, my approach represents a trade-off between accuracy and obtaining honest survey answers. We can't specify location in the survey "Did Charlie get wasted when you went to Your local last night?". People would find that intrusive and will return to their default of avoiding a computer-administered survey! The whole value of the survey is that it appears general to the user but reveals specific information to the analyst.

Relatedly, "Beer King" utilizes what Salagnik calls "Ecological Momentary Assessments" (EMA). A user is only included in the sample when they reach the event-based criteria (i.e. two bars with two separate people recently). The fact that this occurs immediately is another advantage as we are more likely to get accurate recall.

### Sources of error

##### Coverage error. Population to Frame Population.

We lose non-regular Facebook users.
This is not killer. Amongst young males, Facebook usage is at around 90%.

We lose data on bars not able to be tagged on Facebook
Again - most businesses now have Facebook pages.

##### Sampling error

"Beer King" uses non-probability sampling - i.e. it doesn't appear on each user's wall with a specified probability - rather the sample depends on the criteria.

However, this is not a problem for our purposes. We are not trying to estimate some mean value across the population. We are merely trying to create pairwise rankings of locations for each user.

Obviously there is a bias in that bars which are more likely to be tagged at will be included in the Beer King surveys more often. However, this won't push up its Puke Rank, because what matters is its average ranking against other bars.

##### Non-response error

Of those users sampled, I imagine only around 1% will actually respond by completing Beer King.

Again, this is not particularly important. We are not interested in estimating the true value of some variable, but rather obtaining rankings by individuals, regardless of who they are.

### Comparison to observational study

##### Revealing behavior on extreme drinking

On the one hand, Beer King is superior because it just concerns drinking behavior. With the Uber cleaning fees, there is noise from irrelevant cleaning fees - such as illness, random spills, weather etc.

However, the Uber observational data has the huge advantage that it definitely records actual behavior (i.e. a mess in a car), whereas Beer King asks for a friend's opinion on a person's behavior. For this reason, the observational data is superior at revealing this behavior.

##### Linking behavior to locations

Both are imperfect, due to unobservable data. In the Uber case, start locations are often not the same as where the drinking took place. In the Beer King case, as discussed in "Enriched Asking", the tagged location may not be the one where the drinking took place, or where the person has in mind when they complete the survey. I suspect that the Uber start location is more relevant to the behavior, than the most recently tagged bar is to a friend's Beer King answers (which are going to be more general).

### Conclusion

"Beer King"'s main strength is that it is a clever way to encourage certain types of people (young males) to want to reveal information about something they usually wouldn't in a survey. Firstly, by playing to their desires to make them want to complete it. Secondly, by not revealing to them the fact that they are revealing information on specific locations. 
