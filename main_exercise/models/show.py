from main_exercise.models.ticket import VIPTicket
class Show:
    def __init__(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date
        self.tickets = []

    def add_ticket(self, ticket):
        if any(t.id == ticket.id for t in self.tickets):
            raise ValueError("Ticket with this ID already exists.")
        self.tickets.append(ticket)

    def remove_ticket(self, ticket_id):
        self.tickets = [t for t in self.tickets if t.id != ticket_id]

    def calculate_revenue(self):
        return sum(ticket.calculate_price() for ticket in self.tickets)

    def calculate_total_discount(self):
        return sum(ticket.customer.customer_discount for ticket in self.tickets if isinstance(ticket, VIPTicket))
