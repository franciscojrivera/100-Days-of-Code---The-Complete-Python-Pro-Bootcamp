def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


#print(format_name(input("What is your first name?"), input("What is your last name?")))


def is_leap_year(year):
    # Write your code here.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

is_leap_year(2020)