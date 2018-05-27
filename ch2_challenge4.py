#car salesman program

base_price = int(input("Price of car: "))

tax = base_price * 0.15
car_license = base_price * 0.05
dealer_fee = int(500)
dest_charge = int(25)

total_price = base_price + tax + car_license + dealer_fee + dest_charge

print("The total price of the car will be",total_price)
