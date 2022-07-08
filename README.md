# python-challenge
Module 3 Challenge – Python Homework:  Py Me Up, Charlie

Objective:

This project will apply the Python scripting skills learned in Module 3 – Python Scripting. This will apply the skills on reading and writing files, using variables, iterating through lists and dictionaries and creating functions.  This project will also develop the testing and debugging skills. The project results will be uploaded to GitHub to develop the skills in project versioning.

Project Details:
This project includes two challenges using Python scripting. 
-    PyBank - Analyze the company’s financial records and create a budget summary
-    PyPoll – Analyze a rural town election data and create the election result summary

1.    PyBank 

Analyze the company’s financial records using Python script.  The input is the financial data in csv format with two columns ("Date" and "Profit/Losses")

The output will be printed to the terminal and written to a text file. The output includes the budget summary over the entire period with the following information:

-    Total number of months included in the input data
-    Net total amount of "Profit/Losses" 
-    Average changes in "Profit/Losses"
-    Greatest increase in profits (date and amount)
-    Greatest decrease in profits (date and amount)

Input and Output files:
-    Input file location/filename : PyBank/Resources/budget_data.csv
-    Output file location/filename: PyBank/analysis/budget_summary.txt

The Python scripts reads each record from the csv file and saves it into two lists (date and profit/losses). Using the data saved in the lists, it performs the following to get the budget summary for the entire period:

-    Count the number of months saved in date list
-    Calculates the net total profit/losses saved in profit/losses list 
-    Calculate the monthly change in profit/losses and get the average monthly changes in profit/losses 
-    Find the greatest increase in profits/losses and the greatest decrease in profits/losses
-    Find the date for  the greatest increase in profits/losses and greatest decrease in profits/losses

2.    PyPoll

Analyze a rural town election data using Python script. The input is the poll data in csv format 
with three columns ("Ballot ID", "County", and "Candidate")

The output will be printed to the terminal and written to a text file. The output includes the election result summary with the following information:

-    Total number of votes cast
-    Complete list of candidates who received votes
-    Percentage of votes each candidate won
-    Total number of votes each candidate won
-    Winner of the election based on popular vote

Input and Output files:
-    Input file location : PyPoll/Resources/election_data.csv
-    Output file location: PyPoll/analysis/election_summary.txt

The Python scripts reads each record from the csv file and saves the “Candidate” column into a list. Using the data saved in the candidate list, it performs the following to get the election summary:

-    Count the total number of votes cast 
-    Create a unique list of candidates saved in the “candidate list”. For each candidate in the unique list, it calculates the total votes cast and the percentage of votes cast
-    Find the candidate with the greatest votes cast


Project Submission:
The following folders/files will be uploaded to GitHub repository called “python-challenge”. A shareable link of the GitHub repository will be submitted to bootcamp spot site.

1.    PyBank folder including the following:
-    File named “main.py” – the PyBank python script 
-    Folder named “analysis” – contains the budget summary text file and the screenshot of the result printed in the terminal
-    Folder named “Resources” – contains the input csv files used 

2.    PyPoll folder including the following:
-    File named “main.py” – the PyPoll python script 
-    Folder named “analysis” – contains the election summary result text file and the screenshot of the result printed in the terminal
-    Folder named “Resources” – contains the input csv files used 

3.    README.md file
