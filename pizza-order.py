print("Welcome To Python Pizza Order Delivery")

size = input(print("What size of pizza do you want? S, M or L: "))
add_pepperoni = input(print("Do you want pepperoni? Y or N: "))
extra_cheese = input(print("Do you want extra cheese? Y or N: "))
bill = 0

if size == "S":
  bill +=15
  if add_pepperoni == "Y":
    bill += 2
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
elif size == "L":
  bill += 25
  if add_pepperoni == "Y":
    bill += 3
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is ${bill}")
