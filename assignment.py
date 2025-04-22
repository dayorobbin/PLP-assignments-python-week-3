def calaculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent /100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
#Prompt user for input
original_price = float(input("Enter the discount price of the item:"))
discount_percentage = (float(input("Enter the discount percentange:")))

#Calculating final price
final_price = calaculate_discount(original_price, discount_percentage)

#Printing the result
if final_price != original_price:
    print(f"The final price after applying  the discount is: ${final_price}")
else:
    print(f"No discount applied. The original price is: ${original_price}")
