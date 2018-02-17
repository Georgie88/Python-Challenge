#dependencies
import csv

#determine the file name
file_name = 'election_data_2.csv'

#creating an empty dictionary for the candidates
candidates = {}
#starting a counter to count all votes
votes_count = 0
#initializing a counter for storing maximum number of votes per candidate
max_votes_candidate = 0
    
#open a file
with open(file_name, newline='') as csvfile:
#read the  file with csv
    election_data = csv.reader(csvfile, delimiter=',')
    #skip the first line    
    next(election_data)
    
    #looping through each row in the table
    for row in election_data :
        #determine the total number of votes
        votes_count += 1
        #storing a value in candidate per iteration for row[2]
        candidate_name = row[2]
        #check for condition
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

#open file to write results to file
Results = open('Election_Result_2.txt', 'w')
    
#Print the header string
print("Election Results" + '\n'
      + "-------------------------" + '\n'
      + "Total Votes: " + str(votes_count) + '\n'
      + "-------------------------")
#print result to file
Results.write("Election Results" + '\n'
              + "-------------------------" + '\n'
              + "Total Votes: " + str(votes_count) + '\n'
              + "-------------------------")

for  candidate_name in candidates.keys() :
    count_of_votes = candidates[candidate_name]
         
    #calculating the percentage and rounding of thr result to 2 places of decimal
    percentage = round((count_of_votes/votes_count)*100.00,2)
    #print the result 
    print (candidate_name + (": ") + str(percentage) +  ("% (")  + str(count_of_votes) + ")")
    #print result to file
    Results.write(candidate_name + (": ") + str(percentage) +  ("% (")  + str(count_of_votes) + ")")
    #check for condition to find out winner by finding the max votes
    if count_of_votes > max_votes_candidate :
        max_votes_candidate = count_of_votes
        winner = candidate_name
print("-------------------------" + '\n'
        + "Winner: "+ winner + '\n'
        + "-------------------------")
#print result to file
Results.write("-------------------------" + '\n'
                + "Winner: "+ winner + '\n'
                + "-------------------------")