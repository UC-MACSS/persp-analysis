---
output:
  html_document: default
  pdf_document: default
  word_document: default
---
# Dusty but not Dirty: Identifying political fundraising rule skirting from Elections Canada donation records
Tyler Amos

MACSS 30000

University of Chicago

October 16, 2017

Word count (excluding references and titles): 1,452

## Summary
In the past few years alone Canadian Senators, sitting Members of Parliament and a number of campaign operatives at both federal and provincial levels have all faced scrutiny for violating, or appearing to skirt political finance rules. Media investigations regularly highlight criminal wrongdoing and unethical practices which skirt rules without breaking them. (Globe and Mail 2017; Maclean's 2017; Maclean's 2016; National Post 2017; CBC 2013; CBC 2012)  While Elections Canada and law enforcement publicize their findings in cases of criminal wrongdoing, it is substantially less clear to what extent political financing rules are being skirted but not broken.  

In this study, a straightforward "counting" technique (Salganik 2017, 2.4.1) will be used to investigate the principal research question: How prevalent are irregular political donation patterns? Additional research questions will also be investigated, including:

  * To which political entities are irregularly-patterned donations directed?
  * Do certain types of organizations (unions, corporations, small business, etc.) appear more often in connection with irregular donation patterns?

## Motivation
Approaching this issue from the normative position that rule skirting should be deterred, this study will improve understanding of a legal, ethically questionable practice. Once an initial understanding has been developed, it may be possible to develop techniques to identify irregular donations more quickly and allocate enforcement (or education) resources appropriately. Furthermore, the volume of irregular donation patterns across time may inform some analyses of successive policy reforms. 

## Research Design
Irregular donation patterns will be understood as any combination of the following behaviours (Globe and Mail 2007; Democracy Watch; CBC 2006):

   * Numerous donations just below various reporting thresholds;
   * Numerous donations by entities with shared features such as surname or postal code;
   * Donations to candidates in ridings outside of the contributor's region;
   * Frequent cash donations;
   * Donations in the name of individuals not registered to vote.
   
Additional characteristics may emerge in the course of research, these heuristics will be adjusted accordingly. By identifying these behaviours in official datasets and web-scraped data, this study will quantify irregular donation patterns in political contribution records, which is assumed to represent rule skirting.

### Data Sources
The principal data source for this project will be the Elections Canada record of political donations from 2004 to the present. This dataset is freely available from Elections Canada and contains attributes on contributors and recipients such as names and donation amounts. (Elections Canada, _Open Data_) This dataset will be merged with two other datasets which cover the period 1994 - 2003. Altogether, these datasets detail approximately 4.8 million donation records (4.2 million from 2004 - the present; 600,000 from 1993 - 2003)

This dataset will be used as a starting point to build more complete donor profiles. This will be achieved using two data acquisition and merging tasks. First, access to the Elections Canada National Register of Electors will be requested, and if permission is granted, these records will be linked to the record of political contributions from 1994 - the present. They will also provide a means to identify donations made in the name of individuals not registered to vote. Historical lists from the Register will be used to complete records from before 2004, which do not include the same level of detail as 2004 to the present. Second, supplementary information on organizations will be collected via web scraper, providing data on organizations' activities and staffing. This will be linked to business, corporate, non-profit, and union donations detailed by Elections Canada records.  

### Using Observational Data to Answer the Research Question
To the author's knowledge no large-scale, big data-informed investigation of donation rule skirting in Canada has been done. As a first foray, this study will establish a baseline understanding of the extent of rule skirting, as measured by irregular donation patterns. In order to establish this baseline, it is necessary to identify and count irregular donation patterns. Policy makers and implementers would benefit most from more advanced approaches such as prediction, but given the lack of existing research in this area, an emphasis will be placed on more foundational analyses. Specifically, observed counts of irregular behaviours will be caculated. Once this baseline has been identified, dissaggregated counts of irregular donation patterns will be computed across individual and organizational attributes. 

### Leveraging the Advantages of Big Data
This study will leverage the advantages of big data, as defined by Salganik (2017, 2.3) in a number of ways:

### Big
The roughly 4.8 million core records from Elections Canada, along with additional data gathered from the Register of Electors and scraped from web sites affords an opportunity to study, in a quantitatively rigorous way, what may be a rare event. The size of this dataset also helps to investigate specific behaviours of organizational contributors and may allow some generalizable findings about the role these organizations played in political finance. This in turn may offer some insights as to the effect of federal reforms prohibiting organizational contributions.

### Non-reactive
Using organizations' web presence to complete campaign donation records offers an opportunity to observe organizations in an environment in which they are not aware their data is being collected for use in this project. In other words, the organizations which will be studied may have a web presence, but this is intended for their everyday operations, not to justify past political contributions. Therefore, the subject (the organization, through its web presence) will not adapt their behaviour in response to observation and (in theory) the result will be more accurate data on the variables of interest. 

### Mitigating the Risks of Big Data
While a big data-informed approach has advantages, this study will take care to mitigate certain risks (Salganik 2017, 2.3):

### Incomplete, Inaccessible and Dirty
As mentioned above, donation records have become progressively more detailed over time. Earlier records offer limited data, which will need to be completed through record linkage with additional datasets. Data on organization attributes is also missing, this will need to be collected using a web scraper. Nonetheless, some information will not be available (e.g., business which have closed, voters who never registered as electors). Other data may be incorrectly assigned to a given record. Due to the size of the dataset and its bias towards the the individual-only contribution regulatory regime (post-2006) neither of these issues is anticipated to have a substantial impact on results. 

Another risk is inaccessibility. The clearest case of this is the missing organizational attributes necessary to build profiles of organizational contributors. This data is present in government records, including tax filings. However, this data would be challenging to access due to privacy, confidentiality, and cost concerns (some access pathways are paid services). Comparable information will be collected by web scraping. Similarly, the Register of Electors is inaccessible without permission from Elections Canada. However, the author does not anticipate Elections Canada denying access to the Register (the data is already provided to political parties). Nevertheless, the core investigation of this study does not require access to the Register, and the study is thus insulated from inaccessibility risks.

Data collected via the web scraper will likely be "dirty" - requiring substantial manipulation in order to extract relevant information.  To mitigate this challenge, the web scraper will be targeted at business listings and government records such as YellowPages, and Canada Revenue Agency's public filings for non-profits (CRA 2017). The advantage of targeting the web scraper will be more predictable formatting and more authoritative data. This may sacrifice some completeness, but the time saved through this strategy is judged to outweigh the risk of incompleteness. 

### System Drift
Fundraising behaviour and dynamics have drifted over the course of the study period. The most clear of these is the ban on organizational contributions. Contribution limits have also shifted as a result of successive regulatory changes. Furthermore, business and other organizations will have closed or merged. To some extent, these changes are anticipated and will be of interest (e.g, regulatory changes). Others present challenges (e.g., business closure), which will have to be addressed on a case-by-case basis. 
      
### Sensitive
The contributions records used in this study will contain some personal information such as postal code, name, and amounts donated. While this information is public, it is not readily accessible, thus the act of consolidating it is akin to rigorous investigation of a particular individual or organization. The researcher will exercise discretion in communicating their findings by avoiding mentioning identifying characteristics when citing examples. 

## Conclusion
Starting from Elections Canada political contribution data, this study will build a more complete picture of patterns in political contributions in order to identify rule skirting behaviours. Quantifying these behaviours will provide a baseline for further study and action on ethically questionable, but legal practices. Building on these findings, future research may include prediction or classification to improve detection of irregular contributions.

## References
CBC. 2012. _9 Facts about Pierre Poutine and the robocalls case_ http://www.cbc.ca/news/politics/9-facts-about-pierre-poutine-and-the-robocalls-case-1.1143560

CBC. 2013.  _Elections Canada audit seeks those dodging donation limits_  http://www.cbc.ca/news/politics/elections-canada-audit-seeks-those-dodging-donation-limits-1.1302829

CBC. 2006. _Political Contributions: Money, Money, Money_ http://www.cbc.ca/news2/background/cdngovernment/political-contributions.html

Democracy Watch. Bill C-2 Analysis. http://democracywatch.ca/c2analysis/

Canada Revenue Agency (CRA). 2017.  _Registered Charity Information Return_ https://www.canada.ca/en/revenue-agency/services/charities-giving/charities-listings.html

Elections Canada. _Open Data_ http://www.elections.ca/content.aspx?section=fin&dir=oda&document=index&lang=e 

Globe and Mail. 2017. _With cash-for-access, Justin Trudeau picks up where Kathleen Wynne left off_ https://beta.theglobeandmail.com/opinion/editorials/with-cash-for-access-justin-trudeau-picks-up-where-kathleen-wynne-left-off/article32464117/

Globe and Mail. 2007. _Ottawa refuses to close donation loophole_ https://beta.theglobeandmail.com/news/national/ottawa-refuses-to-close-donation-loophole/article20399805/?ref=http://www.theglobeandmail.com& 

Maclean's. 2017. _How Ottawa banned corporate donations to parties_ http://www.macleans.ca/politics/ottawa/how-ottawa-banned-corporate-donations-to-parties/

Maclean's. 2017. _Inside the progressive think tank that really runs Canada_ http://www.macleans.ca/politics/ottawa/inside-the-progressive-think-tank-that-really-runs-canada/

National Post. 2017. _Elections Canada finds more than 40 cases of ineligible coporate donations from 2011 federal election_
http://nationalpost.com/news/politics/elections-canada-finds-more-than-40-cases-of-ineligible-corporate-donations-from-2011-federal-election

Salganik, Matthew. 2017. _Bit by Bit: Social Research in the Digital Age._ Princeton, NJ: Princeton University Press. Open Review Edition. http://www.bitbybitbook.com/
