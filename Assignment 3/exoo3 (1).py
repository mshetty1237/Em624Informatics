print("\n Run by Mohit Shetty")

#Part 1:

import csv

with open("CitiBike-NYC-CitiBike-Jan_Feb2016.csv", 'r') as file1:
    r = csv.reader(file1, delimiter=',')
    n0 = -1   # count of total number of lines
    n1 = 0    # count of number of lines with customer
    n2 = 0    # count of number of lines with subscriber

    for row in r:
        if (n0 == -1):
            n0 = 0
            continue
        n0 += 1      #Calculates the total number of lines in the file

        if (row[13] == 'Customer'):
            n1 += 1        #Calculates the total number of customers in the file
        if (row[13] == 'Subscriber'):
            n2 += 1        #Calculates the total number of subscribers in the file
z1 = n1 / n0 * 100 #Formula to find percentage of customers.

with open("CitiBike-NYC-CitiBike-Jan_Feb2016.csv", 'r') as file1: #Opens and reads the file
    print("\n These are the last 5 lines in the file: ")
    for rows in (file1.readlines()[-5:]):
        print(rows, end=' ')  #printslast5lines
print("\n")

print('The file has', n0, 'lines.', n1, 'of them have "Customer" as usertype,', n2,
      'have "Subscriber" as usertype. Customer are', z1, '% of the total.') #Final output.

#Part 2:
lines=0

with open("NYC-CitiBike-Apr_May2016.csv", 'r') as file2:
    r = csv.reader(file2, delimiter=',')
    # initializing variable
    n3 = -1
    n4 = 0
    n5 = 0

    for row in r:
        if (n3 == -1):
            n3 = 0
            continue
        n3 += 1

        if (row[13] == 'Customer'):
            n4 += 1   #Calculates the total number of customers in the file
        if (row[13] == 'Subscirber'):
            n5 += 1   #Calculates the total number of subscribers in the file
z2 = n4 / n3 * 100 #percintage of customer2qa

with open("NYC-CitiBike-Apr_May2016.csv", 'r') as file2:  #openfile NYC-CitiBike-Apr_May2016.csv
    print("\n These are the first 5 lines in the file: ")  #printsfirst5lines
    next(file2)    #to skip the header
    for line in file2:
        print(line)
        lines += 1  # count lines in the file
        if lines == 5:
            break
print("\n")

print('The file has', n3, 'lines, of which', n4,'have "Customer" as usertype,',n5,'have "Subscriber" as usertype. Customer are',z2 ,'% of the total.')

if n0>n3:
    print("The first file is bigger than the second one.")
else:
    print("\n The first file is smaller than the second file.")
if z1>z2:
    print("The first file has relatively more customers than the second one.")
else:
    print("The first file has relatively less customers than the second file.")

#Part 3:
if n0 > n3:
    print("\nThe Winter riders are more than the Spring")

elif n0 <= n3:

    print("\nThe Spring riders are more than the Winter")

if z1 > z2:

    print("\nDuring the Winter there are more Customers/non-Subscribers than in the Spring")

elif z1 <= z2:

    print("\nDuring the Spring there are more Customers/non-Subscribers than in the Winter")