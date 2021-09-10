calculation_to_units = 24
name_of_units = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


user_input = input("Hey user, enter the number of days and I will convert it to hours\n")
user_input_number = int(user_input)
print(days_to_units(user_input_number))


## This is from branch name rebase
## This is the second commit from rebase
