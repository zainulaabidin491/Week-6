
# Constants for prices
CEMENT_PRICE = 3
GRAVEL_PRICE = 2
SAND_PRICE = 2
SPECIAL_PACK_PRICE = 10

def check_sack(contents, weight):
    """
    Check the contents and weight of a single sack.
    
    Args:
    contents (str): The contents of the sack (C, G, or S).
    weight (float): The weight of the sack in kilograms.
    
    Returns:
    bool: True if the sack is accepted, False otherwise.
    str: The reason for rejection, or an empty string if accepted.
    """
    if contents not in ['C', 'G', 'S']:
        return False, "Invalid contents"
    
    if contents == 'C' and (weight < 24.9 or weight > 25.1):
        return False, "Cement weight is incorrect"
    elif (contents == 'G' or contents == 'S') and (weight < 49.9 or weight > 50.1):
        return False, "Gravel/Sand weight is incorrect"
    
    return True, ""

def check_order(num_cement, num_gravel, num_sand):
    """
    Check a customer's order for delivery.
    
    Args:
    num_cement (int): The number of sacks of cement required.
    num_gravel (int): The number of sacks of gravel required.
    num_sand (int): The number of sacks of sand required.
    
    Returns:
    float: The total weight of the order.
    int: The number of sacks rejected from the order.
    """
    total_weight = 0
    rejected_sacks = 0
    
    for _ in range(num_cement):
        contents = 'C'
        weight = float(input("Enter weight of cement sack: "))
        accepted, reason = check_sack(contents, weight)
        if accepted:
            total_weight += weight
        else:
            rejected_sacks += 1
            print(f"Cement sack rejected: {reason}")
    
    for _ in range(num_gravel):
        contents = 'G'
        weight = float(input("Enter weight of gravel sack: "))
        accepted, reason = check_sack(contents, weight)
        if accepted:
            total_weight += weight
        else:
            rejected_sacks += 1
            print(f"Gravel sack rejected: {reason}")
    
    for _ in range(num_sand):
        contents = 'S'
        weight = float(input("Enter weight of sand sack: "))
        accepted, reason = check_sack(contents, weight)
        if accepted:
            total_weight += weight
        else:
            rejected_sacks += 1
            print(f"Sand sack rejected: {reason}")
    
    return total_weight, rejected_sacks

def calculate_price(num_cement, num_gravel, num_sand):
    """
    Calculate the price for a customer's order.
    
    Args:
    num_cement (int): The number of sacks of cement required.
    num_gravel (int): The number of sacks of gravel required.
    num_sand (int): The number of sacks of sand required.
    
    Returns:
    float: The regular price for the order.
    float: The new price for the order after discounts.
    float: The amount saved.
    """
    regular_price = num_cement * CEMENT_PRICE + num_gravel * GRAVEL_PRICE + num_sand * SAND_PRICE
    
    special_packs = min(num_cement, num_sand // 2, num_gravel // 2)
    discount = special_packs * (CEMENT_PRICE + 2 * GRAVEL_PRICE + 2 * SAND_PRICE - SPECIAL_PACK_PRICE)
    
    new_price = regular_price - discount
    amount_saved = regular_price - new_price
    
    return regular_price, new_price, amount_saved

# Main program
num_cement = int(input("Enter number of sacks of cement required: "))
num_gravel = int(input("Enter number of sacks of gravel required: "))
num_sand = int(input("Enter number of sacks of sand required: "))

total_weight, rejected_sacks = check_order(num_cement, num_gravel, num_sand)
print(f"Total weight of order: {total_weight} kg")
print(f"Number of sacks rejected: {rejected_sacks}")

regular_price, new_price, amount_saved = calculate_price(num_cement, num_gravel, num_sand)
print(f"Regular price: ${regular_price:.2f}")
print(f"New price after discounts: ${new_price:.2f}")
print(f"Amount saved: ${amount_saved:.2f}")