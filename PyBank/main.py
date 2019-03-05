# Modules
import os
import csv
from operator import itemgetter
import operator
import io

rec_count = 0
current_value = 0
current_date = " "
incoming_value = int
change_in_profit_loss = int
incoming_value = int 
total_change_in_profit_loss = int 
total_change_in_profit_loss = 0
net_profit_loss = int
net_profit_loss = 0
header = '        Financial Analysis          ' 
filler = '------------------------------------'

# Set path for file
Budget_Data = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(Budget_Data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        incoming_value = row[1]
        incoming_date  = row[0]

        if rec_count > 1:
            rec_count = rec_count + 1  

            change_in_profit_loss = int(incoming_value) - current_value
        #    print(change_in_profit_loss)
            total_change_in_profit_loss = total_change_in_profit_loss + change_in_profit_loss 
        #    print(str(total_change_in_profit_loss))

            if  greatest_gain       < change_in_profit_loss:
        #        print("greatest_gain :   " + str(greatest_gain))
        #        print("change_in_profit_loss   :  " + str(change_in_profit_loss))
                greatest_gain       = change_in_profit_loss
                greatest_gain_mmyy  = incoming_date

            if  greatest_loss        > change_in_profit_loss:
                greatest_loss        = change_in_profit_loss
                greatest_loss_mmyy   = incoming_date
            
            current_value = int(incoming_value)
            net_profit_loss = net_profit_loss + current_value
            

        elif rec_count == 1:
            rec_count = rec_count + 1

            current_date  = incoming_date
            current_value = int(incoming_value)

            net_profit_loss = current_value

        #    greatest_gain = current_value
            greatest_gain = 0
            greatest_gain_mmyy = current_date
        #    greatest_loss = current_value
            greatest_loss = 0    
            greatest_loss_mmyy = current_date



        else:
            rec_count = rec_count + 1
        
    average_change_in_profit_loss = (total_change_in_profit_loss / (rec_count-2))



with io.open("output_file.txt", mode='w', encoding='utf-8') as f:
    result_string = header
    f.write(result_string)
    f.write("\n")
    print(result_string)
    result_string = ' '

    result_string = filler
    f.write(result_string)
    f.write("\n")
    print(result_string)
    result_string = ' '

    result_string = "Total Months: " + str(rec_count-1)
    f.write(result_string)
    f.write("\n")
    print(result_string)
    result_string = ' '

    result_string = "Total: " + str(net_profit_loss)
    f.write(result_string)
    f.write("\n")
    print(result_string)
    result_string = ' '

    amountAsFormattedString = '${:,.2f}'.format(average_change_in_profit_loss)
    result_string = "Average  Change: " + str(amountAsFormattedString)
    f.write(result_string)
    f.write("\n")
    print(result_string)
    result_string = ' '
    amountAsFormattedString = ' '

    amountAsFormattedString = '${:,.0f}'.format(greatest_gain)
    result_string = "Greatest Increase in Profits : " + greatest_gain_mmyy + " " + str(amountAsFormattedString)
    f.write(result_string)
    f.write("\n")
    print(result_string)
    result_string = ' '


    amountAsFormattedString = '${:,.0f}'.format(greatest_loss)
    result_string = "Greatest Decrease in Profits : " + greatest_loss_mmyy + " " + str(amountAsFormattedString)
    f.write(result_string)
    f.write("\n")
    print(result_string)
    result_string = ' '





    


