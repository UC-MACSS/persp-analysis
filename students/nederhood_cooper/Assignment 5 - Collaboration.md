# Collaboration

### By Cooper Nederhood

### Kaggle open call projects (3 points)

[Kaggle.com](https://www.kaggle.com/) is a data science website that hosts open call projects, datasets, data science competitions, code, and more.

1. Explore the Kaggle [competitions page](https://www.kaggle.com/competitions), which maintains a list of open call projects. Describe one that is of interest to you. What is the goal of the competition? What would you have to do to make a submission?

#### What is the goal of the competition? 
Having performed analytics on mortgage data at my previous employer, I am interested in the 'Zillow Home Value Prediction: Zestimate' competition. Zillow is a website providing estimates of the sales price of homes. The goal of the competition is to improve the accuracy of current Zillow sale price prediction algorithm. The winning algorithm could affect the value of over 110 million homes around the United States.

#### What would you have to do to make a submission?
There are two rounds to the competition. Because real-estate data is public information, after the close of each round there is a 3-month tracking period to test the results. While every submission must value each house, if a sale does not occur in the given period then that valuation is not counted towards the accuracy testing. 

The first round is open to the public. Competitors need to register and download the posted training data from Zillow on Kaggle. The sale price for each property is the training target. A submission consists of a log error prediction for each property at each of the specified time points. The first-round deadline is October 16, and immediately following the deadline the 3-month testing period begins. Winners and second round qualifiers are notified in January. 

The second round is similar, but is only open to the highest 100 performers of round one. Second round performers also need to sign non-disclosure agreements and an agreement to assign all intellectual property to Zillow. Even losers in the second round do not have a right to the IP generated in their losing effort. After another 3-month testing period, the overall winners are determined and prizes awarded.

1. Explore the available datasets on the Kaggle [datasets page](https://www.kaggle.com/datasets). Download one of the datasets and generate a descriptive plot that highlights some instructive characteristic of the data. Make sure your plot has a title, labeled axes and axis titles, and a legend if necessary. Submit your script (`.R` or `py`) and your plot (saved as a PDF). Make sure your script is properly commented and reproducible.

See IPython notebook file

### Improving a journal article (3 points)

Look through a recent issue of a journal in your field. Find a paper that you think could have been reformualted as a human computation project. How would you formulate the data collection as a human computation project? How might this improve the study?

In Geoff Boeing's paper "OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks" he presents a Python tool, OSMnx, he has developed to analyze city street maps. His package allows for the automated downloading of street maps across thousands of cities internationally and can then construct graphs based on the network of streets (edges in the graph) and intersections (nodes in the graph). Once the street network has been caste as a graph, the package can return various graph theoretic measures related to the connectedness and general dynamics. 

The project in this paper is the functionality of the Python package and a crucial step in the viability of the end-product graph is the "algorithmic correction of network topology." This step is the cleaning stage from raw map data, which reflects the endless heterogeneity across city structure, to the streamlined graph consisting of only nodes and edges. Formulating this step as a human computation project could greatly increase the accuracy of final graph. Identifying subtle characteristics in city structures like discerning between a parking lot and an alley, an overpass and a tunnel, etc. are straightforward tasks for a human but are more difficult for a computer algorithm. Ultimately, the functionality of the package requires an algorithm to clean the graph structures. However, he could create an online human computation component where participants can verify algorithmically cleaned structures against satellite images. Images can be pulled easily through Google Maps. If the participant identifies issues with the cleaning result she can report and classify the error. Hopefully, if there are systematic shortcomings in the cleaning algorithm these will emerge in large scale verification more fully than a simple one-man verification. Any corrections can then be tested to determine if further corrections are warranted. 

I was excited by this paper because it presents an interesting tool for future research, the tool is free, and the code is publicly available on GitHub. However, the usefulness of this tool fundamentally hinges on the reliability of the graphs that it produces. Employing human computation in the verification process would greatly increase the accuracy of the end-product graph. 

### Alternative assignment: InfluenzaNet (4 points)

Google Flu Trends analyzes historical relationships between search queries and flu patterns and applies this relationship to current search queries to estimate current flu amounts. Traditional influenza tracking systems use doctoral information which is lagging by at least two weeks. InfluenzaNet relies on the voluntary disclosure of influenza-like symptoms from online users. 

Google Flu Trends and InfluenzaNet share the strength that neither requires individuals to physically report to a doctor to disclose useful data. As discussed in the "Ten-year performance of Influenzanet" article, there is considerable heterogeneity in the rate at which various populations seek medical help. For example, economically disadvantaged communities may be less likely to seek medical attention. However, it is exactly these populations that policy makers need information on because they may be more susceptible to the spread of flu in the first place.  While neither Google Flu Trends nor InfluenzaNet require users to visit a doctor, InfluenzaNet does require that users come to a decision that they are in fact sick to an extent that warrants some sort of deviation from normal behavior. Because using Google is ubiquitous in our daily life, there is next to no up-front cost for an internet user to make a simple flu-related query. It could be something as simple as searching for a pharmacy nearby to buy throat lozenges. This low barrier to entry is a particular strength of Google Flu trends. In contrast, trafficking InfluenzaNet is certainly not a daily activity. It requires an internal calculus greater than a simple web query but less than a full-blown doctor visit. 

Google Flu Trends and InfluenzaNet are also similar in that they are real-time. They are directly relying on real-time data from individuals that may be sick rather than receiving data through various reporting processes. Having the most up-to-date estimates is clearly advantageous but this real-time data may come at the cost of decreased accuracy. While traditional doctor-based reporting numbers are typically reported with a lag, the information when received should essentially be a direct computation of the number of individuals going to the doctor. Thus, for traditional measures the only source of measurement error is the degree to which going to the doctor reflects the underlying population's sickness. Google Flu Trends and InfluenzaNet are subject to estimation error and the degree to which they measure the true construct.

Relatedly, a potential drawback from Google Flu Trends and InfluenzaNet vis-a-vis traditional methods is that both are internet focused. Isolated or economically disadvantaged communities may not have internet connection. This could mean that neither user base is representative of the broader population. I see this as being less of an issue with Google because of how pervasive the internet is. However, InfluenzaNet operates purely on goodwill. If an individual goes to the doctor or makes a Google search they are seeking something in return, but InfluenzaNet is purely altruistic which could cause representativeness issues.

A final advantage of Google Flu Trends and Influenza Net is that both should operate at a drastically lower cost than a governmentally administered practice of reporting doctoral visits. Because the two products are administered online they should have low variable costs once established.

These strengths and weaknesses become more pronounced in event periods like the swine-flu outbreak. Because such outbreaks cause fear in the general population, usage of InfluenzaNet and Google Flu Trend results could fundamentally change. If the relationships between explanatory variables and flu estimates are not updated accordingly then large discrepancies in estimates could arise. For example, search history will no doubt sky rocket if an outbreak is feared and worried individuals may become very warry of any signs of sickness, causing changes in InfluenzaNet behavior. Thus, the traditional methods will be less error prone. However, if an outbreak is threatening, then the delay of the traditional methods may be unacceptable. Real-time estimates may be incredibly valuable in the face of a rapidly developing contagion. Hopefully, when used in consortium the various strengths and weaknesses of the three methods can offset.  



