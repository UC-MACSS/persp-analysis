Hunting for the Russian Trolls
------------------------------

##### MACSS 30000 - Assignment 1

##### Alexander Tyan

##### 10/16/2017

### Context

The past year saw numerous journalist and intelligence reports about
Russian interference in the US presidential elections (Watkins 2016).
This interference allegedly included but may not have been limited to
operations on popular social media outlets, such as Twitter and Facebook
(Weisburd and Watts 2016; “Trolling for Trump: How Russia Is Trying to
Destroy Our Democracy” 2016; Shane and Goel 2017; Leonnig, Hamburger,
and Helderman 2017). Moreover, social media manipulation sponsored by
the Russian (and other) government(s) may extend beyond US presidential
elections. For instance, Russian activity online is linked to other
issues, such as Russian domestic politics and the Ukraine crisis
(Benedictus 2016).

However, such reports tend to be limited because evidence of these
activities is only anecdotal. This is because most reporting is
selective and is based on sparse data, such as leaked documents of
government-sponsored “trolling” and witness accounts (see reports on the
Internet Research Agency for an example (Chen 2015; Walker 2015)). Thus,
despite this information, it is difficult to ascertain the true extent
of such social media manipulation. How many posts are generated? Are
they similar in target destination (e.g. Facebook comments on news
outlets pages vs. wall posts on profile pages, community pages vs
personal wall posts, addressed tweets vs unaddressed tweets)? Is the
content similar in type (e.g. user-generated text vs bot-generated
text)? Is there a preferred strategy (e.g. engaged argument vs strategic
distraction (King, Pan, and Roberts 2017))? In short, the activity is
not very well documented. This research project will address the issue
of Russian-sponsored posts on the social media during the US
presidential campaign in 2015-16, through a more systematic analysis of
data collected on Facebook and Twitter. The data will be (hopefully)
obtained through a collaborative relationship with both platforms, where
the project will be proposed to both firms as an opportunity to gain
insight into content generating patterns and to investigate a
politically salient issue. The challenges for obtaining this data will
be discussed later in the proposal.

### Design

This will be an observational study, counting Russian-sponsored posts
(in English) on Facebook and Twitter between September 2015 and November
2016 (to coincide with the US presidential election campaign). Hence,
each post will serve as a unit of analysis.

The plan will be first to make use of the data leaked from a Russian
government cyber-unit specializing in user-generated Facebook and
Twitter content (Seddon 2014). The data details instructions given to
organization’s employees on how to form their posts, as well as target
number of posts per day. It also contains account names used by the
employees both on Twitter and Facebook. Knowing these accounts may
supply posts associated with them to extract text data. While the data
may not reveal all such accounts and associated posts, it may be used to
train a machine learning algorithm (such as a neural network) on
recognizing such patterns in a wider content. This wider text content
will be Facebook and Twitter records in the specified period to find
which posts are likely to have been originated from such common
practices, even if the original leaked data set does not contain all
account names. We may then infer that such content was generated using
practices outlined in the leaked data set. Hopefully, our machine
learning application is capable of discriminating needed posts from
other seemingly similar content, though there is no guarantee.

Furthermore, results obtained from the machine learning algorithm may
then be used to identify distinct post groups. This may be similar to
clickstream user behavior models identification (Wang et al. 2017). The
main exception may be that the machine-learned language patterns would
be used instead of clickstream patterns and that posts, instead of users
are the unit of analysis. Examples of distinct post groups will be
non-Russian and Russian sponsored user posts. The latter group may be
further subdivided into several distinct groups, though only behavior
model algorithm would tell us what they are more accurately. Since data
analysis is for both platforms with different built-in constraints on
user-generated content, there may emerge different distinct groups
associated with each social media site.

After this sorting mechanism is applied, we will count the number of
posts in each distinct user group and compare which kinds of posts are
occurring with higher frequency relative to other groups. Other data on
variables associated with each observation may help identify groups
further, according to, say, post type and destination (e.g. community
page post, retweet, wall post, comment, etc.) This may depend on data
made available by Facebook and Tweeter.

To put it more formally, our dependent variable is count of posts. The
independent variable would be whether the post spawned from a practice
identified in the leaked government data. If the sorting mechanism is
successful, the dependent variable could also be proportions of posts,
based on the counts in each category. In this case, the independent
variables would be each distinct behavior group.

### Advantages (Salganik 2017)

#### Big

Since the topic of interest is Russian government-sponsored activity on
social media during US presidential campaign, the population of interest
is posts on such social media platforms. The big aspect of the
observational data allows us to overcome some of the non-representative
biases often associated with the traditional sampling techniques. In
other words, we would have access to the data on all of population
without the risk of sampling bias. Pending access to this data, we may
also have information on other variables of interest associated with
each post, like where this post was displayed, at what time, and other
meta data. This may aid us in identifying patterns of post behavior
which we can use to infer strategy and intention behind Russian
government actions, similarly to the of (King, Pan, and Roberts 2017).
The bigness of data may also help identify sudden but short increases or
decreases in post rates, if such an event occurred. Identifying such a
rare event occurrence may not be as easy with a smaller data set.

#### Always On

Since the data stream is always on, our data would be a longitudinal
record of events as they unfolded in the past. This study would not be
possible otherwise, since Russian online activity toward US presidential
elections has taken many by surprise. The record allows to dissect the
process in hindsight.

### Limitations (Salganik 2017)

One potential drawback of such a working relationship with Facebook and
Twitter may be the difficulty in publishing the results of the research,
if the firms insist on keeping the results private, for fear of public
scrutiny and political sensitivity, for example.

#### Inaccessibility

A potential limitation is our uncertainty in data accessibility. We do
not know if the firms would consent to our research project. Even if
they do, they may withhold some data, especially metadata on each post
for privacy or other concerns. This may limit the scope and depth of our
study. Another limitation is our uncertainty of how well the platforms
keep the record of posts. For instance, if a user decides to delete a
post, does the infrastructure erase the traces of the post permanently?
If so, it may skew our data because of behavioral drift risks.

#### Drifting/Algorithmic Confounding

If users who generated posts deleted them because of heightened public
scrutiny of the issue and platforms erased this data, it may result in a
behavioral drift effects. This would distort our data counts in each
post category.

On the other hand, limiting our search window to about one year allows
us to minimize the risk of a system drift. Though we would consult the
firms to verify that there has not been a significant shift in the
algorithms related to posts.

Another potential for behavioral drifting is if the Russian-sponsored
posts have changed their practices significantly between the government
leak and the time of the US presidential campaign. In this case the data
input into the machine learning algorithm may be no longer be
representative of how such posts were generated during the presidential
campaign. Unfortunately, there is not a systematic way to know this,
unless updated data becomes available about Russian government practices
on social media.

### Bibliography

Benedictus, Leo. 2016. “Invasion of the Troll Armies: ‘Social Media
Where the War Goes On.’” The Guardian, November 6, 2016, sec.
Media.<http://www.theguardian.com/media/2016/nov/06/troll-armies-social-media-trump-russian>.

Chen, Adrian. 2015. “The Agency.” The New York Times, June 2, 2015, sec.
Magazine. <https://www.nytimes.com/2015/06/07/magazine/the-agency.html>.

King, Gary, Jennifer Pan, and Margaret E. Roberts. 2017. “How the
Chinese Government Fabricates Social Media Posts for Strategic
Distraction, Not Engaged Argument.” American Political Science Review
111 (3):484–501.

Leonnig, Carol D., Tom Hamburger, and Rosalind S. Helderman. 2017.
“Russian Firm Tied to pro-Kremlin Propaganda Advertised on Facebook
during Election.” Washington Post, September 6, 2017, sec. Politics.
<https://www.washingtonpost.com/politics/facebook-says-it-sold-political-ads-to-russian-company-during-2016-election/2017/09/06/32f01fd2-931e-11e7-89fa-bb822a46da5b_story.html>.

Salganik, Matthew J. 2017. Bit by Bit: Social Research in the Digital
Age. Princeton, NJ: Princeton University Press.

Seddon, Max. 2014. “Documents Show How Russia’s Troll Army Hit America.”
BuzzFeed. June 2, 2014.
<https://www.buzzfeed.com/maxseddon/documents-show-how-russias-troll-army-hit-america>.

Shane, Scott, and Vindu Goel. 2017. “Fake Russian Facebook Accounts
Bought $100,000 in Political Ads.” The New York Times, September 6,
2017, sec. Technology.
<https://www.nytimes.com/2017/09/06/technology/facebook-russian-political-ads.html>.

“Trolling for Trump: How Russia Is Trying to Destroy Our Democracy.”
2016. War on the Rocks. November 6, 2016.
<https://warontherocks.com/2016/11/trolling-for-trump-how-russia-is-trying-to-destroy-our-democracy/>.

Walker, Shaun. 2015. “Salutin’ Putin: Inside a Russian Troll House.” The
Guardian, April 2, 2015, sec. World news.
<http://www.theguardian.com/world/2015/apr/02/putin-kremlin-inside-russian-troll-house>.

Wang, Gang, Xinyi Zhang, Shiliang Tang, Christo Wilson, Haitao Zheng,
and Ben Y. Zhao. 2017. “Clickstream User Behavior Models.” ACM Trans.
Web 11 (4):21:1–21:37. <https://doi.org/10.1145/3068332>.

Watkins, Ali. 2016. “Intel Officials Believe Russia Spreads Fake News.”
BuzzFeed. November 30, 2016.
<https://www.buzzfeed.com/alimwatkins/intel-officials-believe-russia-spreads-fake-news>.

Weisburd, Andrew, and Clint Watts. 2016. “How Russia Dominates Your
Twitter Feed to Promote Lies (And, Trump, Too).” The Daily Beast, August
6, 2016, sec. world.
<https://www.thedailybeast.com/articles/2016/08/06/how-russia-dominates-your-twitter-feed-to-promote-lies-and-trump-too>.
