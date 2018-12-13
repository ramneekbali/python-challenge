import os
import csv
from collections import Counter
budget_data = os.path.join('/Users/p2778494/UDEN201811DATA3/Week3/HW/Instructions/PyBank/Resources','budget_data.csv')

Months_list =[]
Budget_list=[]
print("Financial Analysis")
print("---------------------------------")

with open(budget_data,'r') as f:
    reader=csv.reader(f)
    next(reader)
    for(row)in reader:
        Months_list.append(row[0])

Total_Months=(len(Months_list))
print("Total_Months =",Total_Months)

with open(budget_data,'r') as f:
    reader=csv.reader(f)
    next(reader)
    for (row)in reader:
        Budget_list.append(row[1])

Total_list = [int(column) for column  in Budget_list]
Total = sum(Total_list)
print("Total =","$",Total)

change=list(zip(Total_list,Total_list[1:]))
monthly_change=[x[1]-x[0] for x in change]
average_change=sum(monthly_change)/len(monthly_change)
print("Average change:","$",round(average_change,2))

Profit_increase=max(monthly_change)
Profit_increase_month=Months_list[monthly_change.index(max(monthly_change))+1]
print("Greatest Increase in Profits:",Profit_increase_month,"($",Profit_increase,")")

Profit_decrease=min(monthly_change)
Profit_decrease_month=Months_list[monthly_change.index(min(monthly_change))+1]
print("Greatest Decrease in Profits:",Profit_decrease_month,"($",Profit_decrease,")")


output_file = os.path.join("output_bank.csv")
output=open("output_bank.csv", "w")
print("Financial Analysis",file=output)
print("---------------------------------",file=output)
print("Total_Months =",Total_Months,file=output)
print("Total =","$",Total,file=output)
print("Average change:","$",round(average_change,2),file=output)
print("Greatest Increase in Profits:",Profit_increase_month,"($",Profit_increase,")",file=output)
print("Greatest Decrease in Profits:",Profit_decrease_month,"($",Profit_decrease,")",file=output)
