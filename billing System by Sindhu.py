class BillingSystem:
    def __init__(self):
        self.items = {}
        self.total_bill = 0

    def add_item(self, item, quantity, price):
        self.items[item] = {'quantity': quantity, 'price': price}
        print(f"{quantity} {item}(s) added to the bill.")

    def calculate_bill(self):
        for item, details in self.items.items():
            total_item_cost = details['quantity'] * details['price']
            self.total_bill += total_item_cost
            print(f"{item}: {details['quantity']} x ${details['price']} = ${total_item_cost}")

    def display_bill(self):
        print(f"\nTotal Bill: ${self.total_bill}\n")


def main():
    billing_system = BillingSystem()

    while True:
        print("\nOptions:")
        print("1. Add item to the bill")
        print("2. Calculate and display the bill")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))
            billing_system.add_item(item, quantity, price)

        elif choice == '2':
            billing_system.calculate_bill()
            billing_system.display_bill()

        elif choice == '3':
            print("Exiting the billing system. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
