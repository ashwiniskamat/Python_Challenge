import csv
def printext(linex, fp):
       print(linex, file=fp)
       print(linex)

with open("C:\\Projects\KUDABC\HW\\3\PyPoll\Resources\pypoll.csv", 'r') as file:
   reader = csv.reader(file)
   candidate = []
   votes = []
   totalvotes = 0
   rowcandidate = ""

   for each_row in reader:
       totalvotes = totalvotes + 1
       if totalvotes == 1:
           continue
       rowcandidate = each_row[2]
       rowx = -1
       for ix in range(0,len(candidate)):
           if candidate[ix] == rowcandidate:
               rowx = ix
               break
       if rowx == -1:
           candidate.append(rowcandidate)
           votes.append(1)
       else:
           votes[ix] = votes[ix] + 1

   fp = open("C:\\Projects\KUDABC\HW\\3\\PyPoll\Analysis\Analysis.txt", "w")
   printext("Election Results", fp)
   printext("----------------------", fp)
   printext("Total Votes: " + str(totalvotes), fp)
   printext("----------------------", fp)
   ix = -1
   winnervotes = 0
   winnercandidate = ""
   for cx in candidate:
       ix = ix + 1
       if winnervotes < votes[ix]:
           winnervotes = votes[ix]
           winnercandidate = candidate[ix]
       printext(
           candidate[ix] + " " + str(format(votes[ix] * 100 / totalvotes, ".3f")) + "%" + " (" + str(votes[ix]) + ")",
           fp)
   printext("----------------------", fp)
   printext("Winner: " + winnercandidate, fp)
   printext("----------------------", fp)
   fp.close()