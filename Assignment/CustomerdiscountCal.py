print("Welcome to Grace world!")

customer_name = input("Enter your name: ")
customer_status = int(input("Enter your current status \nNew customer: 1 \nExisting Customer: 2 \nStaff of Grace world: 3 \n"))
discount_tenpercent = float(0.10)
discount_fivepercent = float(0.05)
discount_fifteenpercent = float(0.15)
discount_threepercent = float(0.03)

if customer_status == 1:
    print("Okay " + customer_name + " you're a New Customer.")
    total_purchased_power = float(input("What is the total amount of your purchased goods?: "))
    
    if total_purchased_power > 50000: 
        discounted_value = total_purchased_power * discount_fifteenpercent
        payable_value = total_purchased_power - discounted_value
        print(f"You've earned 15%, you're to pay the sum of {payable_value} off on your purchase as a New Customer.")
    else: 
        discounted_value = total_purchased_power * discount_tenpercent
        payable_value = total_purchased_power - discounted_value
        print(f"Congratulations! You have 10% as a new customer, you can pay the sum of {payable_value} off your total purchase.")
        
elif customer_status == 2:
    print("Okay " + customer_name + " you're an Existing Customer.")
    total_purchased_power = float(input("What is the total amount of your purchased goods?: "))
    
    if total_purchased_power > 50000: 
        discounted_value = total_purchased_power * discount_tenpercent
        payable_value = total_purchased_power - discounted_value
        print(f"You've earned 10%, you're to pay the sum of {payable_value} off on your purchase as an Existing Customer.")
    else:
        discounted_value = total_purchased_power * discount_threepercent
        payable_value = total_purchased_power - discounted_value
        print(f"Congratulations! You have 3%, and you're to pay the sum of {payable_value} off your total purchase.")

elif customer_status == 3:
    print("Okay " + customer_name + " you're a staff of Grace world.")
    total_purchased_power = float(input("What is the total amount of your purchased goods?: "))
    
    discounted_value = total_purchased_power * discount_fivepercent
    payable_value = total_purchased_power - discounted_value
    print(f"You've earned 5%, you're to pay the sum of {payable_value} off on your purchase as a staff of Grace world.")
else:
    print("You need to enter a valid status.")
