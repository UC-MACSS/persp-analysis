# Examining gender bias in Wikipedia through the erasure of “notable” women
## Jasmine Mithani

### Research questions
Is there gender discrimination on Wikipedia? The proposed research study aims to address this through the investigation of a much narrower question. Contributions to Wikipedia are practically anonymous; users need not create an account, and the only docuentation is the IP address of the machine used to make a given edit. Since the gender of users is nearly impossible to determine given current resources, this study will focus on gender discrimination in terms of how women versus men are portrayed on Wikipedia. Is there a higher rate of proposal for deletion or deletion for biographical articles about women on Wikipedia? In the cases where articles have not been deleted, was there a high amount of debate as to whether it should be? By answering these narrower questions, we can begin to deduce whether there is systemic gender discrimination in the articles represented on Wikipedia.

### Experimental design
Wikipedia has explicit guidelines for the type of content that is appropriate to post on its website. One of commonly cited rules used to promote deletion of an article is the requirement of notability.

>On Wikipedia, notability is a test used by editors to decide whether a given topic warrants its own article. For people, the person who is the topic of a biographical article should be "worthy of notice"or "note" – that is, "remarkable" or "significant, interesting, or unusual enough to deserve attention or to be recorded" within Wikipedia as a written account of that person's life. "Notable" in the sense of being "famous" or "popular" – although not irrelevant – is secondary...People are presumed notable if they have received significant coverage in multiple published secondary sources that are reliable, intellectually independent of each other, and independent of the subject. *[1]*

Biographical articles need to profile someone of sufficient status as to deserve an entry in an international encyclopedia. A tangible way to measure gender bias would be to compare Wikipedia entries of men and women of the same notability through established metrics. The proposed metrics are as follows.

* Article quality, which is measured by a six-step scale employed by Wikipedia. The danger here is that the system itself may be biased, but this will be a useful quantity to compare to our own definition of quality.
* Article length, in number of words.
* Number of links to other Wikipedia articles it contains.
* Number of times cited for deletion.
* Rules cited by editors as a reason for deletion.

I will find plausible matches of notable men and women by narrowing the pool to a sufficiently small sample size. A large part of Wikipedia editing is finding and citing reliable sources. For scholarly articles, Wikipedia considers a source reliable if the journal it is published in has a high citation index.*[2]* For the realm of scientific research, the top publications would be Science, Nature, and PNAS. Knowing that Wikipedia recognizes the validity and prestige of these publications, the first step in choosing our sample is culling all corresponding authors from articles published in those journals for the past ten years. Corresponding authors have been chosen because they are most likely to be well-established and widely known in their field – it would be unfair to compare a post-doctoral researcher to a tenured faculty member running their own lab. From this pool, matches will be made from men and women who have the same number of lifetime citations, within a certain bound. The gender of the subjects will be determined from Genderize.io, an API service that returns a gender (male, female, none) and the probability its guess being correct.

### Good elements

Wikipedia has a huge number of editors, many articles, and has been an active community for over a decade. There is a large amount of data to sift through, both of articles and the conversation pages attached to each one. While there have been internal efforts to address gender bias in the information coverage of Wikipedia, the data can be considered non-reactive. While all conversation on Wikipedia is public, the purpose of it is for communication, not a massive data collection effort. For years Wikipedia has grown to become a multidisciplinary topic of research, however I am assuming that the average Wikipedia editor is not primarily considering how their actions will be analyzed scientifically when they are performing them.

### Bad elements

One of the main difficulties with the big data required for this study is the issue of **incompleteness**. Once an article is deleted from Wikipedia, all of the history and content of that article is permanently removed. Several sites are dedicated to archiving Wikipedia’s deleted content, but they only have information stored from a handful of years and their method and detail of curation is unreliable. The study is attempting to unearth systemic gender bias, which ideally could be measured in the number of biographical articles of notable women that have been deleted compared to that of men. The counts necessary to measure rate of production and deletion are incomplete, and the study will need to use alternative measures or account for this missing data.

The study will conducted only on the English language version of Wikipedia, and the journals used to cull researchers are published in English. This could perpetuate a cultural bias, but the results of the study will still remain significant within this frame.

The gender of authors is **inaccessible** in a form easy gathered for large-scale research. The most accurate way to gauge gender would be by searching for each faculty member online and then making a binary guess based on their biographies, but that is difficult to automate and a large waste of resources. Many online services are available for guessing the gender of first names, and rely on catalogs of name-gender pairings from the world over. The reliability of these services and the sources of their data are murky, but a necessary risk needed in order to perform the experiment. Genderize.io helpfully includes a probability factor; names below a certain threshold (e.g. 0.85) could be eliminated from the sample. It is possible that this could favor a certain nationality or small group of names, thus not accurately creating a representative sample. Many names are androgynous, and their gender assignment would depend on the service being used.

As Salganik notes in an example, some of the editing and deleting behavior on Wikipedia is due to bot activity, increasing the **dirtiness** of the data.*[3]* While is it important to consider these as a part of a potential gender discrimination problem, it will be difficult to categorize their actions without knowing the purpose and programming of the bot.

### Works Cited
[1] [“Wikipedia:Notability (people)”](https://en.wikipedia.org/wiki/Wikipedia:Notability_(people)) *Wikipedia: The Free Encyclopedia.* 4 Sep 2017. 16 Oct 2017. Web.

[2] [“Wikipedia:Identifying reliable sources.”](https://en.wikipedia.org/wiki/Wikipedia:Identifying_reliable_sources) *Wikipedia: The Free Encyclopedia.* 8 Sep 2017. 16 Oct 2017. Web.

[3] Salganik, Matthew J. *[Bit by bit: social research in the digital age.](http://www.bitbybitbook.com/#)* Princeton University Press, open review edition. Web.
