 
import csv
import os

# Joining path
election_data_file = os.path.join("election_data.csv")
#Saving file to a path
data_save = os.path.join("analysis.txt")

#Initializing a total vote counter. 
total_votes = 0

# Candidate Options
candidate_options = []

#Declaring  dictionary
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Opening the file 
with open(election_data_file) as csvfile: 
    csv_reader = csv.reader(csvfile)
    csv_headers = next(csvfile)
    
    #Reading through rows   
    for row in csv_reader:
        #Count total votes.
        total_votes += 1

        #Print the candidate name from each row. 
        candidate_name = row[2]
 
        if candidate_name not in candidate_options: 
            #Add the name to the list of candidates. 
            candidate_options.append(candidate_name)
            #start to count the candidates vote count. 
            candidate_votes[candidate_name] = 0
        
        #Add a vote to the candidate's vote count. 
        candidate_votes[candidate_name] += 1

#Save the results to the text file. 
with open(data_save, "w") as txt_file: 
    #Print the final vote count. 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file. 
    txt_file.write(election_results)

    for candidate_name in candidate_votes: 
        #Getting vote count 
        votes = candidate_votes[candidate_name]
        #Percentage of votes. 
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes:,})\n")
        #Print the results. 
        print(candidate_results)
        #Save the results to the text file. 
        txt_file.write(candidate_results)
     

        #Determine winning candidate. 
        if (votes > winning_count) and (vote_percentage > winning_percentage): 
            
            winning_count = votes
            winning_percentage = vote_percentage
            
            winning_candidate = candidate_name

       #print winning candidate. 
            winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------\n")
    print(winning_candidate_summary)
    #Save the results to the text file. 
    txt_file.write(winning_candidate_summary)
    
