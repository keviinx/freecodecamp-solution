class Category:

    # initialize
    def __init__(self, category):
        # set the category
        self.category = category
        # init the ledger as empty list
        self.ledger = []

    # accepts an amount and description.
    # If no description is given, it should default to an empty spring.
    def deposit(self, amount, description = ""):
        # Should append an object to the ledger list in the form of {"amount": amount, "description": description}.
        self.ledger.append({"amount": amount, "description": description})

    # similar to deposit method, but the amount passed in should be stored in the ledger as a negative number.
    def withdraw(self, amount, description = ""):
        # If there are not enough funds, nothing should be added to the ledger.
        withdrawal_took_place = False
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            # This method should return True if the withdrawal took place, and False otherwise.
            withdrawal_took_place = True
        return withdrawal_took_place

    # method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
        # loop through to get the sum of amount
        return sum(i["amount"] for i in self.ledger)

    # method that accepts an amount and another budget category as arguments.
    def transfer(self, amount, budget_category):
        transfer_took_place = False
        # If there are not enough funds, nothing should be added to either ledgers.
        if self.check_funds(amount):
            # The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
            self.withdraw(amount, "Transfer to " + budget_category.category.capitalize())
            # The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
            budget_category.deposit(amount, "Transfer from " + self.category.capitalize())
            # This method should return True if the transfer took place, and False otherwise.
            transfer_took_place = True
        return transfer_took_place

    # method that accepts an amount as an argument.
    # This method should be used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        # It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
        amount_is_lesser = True
        if amount > self.get_balance():
            amount_is_lesser = False
        return amount_is_lesser

    # budget object is printed based on README requirement
    def __str__(self):
        # A title line of 30 characters where the name of the category is centered in a line of `*` characters.
        output = self.category.center(30, "*") + "\n"
        # A list of the items in the ledger. 
        # Each line should show the description and amount. 
        for item in self.ledger:
            # The first 23 characters of the description should be displayed, then the amount. 
            description = item["description"][:23].ljust(23)
            # The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
            amount = f'{item["amount"]:7.2f}'
            output += f'{description + amount}\n'
        output += f'Total: {self.get_balance()}'
        return output

# Besides the `Category` class, create a function (outside of the class) called `create_spend_chart` that takes a list of categories as an argument. 
# It should return a string that is a bar chart.

# Each category name should be written vertically below the bar. 

def create_spend_chart(categories):
# There should be a title at the top that says "Percentage spent by category".
    output = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        # Down the left side of the chart should be labels 0 - 100.
        # first empty space if not 100
        first_empty_space = " " if i != 100 else ""
        # second empty space if 0
        second_empty_space = " " if i == 0 else ""
        output += first_empty_space + second_empty_space + str(i) + "|"
        # The chart should show the percentage spent in each category passed in to the function. 
        # The percentage spent should be calculated only with withdrawals and not with deposits.
        total_spending = sum(category.ledger[0]["amount"] - category.get_balance() for category in categories)
        # loop to print the bars
        for category in categories:
            # only the first category has 1 space, others have 2 spaces
            number_of_spaces = 1 if category is categories[0] else 2
            output += number_of_spaces * " "
            spending = category.ledger[0]["amount"] - category.get_balance()
            # The "bars" in the bar chart should be made out of the "o" character.
            # The height of each bar should be rounded down to the nearest 10.
            output += "o" if (round(spending/total_spending, 2) * 100 >= i) else " "

        output += 2 * " " + "\n"
    # The horizontal line below the bars should go two spaces past the final bar.
    output += (4 * " ") + (((len(categories) * 3) + 1) * "-")
    # get the longest name in categories
    category_name_height = max(len(category.category) for category in categories)
    for j in range(category_name_height):
        # newline at the beginning
        output += "\n"
        # 2 spaces at the beginning of the line
        for category in categories:
            # only the first category has 5 spaces, others have 2
            number_of_spaces = 5 if category is categories[0] else 2
            # set the alphabet if not longer than the category name
            alphabet = category.category[j] if len(category.category) > j else " "
            output += number_of_spaces * " " + alphabet
        # two extra spaces at the end
        output += 2 * " "
    return output
