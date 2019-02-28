import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("select * from loan;", conn)
df.info()

bad_loan = ["Charged Off", "Default", "Does not meet the credit policy. Status:Charged Off", "In Grace Period", 
            "Late (16-30 days)", "Late (31-120 days)"]


df['loan_condition'] = np.nan

def loan_condition(status):
    if status in bad_loan:
        return 'Bad Loan'
    else:
        return 'Good Loan'
    
##Creating Column with either loan as Bad Loan or Good Loan
df['loan_condition'] = df['loan_status'].apply(loan_condition)
df.info()

df.to_sql("loan_analysed", conn)