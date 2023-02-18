
import os
import csv

#Joining path
budget_data = os.path.join("budget_data.csv")
#Saving file to a path
data_save = os.path.join("analysis.txt")

#Open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    #Calculating net total amount of profit and loss
    PL = []
    months = []

    #Reading through the rows.
    for rows in csvreader:
        PL.append(int(rows[1]))
        months.append(rows[0])

    #Calculating the revenue change
    revenue_change = []

    for x in range(1, len(PL)):
        revenue_change.append((int(PL[x]) - int(PL[x-1])))
    
    #Calculating avr revenue change.
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    #Calculating total number of months
    total_months = len(months)

    #Calculating greatest increase in revenue
    greatest_increase = max(revenue_change)
    #Calculating greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print the Results.
    with open(data_save, "w") as txt_file:
         financial_analysis = (
        	f"\nFinancial Analysis\n"
                f"...............................................................\n"
	        f"Total Months: {total_months:,}\n"
                f"Total:  $ {sum(PL):}\n"
                f"Average change: $ {revenue_average:.2f}\n"
                f"Greatest Increase in Profits:  {months[revenue_change.index(max(revenue_change))+1]} (${greatest_increase:})\n"
                f"Greatest Decrease in Profits:  {months[revenue_change.index(min(revenue_change))+1]} (${greatest_decrease:})\n")
         print(financial_analysis)
         txt_file.write(financial_analysis)

  
