library(tidyr) # loads tidyr package
library(dplyr) # loads dplyr package
library(reshape2) #loads reshape2 package
library(reshape) #loads reshape package
library(outliers) #loads outliers package
library(ggplot2) #loads ggplot2 package
library(scales) #loads scales package
library(knitr) 
library(tools)

data<-read.csv("siliconvalley.csv")
data_airbnb<-data[data$company == "Airbnb",]
data_latino<-data.frame(data_airbnb[data_airbnb$race == "Latino",])
data_latino$count<-as.numeric(as.character(data_latino$count))

plot1<-ggplot(data_latino, aes(x=job_category, y=count))+geom_bar(stat="identity")+
  labs(title="What roles do Latinos Occupy at AirBnb?",x="Roles", y="No.of Latinos")+
  theme(axis.text.x=element_text(angle=45, hjust=1))