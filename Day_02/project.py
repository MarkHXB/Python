"""
Tip calculator
"""

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))
#my own derivation
bill_people = bill/people
tip_per_person = bill_people * (tip/100)
total_amount_of_tip_per_person = bill_people + tip_per_person
print(f"Each person should pay: ${float(round(total_amount_of_tip_per_person,2))}")

#Or
"""
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")
"""