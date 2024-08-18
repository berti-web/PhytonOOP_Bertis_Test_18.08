
from main_exercise.models import Customer, RegularTicket, VIPTicket, Show, FoodVoucher

if __name__ == "__main__":
    customer1 = Customer(1, "Ori", "Dahan", "Ori21@example.com", "123 Jerusalem Blvrd", "VIP", discount=20)
    customer2 = Customer(2, "Amit", "Dahan", "Amit23@example.com", "123 Jerusalem Blvrd", "VIP", discount=20)
    customer3 = Customer(3, "Omer", "Shimoni", "Omer22@example.com", "456 Fikus Avenue", "REGULAR")
    customer4 = Customer(4, "Ron", "Shimoni", "Ron14@example.com", "456 Fikus Avenue", "REGULAR")
    customer5 = Customer(5, "Haim", "Levi", "Haiml@example.com", "789 Sorek st", "REGULAR")

    show = Show(101, "Mama Mia!", "2024-12-25")

    ticket1 = VIPTicket(1, "Mama Mia!", "2024-12-25", 5, 10, customer1, 100)
    ticket2 = VIPTicket(2, "Mama Mia!", "2024-12-25", 5, 9, customer2, 100)
    ticket3 = RegularTicket(3, "Mama Mia!", "2024-12-25", 10, 15, customer3, 100)
    ticket4 = RegularTicket(4, "Mama Mia!", "2024-12-25", 10, 16, customer4, 100)
    ticket5 = RegularTicket(5, "Mama Mia!", "2024-12-25", 10, 17, customer5, 100)

    show.add_ticket(ticket1)
    show.add_ticket(ticket2)
    show.add_ticket(ticket3)
    show.add_ticket(ticket4)
    show.add_ticket(ticket5)

    print("Show Revenue:", show.calculate_revenue())
    # Expected: 460
    print("Total VIP Discount Given:", show.calculate_total_discount())
    # Expected: 40.0

    food_voucher = FoodVoucher()
    customer1.take_food_voucher(food_voucher)
    customer1.eat_food()
    # Expected: "Here is your food, enjoy!"
