import pandas as pd
import sqlite3
import matplotlib.pyplot as plot
import matplotlib.mlab as mlab
import matplotlib.dates as dates

conn = sqlite3.connect("database.sqlite")

'''
Select all rows which loan status is charged off from orginal data table
and consist of a new data table named charged_off_loan
'''
charged_off_loan = pd.read_sql_query("SELECT * From loan WHERE loan_status = 'Charged Off'",conn)

'''
Classify all charged off loans according to different loan purpose 
count the number loan records for each purpose and make the bar graph
'''
loan_purpose = charged_off_loan['purpose'].value_counts()
loan_purpose.plot("bar")
plot.xlabel("Loan purpose")
plot.ylabel("Count")
plot.title("The distribution of Charged-off-loan's loan purpose")
plot.show()

'''
Classify all charged off loans according to different loan grade 
count the number loan records for each grade and make the bar graph
'''
loan_grade = charged_off_loan['grade'].value_counts()
loan_grade.plot("bar")
plot.xlabel("Loan grade")
plot.ylabel("Count")
plot.title("The distribution of Charged-off-loan's loan grade")
plot.show()