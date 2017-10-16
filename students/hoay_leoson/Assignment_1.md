### MACS30000 Assignment 1
### Wikipedia and and its impact on Science Communication
#### Leoson Hoay
#### October 16, 2017

============================
## Contents
* [Introduction and Research Question](#introduction)
* [Data Sources](#data)
* [Methodology and Advantages](#method)
* [Limitations](#limitations)
* [Conclusion](#conclusion)
* [References](#references)



## Introduction and Research Question <a name = "introduction"></a>
Wikipedia's role in 21st century knowledge aggregation and dissemination should not be underestimated. A 2011 study by Biddix et. al([1]) revealed that alongside libraries and databases such as Google Scholar, Wikipedia is still a significant node in the typical college student's research process in completing academic work, in spite of the contentious nature of the reliability Wikipedia in the academic setting. Furthermore, a very recent paper from the MIT Sloan School of Management([2]) investigated Wikipedia's potential to "shape science" - which found significant co-occurences between word usage in Wikipedia articles and that of contemporaneous scientific literature. The researchers were also able to estimate a significant causal model of new Wikipedia articles on the content of scientific publications. The results suggest the stirring implication that Wikipedia's modes and patterns of knowledge dissemination has an observable relationship with academia and knowledge advancement at the frontiers.

While these findings speak volumes about Wikipedia's role and power in knowledge dissemination - and creation - they are isolated in the academic context. For the generalist interested in various scientific topics or the average citizen who wants to know how new science affects his/her/their life, scouring academic articles is an unlikely activity. These individuals may use Wikipedia itself for information, but often do so with a pre-conceived notion of what they are looking for. It is far more likely that "science news" first reaches the public through online media and television([3]), and the popular science communicators that operate through these channels. Given the above, I propose an observational study that investigates the correlation between Wikipedia articles and contemporaneous content in popular science communication media. This can be investigated both at the single-field level and at the level of multiple fields of scientific inquiry.
 

## Data Sources <a name = "data"></a>
There are two core sources of data required for the proposed study. 

The first is the document data and metadata of Wikipedia articles, which can be obtained by scraping the article content off the Wikipedia webpages, or directly making use of the open-licensed metadata published by Wikimedia and Wikidata. The latter choice may be preferred as the open-licensed data already keeps track of important information such as revisions, and does so in a number of useful analyzable formats (XML, JSON, etc.). To define the specific type of document data and metadata required, if the investigation is addressing a chosen field of science (e.g. Astronomy), then individual articles categorized under the particular field could be looked at at the document level. At the level of multiple fields, metadata about the categorical occurence frequency of articles in their respective scientific fields will be of interest. 

The second source of data is the document and media data of content produced within popular science communication media. For the purposes of this proposal, the scope of the aforementioned media should be defined and sampled in a strategic manner. While it will be beneficial to include television-based science programs into the pool([3]), I propose that television-based media be omitted. This is primarily due to the complexity required to code the data into an analyzable format, and secondarily due to the prevalance of mixed media sources online - online video accompanied with articles([4]), for example - that give these online articles additional dimensionality. The eventual data sample will include a cluster of online science communication sites that have been deemed popular to the public and reliable by some measure or another. In this case, I would propose the usage of this list([5]) of popular science sites by Ebizmba.com as a guide, which includes Discovery, Nature News, and PopSci, among others. The articles posted on these sites will be the data of interest.

Both sources should be easily obtainable, either through readily available open-source data, or through web scraping methods.


## Methodology and Advantages <a name = "method"></a>
To determine the correlation between the content on Wikipedia and those of science media, a time window will be defined for the analysis to take place. The cited study by Thompson and Hanley([2]) uses a twelve year window, which is appropriate for this proposed study as well. In making a single field comparison, document analysis can be used to compare word occurences between Wikipedia articles and science media articles over a time period. When making discipline level comparisons, the occurences of categories can be compared between Wikipedia articles and the science media websites.  

The first advantage that big data lends to this study is definitely that the proposed dataset is a big one. Wikipedia alone boasts over 5 million articles in English, and the amount of aggregated articles from popular science media websites is not to be laughed at as well. This firstly allows for the detection of small differences which may aggregate into significant ones - which is of primary importance in this study when investigating a correlation where each individual article contributes a miniature portion towards the aggregate pattern. Secondly, it may allow the study to reveal insights about subgroups (i.e. Do chemistry articles on Wikipedia have a stronger correlation with its corresponding publications on science media sites as compared to psychology?).

The next advantage is the always-on nature of the dataset - both Wikipedia and science media sites are long-term in their functioning and are constantly being updated. A time period correlation study of this scale will not be possible if the data sources were intermittently online, or if archived content were difficult to access/non-existent.

Lastly, the data and its retrieval is non-reactive. This prevents actions by the researcher to have an effect on the data values. The underlying mechanisms that may link Wikipedia articles to academic study and science news publication may be complex and unknown, and any interaction with the actors involved in the process may have an effect on the measured factors. Fortunately, with this non-reactive dataset, this concern can be eliminated. 


## Limitations (and potential strategies to address them) <a name = "limitations"></a>
The proposed study is has several identifiable limitations. 

System drift is an important potential concern, especially when obtaining data from Wikipedia. It is possible that Wikipedia's submission processes, technical limitations and affordances of article creation, and automated algorithms that categorize, sort, and remove articles from the repository change over time. In accounting for these possible changes, it may be prudent to obtain records of these changes from Wikipedia and interpret the eventual results of the analysis alongside these changes. Population drift is another concern, in terms of the article contributors and editors from both Wikipedia and science media websites. As employees and contributors change over time, alongside shifts in the conventions of science writing, there might be some drift in terms of the tone and language used in the articles. To overcome this, it will be wise to to characterise this drift using a separate model in order to establish a baseline change with which to work from([2]).  

It is also inevitable that these data sources will be incomplete. For one, the list of science media sites excludes other outlets, and also other forms of science communication such as those that manifest via social media. Second, in deciding on the scientific disciplines to be included in the dataset, others will be inevitably excluded. To manage the former, a parallel study which focuses on other forms of science communication could be conducted. To manage the latter, the discipline/cluster of disciplines should be chosen in a way that maximises the representativeness of "science" as a whole. 


## Conclusion <a name = "conclusion"></a>
In closing, the proposed study is well situated within current advancements in big data technologies and methods of analysis. It is a fluent extension of past studies on Wikipedia - which have demonstrated how integral the repository is for many students and budding researchers alike, and also illuminated the "feedback effect" that it has on scientific inquiry. I have personally used Wikipedia numerous times as an entry point into deeper branches of a particular field of knowledge, and on occasion just out of plain curiousity about a specific topic. For the creators and members of the Wikipedia community, studies in this vein are but one of the many validations that the repository is indeed a force in knowledge, and one that has meaningful impact.

Wikipedia's open source nature situates the repository in constant disputes regarding its perceived and actual reliability, but it is precisely this open source nature - leveraging on the power of community and scale - that it is able to exist in the form that it does today. Regardless of one's judgment of the reliability of Wikipedia articles, it is difficult to dispute the notion that Wikipedia pulls some serious weight in realm of modern knowledge. Studies such as the ones referenced above and the one being proposed may unveil useful insights into how Wikipedia should move forward as an organization and repository, given its manifest influence in knowledge dissemination, generation, and possibly on what this proposed study seeks to investigate - the public communication of scientific knowledge. 


## References <a name = "references"></a>

- Biddix, J.P., Chung, C.J., & Park H.W. (2011). Convenience or credibility? A study of college student online research behaviors. Internet and Higher Education, 14, 175-182.
- Thompson, N.C., Hanley, D. (2017). Science is shaped by wikipedia: Evidence from a randomized controlled trial. MIT Sloan School of Management Working Paper 5238-17.
- Mitchell, A., Gottfried, J., Barthel, M., Shearer, E. (2016).The Modern News Consumer: News attitudes and practices in the digital era. Pew Research Center. Retrieved from: http://www.journalism.org/2016/07/07/pathways-to-news/


[1]: https://www.researchgate.net/publication/222036119_Convenience_or_credibility_A_study_of_college_student_research_behaviors
[2]: http://www.nature.com/news/wikipedia-shapes-language-in-science-papers-1.22656
[3]: http://www.journalism.org/2016/07/07/pathways-to-news/
[4]: http://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970

