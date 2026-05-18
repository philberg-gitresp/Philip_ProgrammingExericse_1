# This program displays a total number of buyers who buy
# up to 4 cinema tickets, which is no more than 20.

# The function for how many tickets a buyer would like to buy.
def buy_tickets(remaining_tickets):
    tickets = int(input(f"We currently have {remaining_tickets} tickets left. How many would you like to buy?"
                        " You can only buy up to 1-4 tickets. "))

    # Makes the Ticket Request.
    if tickets < 1 or tickets > 4:
        print("You may only buy 1-4 tickets during purchases.")
        return 0

    if tickets > remaining_tickets:
        print("There are not enough tickets to buy with that amount.")
        return 0

    return tickets

# The function to process the ticket sale.
def process_sales(remaining_tickets, tickets_bought):
    remaining_tickets -= tickets_bought
    print(f"Your purchase has been successful!")
    print(f"Remaining Tickets: {remaining_tickets}")
    return remaining_tickets

############## Main Program #################
# There are 20 tickets for the cinema.
# Our buyers are the accumulator in the code.
#############################################

def main():
    total_tickets = 20
    buyers = 0

    print("Welcome to Regal Films Cinema!")

    while total_tickets > 0:

        tickets = buy_tickets(total_tickets)

        if tickets > 0:
            total_tickets = process_sales(total_tickets, tickets)
            buyers += 1

    # Displays the Results.
    print(" ")
    print("Unfortunately, all of our tickets have been sold out.")
    print("Thanks for coming to Regal Films Cinema, we hope to see you again!")
    print(f"Total Number of Buyers: {buyers}")

main()
