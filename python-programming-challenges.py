# This is where we start with some example service tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to add a new ticket
def open_ticket(ticket_id, customer_name, issue_description):
    # Check if ID is already in the list
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists. Please use a different ID.")
    else:
        # Add a new ticket to list
        service_tickets[ticket_id] = {
            "Customer": customer_name,
            "Issue": issue_description,
            "Status": "open"
        }
        print(f"New ticket: {ticket_id} added for {customer_name}.")

# Function to change existing ticket
def update_ticket_status(ticket_id, new_status):
    # Check if the ticket ID is in our list
    if ticket_id in service_tickets:
        # Change the status of the ticket
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket: {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket ID {ticket_id} not found.")

# View all tickets
def display_tickets(status_filter=None):
    if status_filter:
        print(f"\nShowing all tickets with status '{status_filter}':")
        # Loop through tickets and show only those with the specific status
        for ticket_id, details in service_tickets.items():
            if details["Status"].lower() == status_filter.lower():
                print(f"{ticket_id}: {details['Customer']} - {details['Issue']} ({details['Status']})")
    else:
        print("\nShowing all tickets:")
        # Loop through all tickets and show them
        for ticket_id, details in service_tickets.items():
            print(f"{ticket_id}: {details['Customer']} - {details['Issue']} ({details['Status']})")


# 1. Show all the tickets we have
display_tickets()

# 2. Add a new ticket
open_ticket("Ticket003", "Charlie", "Account suspension")

# 3. Update the status of an existing ticket
update_ticket_status("Ticket001", "closed")

# 4. Show only the open tickets
display_tickets("open")

# 5. Show all the tickets to see the updates
display_tickets()