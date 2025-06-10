import datetime

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_price(self):
        return self.price * self.quantity

class Receipt:
    TAX_RATE = 0.18      # 18% tax
    DISCOUNT_RATE = 0.10 # 10% discount

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.total_price() for item in self.items)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.TAX_RATE

    def calculate_discount(self):
        return self.calculate_subtotal() * self.DISCOUNT_RATE

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        discount = self.calculate_discount()
        return subtotal + tax - discount

    def generate_receipt_text(self):
        lines = []
        lines.append("========== RECEIPT ==========")
        lines.append(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("-----------------------------")
        lines.append("{:<20} {:<10} {:<10} {:<10}".format("Item", "Price", "Qty", "Total"))

        for item in self.items:
            lines.append("{:<20} ₹{:<10.2f} {:<10} ₹{:<10.2f}".format(
                item.name, item.price, item.quantity, item.total_price()
            ))

        lines.append("-----------------------------")
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        discount = self.calculate_discount()
        total = self.calculate_total()

        lines.append(f"Subtotal:       ₹{subtotal:.2f}")
        lines.append(f"Tax (18%):      ₹{tax:.2f}")
        lines.append(f"Discount (10%): ₹{discount:.2f}")
        lines.append(f"TOTAL:          ₹{total:.2f}")
        lines.append("=============================")
        return "\n".join(lines)

    def save_receipt_to_file(self, filename="receipt.txt"):
        with open(filename, "w") as file:
            file.write(self.generate_receipt_text())
        print(f"Receipt saved to {filename}")

def main():
    receipt = Receipt()
    print("Welcome to the Receipt Calculator!")
    
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        try:
            price = float(input("Enter item price: ₹"))
            quantity = int(input("Enter item quantity: "))
            item = Item(name, price, quantity)
            receipt.add_item(item)
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")

    if not receipt.items:
        print("No items entered.")
        return

    print("\n" + receipt.generate_receipt_text())
    receipt.save_receipt_to_file()

if __name__ == "__main__":
    main
           