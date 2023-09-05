class Customer:
    def __init__(self):
        print(f"Welcome to ABC Memorial Park")
        self.ticket_count = 0
        self.total_price = 0



# If the visitor’s age is greater than 10, then the ticket price is 100 taka. Otherwise, 50 taka.
# A customer can’t buy more than 3 tickets.]

    def buyTicket(self, name, age):
          
        if self.ticket_count >= 3:
            print(f"You can't buy more than 3 tickets")
            return
            
        if age > 10:
            ticket_price = 100
        else:
            ticket_price = 50
            
            
        
        self.total_price += ticket_price    
        self.ticket_count += 1
        print(f"Successfully purchased a ticket for {name}!")

    def showDetails(self):
        print("Amount of tickets:", self.ticket_count)
        print("Total price:", self.total_price, "Taka")







print('1-------------------------')
customer1 = Customer()
print('2-------------------------')
customer1.buyTicket('Bob', 23)
customer1.buyTicket('Henry', 7)
customer1.buyTicket('Alexa', 30)
customer1.buyTicket('Jonas', 43)
print('3-------------------------')
customer1.showDetails()
print('4-------------------------')
customer2 = Customer()
print('5-------------------------')
customer2.buyTicket('Harry', 60)
customer2.buyTicket('Tomas', 28)
print('6-------------------------')
customer2.showDetails()


# 1--------------------------
# Welcome to ABC Memorial Park
# 2--------------------------
# Successfully purchased a ticket for Bob!
# Successfully purchased a ticket for Henry!
# Successfully purchased a ticket for Alexa!
# You can't buy more than 3 tickets
# 3--------------------------
# Amount of tickets: 3
# Total price: 250 Taka
# 4--------------------------
# Welcome to ABC Memorial Park
# 5--------------------------
# Successfully purchased a ticket for Harry!
# Successfully purchased a ticket for Tomas!
# 6--------------------------
# Amount of tickets: 2
# Total price: 200 Taka
