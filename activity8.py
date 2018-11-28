# William Ramm
# Activity 8 - Customer Class

import csv
from CustomerClass import Customer


#define main funtion
def main():
    customers = []
    #open customer csv file
    with open('customers.csv') as file:
        reader = csv.reader(file)
        custIDs = []
        line = 0
        #for each row in csv file, not including the first, append customer ids to custIDs list
        #and create/store Customer objects in customers list
        for row in reader:
            if(line > 0):
                custIDs.append(row[0])
                customers.append(Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            line = line + 1
    print('Customer Viewer')
    cont = 'y'
    custID = ''
    #while user enters 'y' to continue, promt for customer ID
    while cont == 'y':
        custIDInput = input('\nEnter customer ID: ')
        index = 0
        custIDMatch = False
        #search for cutomer id match in custIDs list
        for custID in custIDs:
            #if match is found, call method with corresponding object
            if custID == custIDInput:
                print('\n' + customers[index].getAddress())
                custIDMatch = True
                break
            index = index + 1
        #if no match is found, print the following
        if not custIDMatch:
            print('\nNo customer with that ID.')
        #Allow user to continue or not
        cont = input('\nContinue? (y/n): ')
    # if user does not enter 'y', print 'Bye!' and exit program
    print('\nBye!')


#call main funtion
main()