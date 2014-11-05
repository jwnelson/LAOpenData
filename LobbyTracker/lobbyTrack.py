#!/usr/bin/python
import numpy as np
import matplotlib as matplot

# lobbyTrack.py
#
# 

### PARAMETERS ###
PAYMENTS_MADE_FILE = "CEC_-_Payments_Made_by_Clients_to_Registered_Lobbying_Firms.csv"
REGISTERED_LOBBYISTS_FILE = "CEC_-_Registered_Lobbyists.csv"
LOBBYIST_CLIENTS_FILE = "CEC_-_Clients_of_Registered_Lobbying_Firms.csv"
TEST_FILE = "testcsv.csv"

# Loads data from a csv file into a vertical (row-wise) numpy table
#
# Good for loading large csv files
# Handles ValueError issues where the lists don't match in size by simply snipping off the end
# of the line to match the length of the first line, so MAKE SURE THE FIRST LINE OF DATA IS OF
# THE CORRECT SIZE
def load_csv_dat(infile):
    
    f = open(infile, 'r')
    firstLine = f.readline()
    firstLine = firstLine.rstrip('\n')
    firstLine = firstLine.split(',')

    lineCount = 1
    lineLen = len(firstLine)

    datArray = np.array(firstLine)
    print datArray
    
    
    for line in f:
        line = line.rstrip('\n')
        line = line.split(',')
        
        try:
            datArray = np.vstack((datArray,line))
            lineCount = lineCount + 1
            #print datArray
        except ValueError:
            filepoint = f.tell()
            
            print "Found improper formatting at line %i" %lineCount
            print "Snipping end of line to match the rest of the data\n"
            line = line[0:lineLen]
            datArray = np.vstack((datArray,line))
            

    
    return datArray


### MAIN ###
#testData = load_csv_dat(TEST_FILE)
paymentsData = load_csv_dat(PAYMENTS_MADE_FILE)
lobbyistsData = load_csv_dat(REGISTERED_LOBBYISTS_FILE)
clientsData = load_csv_dat(LOBBYIST_CLIENTS_FILE)

print "\nPayments Data:\n",paymentsData
print "\nLobbyists Data:\n", lobbyistsData
print "\nClients Data:\n", clientsData


