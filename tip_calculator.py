# greet to the program
print("Welcome to the tip calculator!\n")

# capture user inputs as variables
total_bill = float(input("What was the total bill? $\n"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill? \n"))

# calculate how much each person is supposed to pay for the bill + tip
each_person_bill = round(((total_bill * (tip_percent/100)) / people) + total_bill / people, 2)

# print the amount each person should pay
print(f"Each person should pay $ {each_person_bill}.")

