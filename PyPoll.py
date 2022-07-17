#PyPoll 

import csv
import os
# Assign a variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save a different file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze data here. 

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
     #   print(row)

    # Objectives
    # 1. Total votes cast
    # 2. List of candididates who rec'd votes
    # 3. Count of votes per candidate
    # 4. Percent of votes per candidate
    # 5. The winner based on popular vote

    print(election_data)


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    
    # Write three counties to the file.
     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")