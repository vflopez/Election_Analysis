# Election_Analysis

## Project Overview
The Election Commission has provided us with a file of the election data, and asked us to report the results of the election.  

To this end, we will  analyze and summarize the data in the file and provide the following:

- The total number of votes cast
- A list of all the counties with the percentage and total number of votes cast in each county
- The name of the county with the largest turnout
- The percentage and total votes for each candidate
- The winning candidate and the total votes and percentage of votes cast for them

## Resources
- Data source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.47.3

## Election Results
The analysis of the election data shows that:
- There were <b>369,711</b> votes cast in the election.
- <b>Turnout by County:</b>
  - Jefferson county had 10.5% or 38,855 votes.
  - Denver county had 82.8% or 306,055 votes.
  - Arapahoe county had 6.7% or 24,801 votes.
  
 - <b>Denver</b> county had the largest turnout.
 
- <b>Candidate Results:</b>
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
    
- <b>Overall Results:</b>
    - Election Winner: Diana DeGette
    - Winning Vote Count: 272,892
    - Winning Percentage: 73.8%

## Analysis of Methodology
  ### File Processing
- The data was provided in a flat csv (comma delimited) file.  
- In order to read and analyze the data, We imported 2 Python modules: <b>os</b> and <b>csv</b>.  
- The <b>csv</b> module makes reading and writing files possible. 
- The <b>os</b> module facilitates using the local file system.

This is how we used these modules to read and write the files:
```
# Add our dependencies.
import csv
import os
...
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
...
# Read and skip the header
    header = next(reader)
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
...
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    ...
    txt_file.write(election_results)
```
  ### Variable Use - Lists and Dictionaries
  - Python Lists are used to gather the candidate and county names.
  - Python Dictionaries are used to accumulate the totals for each candidate or county.
```
# Candidate list and candidate votes dictionary.
candidate_options = []
candidate_votes = {}

# Create a county list and county votes dictionary.
counties = []
county_votes = {}
...
    # For each row in the CSV file.
    for row in reader:
    ...
        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county = row[1]
        
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if county not in counties:

            # 4b: Add the existing county to the list of counties.
            counties.append(county)

            # 4c: Begin tracking the county's vote count.
            county_votes[county] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county] += 1
```

  ## Summary
The script used for this election is fast and accurate.  It can easlily be adapted to any type of election.  For a primary election, with a subsequent run-off election, it can be modified to find the top <b><i>n</i></b> number of candidates to be enterd in the run-off.  It can also be altered to process election results by Congressional District for House elections.  This solution, with minor adjusments, will answer all of your election data processing needs.
