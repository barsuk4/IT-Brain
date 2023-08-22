class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} грн. додано на рахунок"
        else:
            return "Сума для поповнення повинна бути позитивною"

    def withdraw(self, amount):
        if amount > self.balance:
            return "На рахунку недостатньо коштів"
        elif amount <= 0:
            return "Сума для зняття повинна бути позитивною"
        else:
            self.balance -= amount
            return f"{amount} грн. знято з рахунку"

    def __str__(self):
        return f"Власник рахунку: {self.owner}\nБаланс: {self.balance} грн."

# Тестування
account = BankAccount("Олександр", 500)
print(account)

print(account.deposit(150))
print(account.withdraw(50))
print(account.withdraw(700))

print(account)  # Щоб побачити зміни на рахунку
