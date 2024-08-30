class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def check_funds(self,amount):
        return self.get_balance() >= amount

    def get_balance(self):
        return sum(i["amount"] for i in self.ledger)

    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def __str__(self):
        titleLine = f"{self.name.center(30,'*')}\n"
        items = "" 
        for i in self.ledger:
            amount = f"{i['amount']:.2f}"
            description = i['description'][:23]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return titleLine + items + total


def create_spend_chart(categories):
    text = "Percentage spent by category\n"
    chart = ""
    categorySpent = []
    totalSpent = 0

    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        totalSpent += spent
        categorySpent.append(spent)
    

    percentages = [(int((spent / totalSpent) * 100 // 10 * 10)) for spent in categorySpent]
    print(percentages)
    print(spent)
    print(totalSpent)
    print(categorySpent)
    for i in range(100,-1,-10):
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    maxLength = max(len(category.name) for category in categories)

    for i in range(maxLength):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += '\n'

    return text + chart.rstrip("\n")


# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(101.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")

# clothing = Category("Clothing")
# food.transfer(500, clothing)
# clothing.withdraw(500,"shoes")
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(150, "gas")

# categories = [food, clothing, auto]
# print((create_spend_chart(categories)))
