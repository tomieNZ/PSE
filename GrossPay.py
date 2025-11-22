"""
This file is used to calculate the gross pay of a worker in NZ.
@author: Yaohui Zhang @tomie
"""

# Tax rate dictionary
# The key is a tuple of the tax bracket
# The value is the tax rate for net pay pre year
tax_rate = {
    (0, 15600): 10.5,
    (15601, 53500): 17.5,
    (53501, 78100): 30,
    (78101, 180000): 33,
    (180001, float('inf')): 39,
}

# Function to calculate the gross pay after tax
# The input is the hours worked and the hourly rate
# The first step is to calculate the gross pay (Be attention the tax rate is for net pay pre year)
# Then, we need to calculate the tax amount using progressive tax brackets
# Progressive tax means different portions of income are taxed at different rates
# For example: first $15,600 at 10.5%, next portion at 17.5%, and so on
# We loop through each tax bracket and calculate tax for the portion of income in that bracket
# Finally, we subtract the total tax from gross pay to get the net pay after tax
def calculate_gross_pay_after_tax(hours_worked, hourly_rate):
    # Calculate the gross pay pre year (total income before tax)
    gross_pay_pre_year = hours_worked * hourly_rate
    
    # Initialize total tax amount and previous threshold for progressive tax calculation
    total_tax = 0.0
    previous_threshold = 0
    
    # Sort tax brackets by minimum income to process from lowest to highest
    # This ensures we calculate tax progressively: lower income portions first
    sorted_brackets = sorted(tax_rate.items(), key=lambda x: x[0][0])
    
    # Loop through each tax bracket to calculate tax for the portion of income in that bracket
    for (min_income, max_income), rate in sorted_brackets:
        # If all income has been taxed, exit the loop
        if gross_pay_pre_year <= previous_threshold:
            break
        
        # Calculate the taxable amount in this bracket
        # It's the minimum of: (remaining income) or (income in this bracket)
        # For example: if income is $68,640 and we're in bracket $53,501-$78,100,
        # taxable amount = min($68,640, $78,100) - $53,500 = $15,140
        taxable_amount = min(gross_pay_pre_year, max_income) - previous_threshold
        
        # Only calculate tax if there's taxable income in this bracket
        if taxable_amount > 0:
            # Calculate tax for this portion: taxable amount × rate / 100 (rate is percentage)
            tax_in_bracket = taxable_amount * rate / 100
            # Add this bracket's tax to the total tax
            total_tax += tax_in_bracket
        
        # Update previous threshold to the end of current bracket for next iteration
        previous_threshold = max_income
    
    # Calculate the net pay after tax: gross pay minus total tax
    net_pay = gross_pay_pre_year - total_tax
    return net_pay

if __name__ == "__main__":
    # Test the function
    # 40 hours pre week, 33 dollars pre hour, 52 weeks pre year
    print("--------------------------------")
    print("\n The net pay after tax based on the tax rate is:\n")
    print("40 hours pre week, 33 dollars pre hour, 52 weeks pre year\n")
    print(calculate_gross_pay_after_tax(40*52, 33))
    print("\n")
    print("--------------------------------")