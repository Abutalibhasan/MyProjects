"""
Program: camper_age_input.py
Author: Abutalib
Last date modified: 06/03/2020



The purpose of this program is to accept the age on years and
convert to months.
"""
def convert_to_months(years):
    months =  years*12
    return months
if __name__ == '__main__':
 age_in_months = input("Enter your age in years:")
 age_in_years = convert_to_months(int(age_in_months))
 print("your age in years =", age_in_months)
 print("your age in months =", age_in_years)

# Input   Expected Output
#    5              12
#    7              84

