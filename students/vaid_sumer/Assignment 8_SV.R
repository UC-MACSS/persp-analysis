library("dplyr")
library("ggfortify")
library("dendextend")



data<-read.csv("College.csv")
#perform PCA analysis on the college dataset and plot the first two principal components. Describe the results.

data.numeric<-select_if(data, is.numeric)
data.pca<-prcomp(data.numeric, center = TRUE, scale.=TRUE)
#plot the first tw principal components
plot<-biplot(data.pca)
plot<-autoplot(data.pca, loadings=TRUE, loadings.label=TRUE)
#Approximately how much of the variance in College is explained by 
#the first two principal components?



