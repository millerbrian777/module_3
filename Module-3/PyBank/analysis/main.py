import os
import csv

dirname = os.path.dirname(__file__)
budget_csv= os.path.join(dirname, "..", "Resources", "budget_data.csv")

# with open(budget_csv) as csv_file:
#     csvreader = csv.reader(csv_file,delimiter= ',')
with open(budget_csv, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  
    data = [row for row in csvreader]    
    # print(next(csvreader))

#  print total number of months
    total_months = len(data)


# net total amount of profit/loss
    net_profit_loss = sum(int(row[1]) for row in data)
    print(net_profit_loss)


# change in profot and loss over the period and avg in the changes

profit_losses_changes = [int(data[i][1]) - int(data[i-1][1]) for i in range(1, len(data))]

average_change = sum(profit_losses_changes) / len(profit_losses_changes)

# Find the greatest increase in profits 
max_increase_index = profit_losses_changes.index(max(profit_losses_changes)) + 1
max_increase_date = data[max_increase_index][0]
max_increase_amount = max(profit_losses_changes)

# Find the greatst decrease in profit
max_decrease_index = profit_losses_changes.index(min(profit_losses_changes)) + 1
max_decrease_date = data[max_decrease_index][0]
max_decrease_amount = min(profit_losses_changes)

# Print the results
print("finacial Anaylsis")
print('---------------------------')
print("Total Months:", total_months)
print("Net Total Profit/Losses:", net_profit_loss)
print("Average Change in Profit/Losses:  ${:.2f}".format(average_change))
print("Greatest Increase in Profits:", max_increase_date, "($", max_increase_amount, ")")
print("Greatest Decrease in Profits:", max_decrease_date, "($", max_decrease_amount, ")")