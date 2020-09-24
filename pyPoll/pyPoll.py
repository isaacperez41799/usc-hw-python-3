import csv
import os

#Reading resource folder
csvpath = os.path.join("Resources", "election_data.csv")
pathout = os.path.join("Resources", "Election Analysis")

#Listing Variables to use
votes = 0
winnerVotes = 0
totalCandidates = 0

#was confused how to label largest Votes, and made an array
greatestVotes = ["", o]
candidateOptions = []
candidateVotes{}

#Using as python function to open csv
with open(csvpath) as electionData:
    reader = csv.DictReader(electionData)

#Creating Loop to find canidateOptions
    for row in reader:
        votes = votes + 1
        totalCandidates = row["Candidate"]

        if row["Candiate not in candiateOptions"]:
            candidateOptions.append(row["Candidate"])
            candidateVotes[row["Candidate"]] = 1

        else 
            #Will loop if all else
            candidateVotes[row["Candidate"]] = candidatesVotes[row["Candidate"]] + 1

    #Printing to format like the example
    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
#results
    for candidate in candidateVotes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidateVotes[candidate]) + ")") 
        candidateResults = (candidate + " " + str(round(((candidateVotes[candidate]/votes)*100))) + "%" + " (" + str(candidateVotes[candidate]) + ")") 
    
candidateVotes

winner = sorted(candidateVotes.items(), key=itemgetter(1), reverse=True)

#Printing winner
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")


# Output Files
with open(pathout, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    #txt_file.write(candidate + " " + str(round(((candidateVotes[candidate]/votes)*100))) + "%" + " (" + str(candidateVotes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))
