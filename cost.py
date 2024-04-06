def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price

def main():
    # Prompt user for input
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)

    # Display the final price
    if final_price == original_price:
        print(f"No discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"Discount applied. Final price after {discount_percent}% discount: ${final_price:.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
