# Function to calculate the total sum of all sales values
def calculate_daily_sales(sales):
    return sum(sales)

# Function to apply a discount to each sale in the list
# :param discount: a decimal representing percentage (e.g., 0.1 = 10%)
def apply_discount(sales, discount=0.1):
    return [round(sale * (1 - discount), 2) for sale in sales]

# Function to filter out sales that fall below the threshold value
# :param threshold: the minimum sale value to be considered
def filter_sales(sales, threshold=100):
    return [sale for sale in sales if sale >= threshold]

# Main execution block: only runs if this file is executed directly
if __name__ == "__main__":

    # Sample list of sales values
    sample_sales = [50, 100, 200, 75, 150]

    # Filter out sales below $100
    filtered = filter_sales(sample_sales, threshold=100)

    # Apply a 20% discount to the filtered sales
    discounted = apply_discount(filtered, discount=0.2)

    # Display results to the user
    print("Filtered Sales:", filtered)
    print("Discounted Sales:", discounted)
    print("Total Discounted Sales:", calculate_daily_sales(discounted))

