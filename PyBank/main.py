import pandas as pd

df = pd.read_csv('budget_data.csv',index_col=0,parse_dates=True)            

# TOTAL NUMBER OF MONTHS
total_months  = len(df)


# NET PROFIT AND LOSS
net_profit_loss = sum(df["Profit/Losses"])


# AVERAGE MONTHLY CHANGE
monthly_change = df['Profit/Losses'] - df['Profit/Losses'].shift(1)
monthly_change.dropna(inplace=True)
avg_monthly_change = round(sum(monthly_change)/len(monthly_change),2)


# Shifting one down and subtracting to get the monthly changes >> using for max_change and min_change
monthly_change_df = df - df.shift(1)

# MAX Change

# Finding the index of the max change
max_change = monthly_change_df.iloc[monthly_change_df['Profit/Losses'].argmax()]
# Assigning the date and max_change values to a variable
date, max_change = max_change.name, max_change.iloc[0]
# DateTime/Timestamp formatting to a string (https://www.programiz.com/python-programming/datetime/strftime)
max_date = date.strftime("%b-%Y")
# Converting a float to an integer
max_change = int(max_change)
# Printing the final result


# MIN Change
# Finding the index of the min change
min_change = monthly_change_df.iloc[monthly_change_df['Profit/Losses'].argmin()]
# Assigning the date and min_change values to a variable
date, min_change = min_change.name, min_change.iloc[0]
# DateTime/Timestamp formatting to a string (https://www.programiz.com/python-programming/datetime/strftime)
min_date = date.strftime("%b-%Y")
# Converting a float to an integer
min_change = int(min_change)
# Printing the final result


# Printing Results
print("Financial Analysis\n\n----------------------------\n")
print(f"Total Months: {total_months}")
print()
print(f"Total: ${net_profit_loss:,.0f}")
print()
print(f"Average Change: ${avg_monthly_change}")
print()
print(f"Greatest Increase in Profits: {max_date} (${max_change})")
print()
print(f"Greatest Decrease in Profits: {min_date} (${min_change})")

# RESULTS

line0 = "Financial Analysis\n\n----------------------------\n"
line1 = f"Total Months: {total_months}\n"
line2 = f"Total: ${net_profit_loss:,.0f}\n"
line3 = f"Average Change: ${avg_monthly_change}\n"
line4 = f"Greatest Increase in Profits: {max_date} (${max_change})\n"
line5 = f"Greatest Decrease in Profits: {min_date} (${min_change})\n"

results  = f"""{line0}\n{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n"""
with open('results.txt','w') as f:
    f.write(results)
    f.close()
