import math

class Category:
    def __init__(self, name: str):
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description="") -> bool:
        if not self.check_funds(amount):
            return False
        self.deposit(-amount, description)
        return True

    def get_balance(self) -> int:
        return sum(entry["amount"] for entry in self.ledger)

    def transfer(self, amount: float, destination: 'Category') -> bool:
        w_successful = self.withdraw(amount, f"Transfer to {destination.name}")
        if not w_successful:
            return False
        destination.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount: float) -> bool:
        return True if amount <= self.get_balance() else False

    def __str__(self):
        return (
            self.name.center(30, "*")
            + "\n"
            + "\n".join(self._format_entry(entry) for entry in self.ledger)
            + f"\nTotal: {self.get_balance()}"
        )

    @staticmethod
    def _format_entry(entry: dict) -> str:
        return entry["description"].ljust(23, " ")[
            :23
        ] + f'{entry["amount"]:.2f}'.rjust(7, " ")

    def get_total_spent(self) -> float:
        return abs(sum(v for entry in self.ledger if (v := entry["amount"]) < 0))


def create_spend_chart(categories: list[Category]) -> str:
    spent_per_category = [c.get_total_spent() for c in categories]
    total_spent = sum(spent_per_category)
    percentages = [math.floor(s/total_spent*10)*10 for s in spent_per_category]
    bar_char = 'o'

    chart_lines = ["Percentage spent by category"]

    # bars
    for y_value in range(100, -1, -10):
        line = str(y_value).rjust(3,' ')+'| '
        for p in percentages:
            line += f'{bar_char}  ' if p >= y_value else ' '*3
        chart_lines.append(line)

    # x axis
    chart_lines.append(' '*4 + '-' * (len(categories)*3 + 1))

    # names
    names = [c.name.capitalize() for c in categories]
    max_len = max(len(n) for n in names)

    for i in range(max_len):
        line = ' '*5
        for name in names:
            line += f"{name[i] if len(name) > i else ' '}  "
        chart_lines.append(line)

    return '\n'.join(chart_lines)


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)
print(clothing)

food = Category("Food")
food.deposit(100)
food.withdraw(62)

clothing = Category("Clothing")
clothing.deposit(100)
clothing.withdraw(22)

auto = Category("Auto")
auto.deposit(100)
auto.withdraw(12)

print(create_spend_chart([food, clothing, auto]))

