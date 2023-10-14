#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Welcome to the tip calculator")
Bill = input("What is the price of the bill = $")
a=float(Bill)
Tip = input("What % of tip you want to give? 10 12 0r 15 = ")
e=int(Tip)
People = input("How many people will split the bill = ")
b=float(People)
tip_calculate = e / 100 * a + a
c = float(tip_calculate)
price = c / b
d = float(price)

final_amount = (round(d,2))
final_amount = "{:.2f}".format(d)
print(f"Each person should pay {final_amount}")