
require(ggthemes)
require(data.table)
require(dplyr, warn.conflicts = FALSE)
require(ggplot2)
require(tibble)
##Read data
data <- as_tibble(suppressWarnings(fread("/Users/Rex/Downloads/kaggle-survey-2017/multipleChoiceResponses.csv")))

data %>%
  filter(LanguageRecommendationSelect == "R" | LanguageRecommendationSelect == "Python") %>%
  group_by(CurrentJobTitleSelect, LanguageRecommendationSelect) %>%
  count() %>%
  ggplot(aes(CurrentJobTitleSelect, n, color = LanguageRecommendationSelect)) +
  ggtitle("Python vs. R used by Job Title") +
  labs(x = "Job Title", y = "Frequency") +
  geom_point(size = 4) +
  theme_solarized(light = FALSE) +
  scale_colour_solarized("red") +
  theme(
    axis.text.x = element_text(angle = 330, hjust = 0),
    axis.title.x = element_text(margin = margin(t = 12))
  )

