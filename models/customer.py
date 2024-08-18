class Customer:
    def __init__(self, id, first_name, last_name, email, address, customer_type, discount=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.customer_type = customer_type
        self.customer_discount = discount
        self.food_voucher = None

    def take_food_voucher(self, food_voucher):
        self.food_voucher = food_voucher

    def eat_food(self):
        if self.food_voucher:
            self.food_voucher.eat()
        else:
            print("No food voucher available.")
