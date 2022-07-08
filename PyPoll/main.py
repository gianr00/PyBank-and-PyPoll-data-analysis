# -----------------------------------------------------------------------------------
# PyPoll - Python script that analyzes the election data.
#
# Input file in csv format: 
#  - Election data with three columns ("Ballot ID", "County", and "Candidate")
#
# Output file in txt format: 
# - Election analysis summary with the following information:
#   1. Total number of votes cast
#   2. Complete list of candidates who received votes
#   3. Percentage of votes each candidate won
#   4. Total number of votes each candidate won
#   5. Winner of the election based on popular vote
#
# Input file location : PyPoll/Resources/election_data.csv
# Output file location: PyPoll/analysis/election_summary.txt
# 
# Revision History:
#   Name                Date            Version
#   Rosie Gianan        2022-07-04      Initial version
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Import the necessary dependencies for os.path.join()
# -----------------------------------------------------------------------------------
import os
import csv

# -----------------------------------------------------------------------------------
# Define functions
# -----------------------------------------------------------------------------------

# Get the count of all items in list
def count(items):
    count = 0
    for each_item in items:
        count += 1
    return count

# Get the number of occurences of an item in a list
def count_item(items, the_item):
    count_item = 0
    for each_item in items:
        if each_item == the_item:
            count_item += 1
    return count_item

# Get the unique value in the list
def unique_list(all_list):      
    unique_list = []    
    for each_item in all_list:
        if each_item not in unique_list:
            unique_list.append(each_item)
    return unique_list

# Get the candidate list from the input csv file
def get_candidate_list():
    
    # Create the input file path
    in_csv_path_election_data = os.path.join("Resources", "election_data.csv")

    # Open and read each row of data in the .csv file
    with open(in_csv_path_election_data) as in_csv_file:
        
        in_csv_reader = csv.reader(in_csv_file, delimiter=",")
        
        # Read and save the header row (skip this part if there is no header)
        in_csv_header = next(in_csv_file)

        # Initialize the list to store the name of "Candidates" (column 3 in input file)
        candidate_list = []
        
        # Read and save each row of data after the header
        for row in in_csv_reader:
                    
            # Save the name of candidates to a list
            # Note: Per the input data, each entry in this list is one vote
            candidate_list.append((row[2]))
            
    return candidate_list

# Calculate percent votes and total votes each candidate won
def get_name_percent_count(candidate_list):
    
    # Get the complete list of candidates who received votes
    unique_candidate_list = unique_list(candidate_list)

    # Initialize the list to store the candidate name, percent votes and their total of votes won
    name_percent_count_list = []
    
    # Loop through the unique list of candidates and calculate each candidate's 
    # percent votes and number of votes won. 
    for candidate_name in unique_candidate_list:
        
        # Calculate the candidate's number of votes won
        candidate_votes = count_item(candidate_list, candidate_name)
        
        # Calculate the total number of votes cast
        total_votes_cast = count(candidate_list)
        
        # Calculate the percentage of votes. Format the value in percent with 3 decimal places
        percentage_votes = "{:.3f}%".format((candidate_votes/total_votes_cast) * 100 )
    
        # Save the candidate's name, percent votes and total votes won
        name_percent_count_list.append(f"{candidate_name}: {percentage_votes} ({candidate_votes})" )
        
    # return candidates list
    return name_percent_count_list
     
# Calculate percent votes and total votes each candidate won
def get_winner(candidate_list):
    
    # Get the complete list of candidates who received votes
    unique_candidate_list = unique_list(candidate_list)

    # Loop through the unique list of candidates and find the candidate with highest votes
    winner_total_votes = 0 
    winner_name = "" 
    
    for candidate_name in unique_candidate_list:
        
        # Calculate the candidate's number of votes won
        candidate_votes = count_item(candidate_list, candidate_name)
        
        # Save the winner's name 
        if candidate_votes > winner_total_votes:
            winner_name = candidate_name
            winner_total_votes = candidate_votes
            
    return winner_name    

# Perform data analysis and save the result to a list
def create_result_list(canditate_list):
    
    # Initialize the list to store the election data analysis summary
    result_list = []

    # Save election summary header 
    result_list.append("Election Results")
    result_list.append("-------------------------")

    # Calculate and save the total number of votes cast
    result_list.append(f"Total Votes: {count(candidate_list)}")
    result_list.append("-------------------------")

    # Get the candidate's name, percent votes and the total votes won
    name_percent_count_list = get_name_percent_count(candidate_list)
    
    # Save the candidate's name, percent votes and total votes won
    for each_item in name_percent_count_list:
        result_list.append(each_item)

    # Get the winner's name
    winner_name = get_winner(candidate_list)
    
    # Save the winner's name
    result_list.append("-------------------------")    
    result_list.append(f"Winner: {winner_name}")
    result_list.append("-------------------------")
    
    return result_list

# Create output: write to text file and print to terminal
def write_print_output(result_list):
    
    # Create the output file path for the election summary txt file
    out_txt_path_election_summary = os.path.join("analysis", "election_summary.txt")

    # Loop through the result list and write each result to text file and print to terminal
    with open(out_txt_path_election_summary, "w") as out_txt_file:
        
        for each_item in result_list:
            
            # Write the election summary to the text file, append "\n" to write to next line
            out_txt_file.write(each_item + "\n")
            
            # Print the election summary to the Terminal
            print(each_item)
            
# -----------------------------------------------------------------------------------
# Main processing logic
# -----------------------------------------------------------------------------------

# Get the candidate list from the input csv file
candidate_list = get_candidate_list()

# Perform data analysis and save result to a list
result_list = create_result_list(candidate_list)     

# Write and print the output of the data analysis result
write_print_output(result_list)
      
# -----------------------------------------------------------------------------------
# End of code
# -----------------------------------------------------------------------------------