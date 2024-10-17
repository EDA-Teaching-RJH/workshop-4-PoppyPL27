drinks = ["Tea", "Coffee", "Hot chocolate"]
prices = [30, 75, 80]
amount_due = 0

print("welcome to the coffee machine. the drinks we have vailable today are: ")
for x in range(len(drinks)):
    print(drinks[x] + " - " + str(prices[x]) + "p")

choice = input("what drink would you like? ")
for x in range(len(drinks)):
    if choice == drinks[x]:
        amount_due = prices[x]

extra_shot = input("would you like to add an extra shot for 20p? ")
if extra_shot == "yes":
    amount_due = amount_due + 20

while amount_due > 0:
    print("you have " + str(amount_due) + "p left to pay")
    coin = int(input("please insert a coin: "))
    if coin == 5 or coin == 10 or coin == 20 or coin == 50:
        amount_due = amount_due - coin

change = amount_due * -1
print("full amount paid. you are owed " + str(change) + "p change")

