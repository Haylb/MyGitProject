###########
# Course: COMP 1113 FA02, 2021
# Assignment 2
# Author: Hayden Breault
# Student ID: 100162560
# email address: 162560@acadiau.ca
# Date: 2021-09-26
# I certify that this code is my own and I have not broken any rules concerning Academic Dishonesty.
############

#count number of mild and major symptomes
mildSymptomes = 0
majorSymptomes = 0

name = input("What is your name: ").capitalize()

#print instructions to user
print("\nHello " + name + ". This program is a test to see if you should\ncome to class, stay home or book a test for COVID-19.\n")
print('Enter "y" for yes and "n" for no in your answers.')

#ask user if they have major symptoms first
q1 = input("Do you have a fever? (i.e., chills/sweats): ")
if q1 == "y":
    majorSymptomes = majorSymptomes + 1
    
q2 = input("Do you have a cough? (new or worsening): ")
if q2 == "y":
    majorSymptomes = majorSymptomes + 1

#for any answers that are not "y" or "n"
if q1 != "y" and q1 != "n" or q2 != "y" and q2 != "n":
    print("\n" + name + ", at least one of your inputs is invalid. Try again.")   

elif q1 == "y" or q2 == "y":
    print("\n" + name + ", you should stay home and call 811 to schedule a test.")
    print("You have " + str(majorSymptomes) + " major symptome(s) of COVID-19.")
    #if true, the program prints the aove and goes to line 75
    
else: #if q1 == "n" or q2 == "n" 

    #to get to this point, the user must have no major symptomes
    print("\nYou have " + str(majorSymptomes) + " major symptomes of COVID-19.")
    
    #ask user if they have minor symptomes
    q3 = input("Do you have a headache?: ")
    if q3 == "y":
        mildSymptomes = mildSymptomes + 1
    q4 = input("Do you have a sore throat?: ")
    if q4 == "y":
        mildSymptomes = mildSymptomes + 1
    q5 = input("Do you have a runny nose or nasal congestion?: ")
    if q5 == "y":
        mildSymptomes = mildSymptomes + 1
    q6 = input("Do you have shortness of breath?: ")
    if q6 == "y":
        mildSymptomes = mildSymptomes + 1
    
    #for any answers that are not "y" or "n"
    if q3 != "y" and q3 != "n" or q4 != "y" and q4 != "n" or q5 != "y" and q5 != "n" or q6 != "y" and q6 != "n":
        print("At least one of your inputs is invalid. Try again.")
    
    #if user has 4 minor symptomes, they should book a test
    elif q3 == "y" and q4 == "y" and q5 == "y" and q6 == "y":
        print("\n" + name + ", you should stay home and call 811 to schedule a test.")
        print("You have " + str(mildSymptomes) + " mild symptomes which is enough that you should book one.")
    
    #if user has 1-3 minor symptoms, they should stay home
    elif q3 == "y" or q4 == "y" or q5 == "y" or q6 == "y":
        print("\n" + name + ", you should stay home.")
        print("You have " + str(mildSymptomes) + " mild symptome(s).")
        
    else: #if q3 == "n" and q4 == "n" and q5 == "n" and q6 == "n"
        print("\n" + name + ", you can go to class as you have no symptomes.")

#always stated at the end
print("\nThank you for taking this test as you are keeping not only yourself, \nbut everyone else around you safe.")
        


