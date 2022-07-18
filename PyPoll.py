#PyPoll 

import csv
import os
# Assign a variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save a different file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Initialize candidate options as a separate list we can manipulate
candidate_options = []

# Initialize a dictionary for candidates and their votes
candidate_votes = {}

# Initialize variables to store the winner, winning count, and the winning percentage
winning_candidate = ""
winning_count = 0 
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row with the next function
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # Objective 1. Total votes cast
        # Add to the total_votes each loop (one vote per row)
        total_votes += 1

        # Objective 2. Candidate list who rec'd votes
        # Capture candidate name and put into list
        candidate_name = row[2]
        
        #Append the name only if it is a unique name not already in the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Objective 3.1 Count the votes per candidate
            # As you gather a list of names for Objective 2, create a new key for each of them with a zero vote count
            candidate_votes[candidate_name] = 0
        
        # Objective 3.2 Count the votes per candidate
        #for each row, add a vote (value) to the candidate_votes dictionary
        candidate_votes[candidate_name] += 1

# Print the things to the terminal that we want to put in our writing file to make sure they work
#print(f"Total votes: {total_votes:,}")
#print(candidate_options)
#print(candidate_votes)

# Objective 4. Percent of votes per candidate
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/ float(total_votes)*100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Objective 5. The winner based on popular vote
    # If the current vote count and vote percent are the hightest so far, then assign them to the winner variables
    if votes>winning_count and vote_percentage>winning_percentage:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

#print(f"The winner is {winning_candidate} with {votes:,} votes, comprising {winning_percentage:.1f}% of the vote")
    
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    
    # Write three counties to the file.
     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")