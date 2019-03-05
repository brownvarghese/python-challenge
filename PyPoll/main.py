#                  ELECTION RESULT ANALYSIS
# LIBRARIES
import os
import csv
from operator import itemgetter
import operator
import io

# WORKING STORAGE 

total_votes = int
total_votes = 0
candidate_vote = int
candidate_vote = 0
candidate_name = str
candidate_name_list = []
candidate_vote_list = []
election_result = {}
election_result_sorted = {}


filler = '------------------------------------'
header = '       ELECTION RESULTS             '
winner = str


# OPEN AND READ FILE
with open("Resources/election_data.csv"):
  reader = csv.DictReader(open("Resources/election_data.csv"))


#SORT RECORDS BASED ON CANDIDATE'S NAME
sorted_poll = sorted(reader, key=itemgetter("Candidate"))

# LOOP THRU THE RECORDS
# WHEN CANDIDATE NAME CHANGES, MOVE THE CANDIADTE NAME AND NUMBER OF VOTES TO SEPRATE LISTS  
for row in sorted_poll:
#    print(row)
    Candidate = (row["Candidate"])
    Voter_Id = (int(row["Voter ID"]))
    County = (row["County"])
    
    total_votes = total_votes + 1

    if total_votes > 1:
        if candidate_name != Candidate:
            candidate_name_list.append(candidate_name) 
            candidate_vote_list.append(candidate_vote)
          #  print(candidate_name_list)
          #  print(candidate_vote_list)
            candidate_name = Candidate
            candidate_vote = 1
        else:
            candidate_vote = candidate_vote + 1
    else:
        candidate_vote = 1
        candidate_name = Candidate

candidate_name_list.append(candidate_name)
candidate_vote_list.append(candidate_vote) 
#print(candidate_name_list)
#print(candidate_vote_list)
#print("Total Votes   " + str(total_votes))

# ZIP CANDIDATE LIST AND VOTE LIST INTO DICTIONARY ELECTION RESULT
election_result = dict(zip(candidate_name_list,candidate_vote_list ))
#print(election_result)

# SORT THE RECORDS, SO THAT THE LAST LAST KEY VALUE PAIR IS THE WINNER 
election_result_sorted = dict(sorted(election_result.items(), key=lambda x: x[1], reverse=False))
#print(election_result_sorted)
for key, value in election_result_sorted.items():
  winner = key
  
# SORT THE RECORDS AGAIN BASED ON THE VOTES CASTED, TO PREPARE THE SUMMARY 
election_result_sorted = dict(sorted(election_result.items(), key=lambda x: x[1], reverse=True))
#print(election_result_sorted)

# WRITE RESULTS TO TEXT FILE
with io.open("output_file.txt", mode='w', encoding='utf-8') as f:
  result_string = header
  f.write(result_string) 
  f.write("\n")
  print(result_string)
  result_string = ' '

  result_string = filler
  f.write(result_string)
  f.write("\n")
  print(result_string)
  result_string = ' '


  result_string = "Total Votes:  " + str(total_votes)
  f.write(result_string)
  f.write("\n")
  print(result_string)
  result_string = ' '

  result_string = filler
  f.write(result_string)
  f.write("\n")
  print(result_string)
  result_string = ' '

  for key, value in election_result_sorted.items():
  #  print (key, value)
    out_name = key
    out_votes = value
    out_percentage = "{:.3%}".format(out_votes/total_votes)

    result_string = key + '  :  ' + str(out_percentage) + '  ' + '('+ str(out_votes)+')'
    print(result_string)


    f.write(result_string)
    f.write("\n")
    result_string = ' '
  #print(winner)
  result_string = "Winner:  " + winner
  print(result_string)
  f.write(result_string)
f.close()






