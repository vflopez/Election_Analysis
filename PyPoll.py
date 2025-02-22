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

# Initialize vote accumulator
total_votes = 0
# Initialize the candidate list
candidate_options = []
# Initialize the candidate votes dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

     # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read header row.
    headers = next(file_reader)

    # Increment total_vote by 1 for each row in file
    for row in file_reader:
        # Add to total vote count.
        total_votes += 1

        # Get the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
          candidate_options.append(candidate_name)
          # Begin tracking the candidate's votes
          candidate_votes[candidate_name] = 0
       
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

     election_results = (
          f"\nElection Results\n"
          f"---------------------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"---------------------------------------\n")
     print(election_results, end="")
     # Save the final vote count to the text file.
     txt_file.write(election_results)
     
     # Calculate the percentage of votes for each candidate
     for candidate_name in candidate_options:
          # Get the votes for the candidate
          votes = candidate_votes[candidate_name]
          # Calculate the percentage of votes
          vote_percentage = float(votes) / float(total_votes) * 100
          # Print the candidate name and percentage of votes
          candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          # Print each candidate, their voter count, and percentage to the terminal.
          print(candidate_results)
          #  Save the candidate results to our text file.
          txt_file.write(candidate_results)

          # Determine winning vote count and candidate
          # Determine if the votes is greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If true then set winning_count = votes and winning_percent =
               # vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # And, set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate_name
     
     # Compile the winning candidate infomation for display
     winning_candidate_summary =(
          f"---------------------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"---------------------------------------\n")
     print(winning_candidate_summary)
     txt_file.write(winning_candidate_summary)
 
