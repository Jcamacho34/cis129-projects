# Lab 5: The Bottle Return Program

# Author: Jorge Camacho
# Date: March 27, 2024
# Description: The program counts the number of bottles over 7 days and calculates the total amount and 							total payout. The program asks the user if they want to continue or not.

# Step 1: Declare variables below 
total_bottles = 0
today_bottles = 0
counter = 0
total_payout = 0
keep_going = 'y'
	
   #While loop to run program again
while keep_going == 'y':
      	# code to set value of variable totalBottles 
	total_bottles = 0
	counter = 1
	while counter <= 7: #While loop for each day of the week
		today_bottles = int(input("Enter number of bottles returned for day #" + str(counter) + ": "))
		total_bottles += today_bottles
		counter += 1
      	# code to set value of variable totalPayout
	total_payout = total_bottles * 0.10
       # code to print the number of total bottles and total payout
	print("The total number of bottles collected is ",)
	print("The total paid out is $","{:.1f}".format(total_payout))
		
	print("Do you want to enter another week’s worth of data?")
	print("(Enter y or n)")
	keep_going = input()

