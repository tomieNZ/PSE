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
# Then, we need to calculate the tax amount based on the tax rate and the gross pay pre year
# we loop through the tax rate dictionary to find the current tax rate
# we use the current tax rate to calculate the tax amount
# Finally, we can get the net pay after tax
def calculate_gross_pay_after_tax(hours_worked, hourly_rate):
    # Calculate the gross pay pre year
    gross_pay_pre_year = hours_worked * hourly_rate
    current_tax_rate = 0.0
    # Loop through the tax rate dictionary to find the current tax rate
    for tax_bracket in tax_rate.keys():
        # If the gross pay pre year is in the current tax bracket, set the current tax rate
        if gross_pay_pre_year > tax_bracket[0] and gross_pay_pre_year <= tax_bracket[1]:
            # Attention: tax_rate is a dictionary, so we need to use a temporary variable to store the tax rate
            current_tax_rate = tax_rate[tax_bracket]
            break
    # Calculate the tax amount based on the tax rate and the gross pay pre year
    tax_amount = gross_pay_pre_year * current_tax_rate / 100
    # Calculate the net pay after tax
    net_pay = gross_pay_pre_year - tax_amount
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