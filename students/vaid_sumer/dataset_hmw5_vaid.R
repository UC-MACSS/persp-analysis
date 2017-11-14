library(ggplot2) #loads ggplot2 package

#I am examining a dataset about diversity in silicon valley firms. The dataset is called "Silicon Valley Diversity Data" on Kaggle.

data<-read.csv("siliconvalley.csv") #reads in data
data_airbnb<-data[data$company == "Airbnb",] #subsets data for AirBnB

data_latino<-data_airbnb[data_airbnb$race == "Latino",] #subsets Latino data from all AirBnB data
data_latino$count<-as.numeric(as.character(data_latino$count)) #converts factors to numbers 

plot1<-ggplot(data_latino, aes(x=job_category, y=count))+geom_bar(stat="identity")+
  labs(title="What roles do Latinos Occupy at AirBnb?",x="Roles and Totals", y="No.of Latinos")+
  theme(axis.text.x=element_text(angle=45, hjust=1)) #plots the number of Latinos occupying different roles at AirBnB as a histogram. 

#As one can see, the majority of Latinos occupy a professional position at AirBnb. 
#It is also worth noting that the number of Latinos has increased from the previous year, as evidenced by a lower previous_totals bar as compared to totals. 
