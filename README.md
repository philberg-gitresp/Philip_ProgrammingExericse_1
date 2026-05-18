# Philip_ProgrammingExericse_1
In this program, there are 20 tickets for the cinema. Each buyer selects either 1-4 tickets depending on what the input is given, and they can not pick 0 or over 4. Furthermore, they can not buy tickets that they do not have enough of. After all the tickets have been sold, it displays how many buyers were there and ends the program. The input can not have nothing in it or else the program will stop entirely, so the person who inputs it needs to have a number through 1-4.

## Function: buy_tickets
The function for how many tickets a buyer would like to buy (1-4)

Parameters:
tickets (How many would the buyer purchase?)
buyers (How many buyers came to the cinema?)

Variables:
remaining_tickets (The remaining tickets that are left for purchase.)
total_tickets (The total amount of tickets at the cinema, there were 20 remaining.)

Logic:
1. The program asks how many tickets from the remaining 20 that the buyer will purchase ranging from 1-4. They can not pick nothing or pick tickets that are not enough.
2. An input is made and the remaining tickets go down while representing that number.
3. The program loops until all the remaining tickets are gone.

Returns: tickets

## Function: process_sales
The function to process the ticket sale.

Parameters:
None

Variables:
remaining_tickets (The remaining tickets that are left for purchase.)
tickets_bought (How many tickets were bought.)

Logic:
1. Issues that the purchase has been successful.
2. Displays the remaining amount of tickets left.
3. Continues to ask the viewer to input till there are no more tickets left (Similar to the last function).

Returns: remaining_tickets
