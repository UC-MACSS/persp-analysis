## What is the Goal of the Competition

[The Kaggle Contest I decided to look into](https://www.kaggle.com/c/web-traffic-time-series-forecasting) was a Web Traffic Time Series Forecasting challenge. The challenge specifcally was to forecast the future web traffic of approximately 145,000 Wikipedia articles, based on past observations of Wikipedia page views. 

 The winners of the contest were announced November 12th 2017. 


## What Do You Have to Do to Make a Submission

* To participate in Kaggle competitions you need to be over 18 years old, have a registered Kaggle account, and not a resident of Crimea, Cuba, Iran, Syria, North Korea, or Sudan.

* Submissions are evaluated on SMAPE between forecasts and actual values. Lower SMAPE scores are better (ie. SMAPE = 0 when the actual and predicted values are both 0.)

* To participate in this challenge teams need to accept the compeition rules by September 1st 2017, and submit their final project by September 12th 2017. 

* The contest has two stages. The first stage involves is a training stage in which teams meausure on historical data (Wikipedia page views from January, 1st, 2017 up until March 1st, 2017), and second stage where participants need to score future data (daily Wikipedia page views between September 13th, 2017 and November 13th, 2017). Teams can use any method to predict the data, though most teams will use some type of state-of-the-art machine learning algorithms. The winner will be decided by who can forecast the page views of each Wikipedia article most accurately. 

* To enter the contest, you need to predict web traffic for each article and day combination. Submit this via a .csv file.