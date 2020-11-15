import csv

def printext(linex, fp):
   print(linex, file=fp)
   print(linex)
   
with open("C:\\Projects\KUDABC\HW\\3\PyBank\Resources\pybank.csv", 'r') as file:
   reader = csv.reader(file)
   monthCount = 0
   totalPL = 0
   totaldiff = 0
   greatestinc = 0
   greatestincMonth=""
   greatestdec = 0
   greatestdecMonth=""
   prevPL = 0
   prevMonth = ""
   rowcount = 0
   for each_row in reader:
       rowcount = rowcount +1
       if rowcount == 1:
          continue
       monthCount = monthCount + 1

       totalPL = totalPL + int(each_row[1])
       if rowcount > 2:
           diff = float(each_row[1]) - prevPL
           totaldiff = totaldiff + diff
           if rowcount == 3:
               greatestinc = diff
               greatestdec = diff
               greatestincMonth=each_row[0]
               greatestdecMonth=each_row[0]
           if diff > greatestinc:
               greatestinc = diff
               greatestincMonth=each_row[0]
           if diff < greatestdec:
               greatestdec = diff
               greatestdecMonth=each_row[0]
       prevPL = float(each_row[1])
       prevMonth = each_row[0]

   fp = open("C:\\Projects\KUDABC\HW\\3\PyBank\Analysis\Analysis.txt", "w")
   printext("Financial Analysis", fp)
   printext("------------------------------", fp)
   printext("Total Months: " + str(monthCount),fp)
   printext("Total: $" + str(totalPL), fp)
   printext("Average Change: $" + str(format(totaldiff/(monthCount - 1),".2f")), fp)
   printext("Greatest Increase in Profits: " + greatestincMonth + " " + "($" + str(round(greatestinc)) + ")", fp)
   printext("Greatest Decrease in Profits: " + greatestdecMonth + " " + "($" + str(round(greatestdec)) + ")", fp)

