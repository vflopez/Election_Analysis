# The data we need to retreive.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidata won
# 5. The winner of the election based on popular vote

# Load modules
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize vote accumulator
total_votes = 0
# Initialize the candidate list
candidate_options = []

# Open the election results and read the file
with open(file_to_load) as election_data:

     # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read header row.
    headers = next(file_reader)

    # Increment total_vote by 1 for each row in file
    for row in file_reader:
        # 2. Add to total vote count.
        total_votes += 1

        # Get the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
             candidate_options.append(candidate_name)

# Print the candidate names
print(candidate_options)

# 3. Print the total votes.
print(total_votes)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write('Counties in the Election\n')
     txt_file.write('-------------------------\n')
     txt_file.write("Arapahoe\nDenver\nJefferson")
