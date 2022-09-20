print("Welcome to the tip calculator.")
bill = float(input("What was the total bill ?: "))
num_people = int(input("How may people to split the bill ?: "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15 ?: "))
#amount each person is calculated
each_person_pay = round((bill + ((tip / 100) * bill)) / num_people, 2)
print(f"Each person should pay: {each_person_pay}")