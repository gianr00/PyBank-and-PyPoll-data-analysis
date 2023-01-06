# -----------------------------------------------------------------------------------
# PyBank - Python script that analyzes the company’s financial records. 
#
# Input file in csv format: 
#  - Financial data with two columns ("Date" and "Profit/Losses")
#
# Output file in txt format: 
#  - Budget summary over the entire period with the following information:
#    1. Total number of months included in the input data
#    2. Net total amount of "Profit/Losses" 
#    3. Average changes in "Profit/Losses"
#    4. Greatest increase in profits (date and amount)
#    5. Greatest decrease in profits (date and amount)
#
# Input file location/filename : PyBank/Resources/budget_data.csv
# Output file location/filename: PyBank/analysis/budget_summary.txt
# 
# Revision History:
#   Name                Date            Version
#   Rosie Gianan        2022-07-02      Initial version
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Import the necessary dependencies for os.path.join()
# -----------------------------------------------------------------------------------
import os
import csv

# -----------------------------------------------------------------------------------
# Define function(s)
# -----------------------------------------------------------------------------------

# Get the total of all numbers in list
def total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Get the list of date and profit_losses from the csv input file
def get_date_profit_losses():
    
    # Create the input file path
    in_csv_path_budget_data = os.path.join("Resources", "budget_data.csv")

    # Open and read each row of data in the .csv file
    with open(in_csv_path_budget_data) as in_csv_file:
        in_csv_reader = csv.reader(in_csv_file, delimiter=",")
        
        # Read and save the header row (skip this part if there is no header)
        in_csv_header = next(in_csv_file)
        
        # Initialize the lists to store the "Date" (colum 1 in input file) and 
        # "Profit/Losses" (column 2 in input file) 
        date_list = []
        profit_losses_list = []
        
        # Initialize the dictionary to store the date and profit_losses 
        date_profit_losses_dict = {}
        
        # Read and save each row of data after the header
        for row in in_csv_reader:
                
            # Save the "Date" to a list
            date_list.append(row[0])
                    
            # Save the "Profit/Losses" to a list. Convert the data to float since it will
            # be used in calculation
            profit_losses_list.append(float(row[1]))
    
    # Save the date and profit_losses to the dictionary
    date_profit_losses_dict["date"] = date_list
    date_profit_losses_dict["profit_losses"] = profit_losses_list
    
    # return the list of date and profit_losses saved in the dictionary            
    return date_profit_losses_dict

# Get the date for the profit_losses 
def get_date_for_profit_losses(the_index, date_list):
    the_date = ""

    # Loop through each item in the date_list and save the date that matches the index
    for index, item in enumerate(date_list):
        
        # Save the date for the profit_losses 
        if index == the_index:
            the_date = item
            break
    return the_date

# Calculate the the following values for the entire period:
# - Greatest increase in profits 
# - Greatest decrease in profits
# - Total change in profit and losses 
def calculate_average_max_min(date_list, profit_losses_list):
    
    # define a dictionary to store the result
    average_min_max = {}
      
    # define the variables for the max and min profit_losses and its index
    max_profit_losses = 0
    min_profit_losses = 0
    max_index = 0
    min_index = 0
    
    # define the varibles needed to calculate the total change in profit_losses
    prev_profit = 0
    curr_profit = 0
    ctr_month_change = 0
    total_change_profit_losses = 0

    # Loop through the profit_losses saved in a list and perform the following:
    # - calculate the monthly change in profit_losses
    # - calculate the total monthly change in profit_losses 
    # - find the max and min profit_losses and its index number
    for index, each_item in enumerate(profit_losses_list):
        
        if index == 0:
            # Set the counter for the month with changes to zero since 
            # there is no change of profit_losses on the first month
            ctr_month_change = 0
        else:
            # Accumulate the counter for month with changes
            ctr_month_change += 1   
            
            # Get the prev and curr profit using the list index 
            ctr = 0
            
            for item in (profit_losses_list[(index - 1) : (index + 1)]):
                ctr += 1
                if ctr == 1:
                    prev_profit = item
                else:
                    curr_profit = item
        
        # Calculate the monthly change in profit_losses        
        change_profit_losses = curr_profit - prev_profit
        
        # Add the monthly change in profit_losses to the total change in profit_losses
        total_change_profit_losses += change_profit_losses
        
        # Save the greatest increase in profit_losses and the index number. 
        # The index number will be used to get the date of max profit_losses
        if change_profit_losses > max_profit_losses:
            max_profit_losses = change_profit_losses
            max_index = index
        
        # Save the greatest decrease in profit_losses and the index number. 
        # The index number will be used to get the date of min profit_losses
        if change_profit_losses < min_profit_losses:    
            min_profit_losses = change_profit_losses
            min_index = index
              
    # ================================================================================
    # Calculate and save the average changes in "Profit/Losses" over the entire period
    # ================================================================================
    average_min_max["average"] = total_change_profit_losses / (ctr_month_change)
    
    # ================================================================================
    # Save the max profit_losses (date and amount)
    # ================================================================================
    # get the max_date
    the_date = get_date_for_profit_losses(max_index, date_list)
    
    # Save the max profit_losses (date and amount), format the amount to currency with 
    # no decimal places 
    average_min_max["max"] = f'{the_date} ({"${:.0f}".format(max_profit_losses)})'
    
    # ================================================================================
    # Save the min profit_losses (date and amount)
    # ================================================================================
    # get the min_date
    the_date = get_date_for_profit_losses(min_index, date_list)
    
    # Save the min profit_losses (date and amount), format the amount to currency with 
    # no decimal places  
    average_min_max["min"] = f'{the_date} ({"${:.0f}".format(min_profit_losses)})'

    # return the stats saved in the dictionary
    return average_min_max        

# Create the analysis result list 
def create_result_list(date_list, profit_losses_list):
    
    # Initialize the list to store the budget data analysis summary
    result_list = []        

    # Create and save the header
    result_list.append("Financial Analysis")
    result_list.append("----------------------------")

    # Calculate and save the number of months included in the dataset
    result_list.append(f"Total Months: {len(date_list)}")

    # Calculate and save the net total amount of "Profit/Losses" over the entire 
    # Format the value in $nnnnnnnn
    result_list.append(f'Total: {"${:.0f}".format(total(profit_losses_list))}')

    # Get the average, max and min profit_losses (date and amount)
    average_min_max = calculate_average_max_min(date_list, profit_losses_list)

    # Save the average change of profit_losses. Format to currency with 2 decimal places 
    result_list.append(f'Average Change: { "${:.2f}".format(average_min_max.get("average")) }')

    # Save the date and amount of the greatest increase 
    result_list.append(f'Greatest Increase in Profits: {average_min_max.get("max")}')

    # Save the value and date of the greatest decrease 
    result_list.append(f'Greatest Decrease in Profits: {average_min_max.get("min")}')
    
    # return the result list
    return result_list

# Write and print the output of the data analysis result
def write_print_output(result_list):
    
    # Create the output file path for the budget summary txt file
    out_txt_path_budget_summary = os.path.join("analysis", "budget_summary.txt")

    # Loop through the result list and write each result to text file and print to terminal
    with open(out_txt_path_budget_summary, "w") as out_txt_file:
        
        for each_item in result_list:
            
            # Write the budget summary to the text file, append "\n" to write to next line
            out_txt_file.write(each_item + "\n")
            
            # Print the budget summary to the Terminal
            print(each_item)
                
# -----------------------------------------------------------------------------------
# Main processing logic
# -----------------------------------------------------------------------------------

# Get the list of date and profit_losses from the csv input file
date_profit_losses_dict = get_date_profit_losses()
date_list = date_profit_losses_dict.get("date")
profit_losses_list = date_profit_losses_dict.get("profit_losses")

# Perform data analysis and save result to a list
result_list = create_result_list(date_list, profit_losses_list)     

# Write and print the output of the data analysis result
write_print_output(result_list)

# -----------------------------------------------------------------------------------
# End of code
# -----------------------------------------------------------------------------------