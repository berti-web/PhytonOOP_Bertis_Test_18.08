from abc import ABC, abstractmethod


class Ticket(ABC):
    def __init__(self, id, show_name, show_date, row, seat, customer, price):
        self.id = id
        self.show_name = show_name
        self.show_date = show_date
        self.row = row
        self.seat = seat
        self.customer = customer
        self.price = price

    @abstractmethod
    def calculate_price(self):
        pass


class RegularTicket(Ticket):
    def calculate_price(self):
        return self.price


class VIPTicket(Ticket):
    def calculate_price(self):
        if self.customer.customer_type != 'VIP':
            raise ValueError("Customer is not a VIP")
        return self.price - self.customer.customer_discount
