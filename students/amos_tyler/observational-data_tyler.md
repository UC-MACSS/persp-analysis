---
output:
  word_document: default
  pdf_document: default
  html_document: default
---
    
# Dusty but not Dirty: _Identifying political fundraising rule skirting from Elections Canada donation records_
Tyler Amos

MACSS 30000

University of Chicago

October 16, 2017

Word count: 

### One-Sentence Summary
The proposed study investigates skirting of political donation regulations by identifying irregular donation patterns in campaign and party donation records and the list of electors, supplemented by data scraped from a variety of websites. 

## Summary
Laws which delimit acceptable political behaviour in Canada are regularly revised, often in response to scandals. In the past few years alone a Senator, a sitting Member of Parliament and a number of campaign operatives at both federal and provincial levels have all faced criminal charges for violating these rules. In 2004 the governing Liberals restricted contributions to individuals in response to the Sponsorship Scandal. (Maclean's 2016) Only recently have a number of the larger provinces done the same and prohibited corporate/union donations. Media investigations regularly highlight criminal wrongdoing in this domain, as well as unethical practices which skirt rules without breaking them. (Globe and Mail 2017; Maclean's 2017 ) Violations are not constrained to incumbents either, with both candidates and supporters participating. (National Post 2017; CBC 2013; CBC 2012)  While Elections Canada and law enforcement publicize their findings in cases of criminal wrongdoing, it is substantially less clear to what extent political financing rules are being skirted but not broken.  

In this study, a straightforward "counting" technique (Salganik 2017, 2.4.1) will be used to investigate the principal research question: How prevalent are irregular political donation patterns? This will be investigated through a number of targeted questions. Specifically:

  * How often do irregular donation patterns occur?
  * To which organizations are irregularly-patterned donations directed?
  * In pre-2004 donations, do certain types of organizations (unions, corporations, small business, etc.) appear more often in irregular donation patterns?

## Motivation
As noted above, political financing scandals are a regular feature of the Canadian political landscape. Approaching this issue from the normative position that rule-skirting, if it occurs, should be deterred, this study will improve understanding of an ethically questionable, but legal practice. Once an initial understanding has been developed, it may be possible to develop techniques to identify irregular donations more quickly and allocate enforcement (or education) resources appropriately. Furthermore, the volume of irregular donation patterns across time may provide some indication as to the effectiveness of political financing reforms. 

##Research Design
Starting from fundamentals, this study will seek to identify irregular donation patterns, as characterized by a combination of the following:

   * Numerous donations below maximum allowable amounts in the same election cycle;
   * Numerous donations by individuals (or organizations for pre-2004 data) with shared features such as surname or postal code;
   * Donations to candidates in ridings outside of contributors' area of residence;
   * Frequent cash donations below the threshold required for recording contributor information;
   * Donations in the name of individuals not registered to vote;
   * Additional characteristics which emerge in the course of research.
   
Applying these heuristics to a combination of official datasets and web-scraped data, this study will attempt to identify irregular donation patterns in political contribution records in order to quantify the extent of rule-skirting in Canadian campaign finance. 

###Data Sources
The principal data source for this project will be the Elections Canada record of political donations from 2004 to the present. This dataset is freely available from Elections Canada and contains attributes on contributors such as names, postal codes, and donation amounts, as well as recipient attributes such as name, electoral event and political party. (Elections Canada, _Open Data_) To provide historical context, this dataset will be merged with two other datasets which cover the period from 1994 to 2003 (inclusive). Altogether, these datasets detail approximately 4.8 million donation records (4.2 million from 2004 - present; 600,000 from 1993 - 2003)

This dataset will be used as a starting point to build more complete profile of donations. This will be achieved using two data acquisition and merging tasks. First, access to the Elections Canada National Register of Electors will be requested, and if permission is granted, these records will be linked to the record of political contributions from 1994 - present. Historical lists from the Register will be used to complete records from before 2004, which do not include the same level of detail as 2004 to present (e.g., address information is missing for some older records). They will also provide a means to identify donations made in the name of individuals not registered to vote, one of the study's guiding heuristics. While the author does not anticipate Elections Canada denying access to the Register, the core investigation of this study does not require access, and the success of the study is thus insulated from this risk.  Second, supplementary information on organizations will be collected via web scraper, providing data on industries and staffing for organizational contributors (pre-2004). This will be linked to business, corporate, and union donations detailed by Elections Canada records.  

###Using Observational Data to Answer the Research Question
To the author's knowledge no large-scale, big-data informed investigation of irregular donation patterns has been done. As the first to investigate this topic, this study will first and foremost seek to establish a baseline understanding of the extent of rule-skirting, as measured by irregular donation patterns. In order to establish this baseline, and in doing so respond to the research question, it is necessary to identify and quantify irregular donation patterns. Future analyses would benefit from more advanced approaches such as prediction (e.g., nowcasting), but given the lack of existing research in this area, an emphasis will be placed on more foundational approaches. Specifically, observed counts of irregular behaviours will be established. Once this baseline has been identified, dissaggregated counts of irregular donation patterns will be computed and from these, conclusions drawn. 

###Leveraging the Advantages of Big Data
This study will leverage the advantages of big data, as defined by Salganik (2017, 2.3) in a number of ways:

#####Big
The roughly 4.8 million core records from Elections Canada, along with additional data gathered from the Register of Electors and scraped from web sites affords an opportunity to study, in a quantitatively rigorous way, what may be a rare event. The size of this dataset also helps to investigate specific behaviours of organizational contributors (large and small businesses, unions, etc.), and may allow some generalizable findings about the role these organizations played in political finance. This in turn may offer some causal insights as to the effect of federal reforms prohibiting corporate and union contributions.

#####Non-reactive
Using organizations' web presence to complete campaign donation records offers an opportunity to observe (i.e., acquire data) organizations in an environment in which they are not aware their data is being collected for use in this project. In other words, the organizations which will be studied may have a web presence, but this is intended for their everyday operations, not to justify past political contributions. Therefore, the subject (the organization, through its web presence) will not adapt their behaviour in response to observation and (in theory) the result will be more accurate data on the variables of interest. 

###Mitigating the Risks of Big Data
While a big data-informed approach has advantages, this study will take care to mitigate certain risks: (Salganik 2017, 2.3) 

##### Incomplete, Inaccessible and Dirty
As mentioned above, donation records have become progressively more detailed over time. Earlier records offer limited data, which will need to be completed through record linkage with additional datasets. Data on organization attributes is also missing, this will need to be collected using a web scraper. Nonetheless, some information will not be available (e.g., business which have closed, voters who never registered as electors). Other data may be incorrectly assigned to a given record. Due to the size of the dataset and its strong bias towards more current records (post-2004) it is unlikely this will have a substantial impact on results. 

These points also apply to another risk - inaccessibility The clearest case of this is the organizational attributes necessary to understand the behaviour of organizations in political financing. This data is in fact contained in government records, including tax filings. However, this data would be challenging to access due to privacy and confidentiality concerns. Thus, this information will be collected by web scraping. In addition, the Register of Electors is inaccessible without permission from Elections Canada. The author judges that this data is more likely to be accessible, as it is already shared with political parties. 

Data collected via the web scraper will likely require substantial manipulation in order to identify relevant information.  To mitigate this challenge, the web scraper will be targeted at particular types of business and organizational listings (e.g., LinkedIn, YellowPages, etc.). The advantage of targeting the web scraper will be more predictable formatting and more authoritative data. At the same time this may sacrifice some completeness, but the time saved through this strategy is judged to outweigh the risk of incompleteness. 

##### System Drift
Fundraising behaviour and dynamics have drifted over the course of the study period. The most clear of these is the 2004 ban on organizational contributions. Contribution limits have also shifted as a result of successive regulatory changes. Furthermore, business and other organizations will have closed or merged. To some extent, these changes are anticipated and will be of interest (e.g, regulatory changes). Others present challenges (e.g., business closure), which will have to be investigated on a case-by-case basis. 
      
##### Sensitive
The contributions records used in this study will contain some personal information such as postal code, name, and amounts donated. While this information is public, it is not readily accessible, thus the act of consolidating it is akin to a rigorous investigation of a particular individual or organization. The researcher will exercise discretion in communicating their findings by avoiding mentioning family names when citing examples. 

##Conclusion
Starting from Elections Canada political contribution data, this study will build a more complete picture of patterns in political contributions in order to identify rule-skirting behaviours. Quantifying these behaviours will provide a baseline for further study and action on unethical, but legal practices. Building on these findings, future research may include predictive or classification models to improve detection of irregular contributions. Most importantly, this study will provide badly-needed information on the extent of these practices, which will inform policy debates. 

## References
CBC. 2012. _9 Facts about Pierre Poutine and the robocalls case_ http://www.cbc.ca/news/politics/9-facts-about-pierre-poutine-and-the-robocalls-case-1.1143560

CBC. 2013.  _Elections Canada audit seeks those dodging donation limits_  http://www.cbc.ca/news/politics/elections-canada-audit-seeks-those-dodging-donation-limits-1.1302829

Elections Canada. _Explaining Turnout Decline in Canadian Federal Elections_ http://www.elections.ca/content.aspx?section=res&dir=rec/part/tud&document=reasons&lang=e
Elections Canada. _Open Data_ http://www.elections.ca/content.aspx?section=fin&dir=oda&document=index&lang=e 

Elections Canada. _Voter Turnout at Federal Elections and Referendums_ http://www.elections.ca/content.aspx?dir=turn&document=index&lang=e&section=ele
Globe and Mail. 2017. _With cash-for-access, Justin Trudeau picks up where Kathleen Wynne left off_ https://beta.theglobeandmail.com/opinion/editorials/with-cash-for-access-justin-trudeau-picks-up-where-kathleen-wynne-left-off/article32464117/

Maclean's. 2017. _How Ottawa banned corporate donations to parties_ http://www.macleans.ca/politics/ottawa/how-ottawa-banned-corporate-donations-to-parties/

Maclean's. 2017. _Inside the progressive think tank that really runs Canada_ http://www.macleans.ca/politics/ottawa/inside-the-progressive-think-tank-that-really-runs-canada/

National Post. 2017. _Elections Canada finds more than 40 cases of ineligible coporate donations from 2011 federal election_
http://nationalpost.com/news/politics/elections-canada-finds-more-than-40-cases-of-ineligible-corporate-donations-from-2011-federal-election

Salganik, Matthew. 2017. _Bit by Bit: Social Research in the Digital Age._ Princeton, NJ: Princeton University Press. Open Review Edition. http://www.bitbybitbook.com/


## Submitting your assignment

See [here](../students/) for instructions on submitting course assignments.

## Submission deadline

Submit your pull request before class on Monday, October 16 (11:30 am).
