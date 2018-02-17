#dependencies
import csv

#set file name
file_name = 'budget_data_1.csv'

#open a file
with open(file_name, newline='') as csvfile:
    #read the  file with csv
    budget_data = csv.reader(csvfile, delimiter=',')
    #skip the header row
    next(budget_data)
    
    #setting up the variables for the number of months, total revenue, average, greatest increase and decrease
    Total_Months = 0
    Total_Revenue = 0
    Revenue_Change = 0
    Total_Revenue_Change = 0
    Prev_Month_Revenue = 0
    Gretest_Revenue_Increase = 0
    Greatest_Revenue_IncMonth = "Date1"
    Gretest_Revenue_Decrease = 0
    Greatest_Revenue_DecMonth = "Date2"
    
    #looping through each row in the table
    for row in budget_data:
        #calculating the total months by incrementing the row count
        Total_Months += 1
        #calculate total revenue
        Total_Revenue += int(row[1])
        
        #excluding the first month as there will be no revenue change 
        if Prev_Month_Revenue != 0:
            #calculate revenue change for current month
            Revenue_Change = int(row[1])-Prev_Month_Revenue
            #calculate total revenue change
            Total_Revenue_Change = Total_Revenue_Change + abs(Revenue_Change)
            
            #comparing the current change in value to the previous greatest increase in revenue
            if Revenue_Change > Gretest_Revenue_Increase:
                #update the greatest increase in revenue to current month
                Gretest_Revenue_Increase = Revenue_Change
                Gretest_Revenue_IncMonth = row[0]
            
            #comparing the current change in value to the previous greatest decrease in revenue
            if Revenue_Change < Gretest_Revenue_Decrease:
                #update the greatest decrease in revenue to current month
                Gretest_Revenue_Decrease = Revenue_Change
                Gretest_Revenue_DecMonth = row[0]

        #assigning the value of current revenue to the variable for using it as previous revenue
        Prev_Month_Revenue=int(row[1])

        #calculating the average revenue change
        Average_Revenue_Change = round(Total_Revenue_Change/Total_Months,2)

#print to terminal all the solution
print("Financial Analysis" + '\n' 
      + "-------------------------" + '\n'
      + "Total Months: " + str(Total_Months) + '\n'
      + "Total Revenue: $" + str(Total_Revenue) + '\n'
      + "Average Revenue Change: $" + str(Average_Revenue_Change) + '\n'
      + "Greatest Increase in Revenue: " + Gretest_Revenue_IncMonth + ", $" + str(Gretest_Revenue_Increase) + '\n' 
      + "Greatest Decrease in Revenue: " + Gretest_Revenue_DecMonth + ", $" + str(Gretest_Revenue_Decrease))

#create output file
with open('Results_Budget_1.txt', 'w') as results_2:

    #creating the output
    results_2.write("Financial Analysis" + '\n' 
                    + "-------------------------" + '\n'
                    + "Total Months: " + str(Total_Months) + '\n'
                    + "Total Revenue: $" + str(Total_Revenue) + '\n'
                    + "Average Revenue Change: $" + str(Average_Revenue_Change) + '\n'
                    + "Greatest Increase in Revenue: " + Gretest_Revenue_IncMonth + ", $" + str(Gretest_Revenue_Increase) + '\n' 
                    + "Greatest Decrease in Revenue: " + Gretest_Revenue_DecMonth + ", $" + str(Gretest_Revenue_Decrease))