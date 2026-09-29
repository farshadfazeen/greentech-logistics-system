# GreenTech Logistics Shipment Order Management System
# Developed for MadZoo Digital (Pvt) Ltd
# Console Application using Python

# Stack implementation using list
# Level 1 urgent orders will be stored here
urgent_stack = []

# Queue implementation using list
# Level 2 standard orders will be stored here
standard_queue = []

# Orders ready for route optimisation will be stored here
ready_dispatch_orders = []


# Home page
# welcome screen before login
def home_page():
    print("")
    print("GREENTECH LOGISTICS")
    print("Shipment Order Management System")
    print("Developed by MadZoo Digital (Pvt) Ltd")
    print("")
    print("Welcome to the shipment order management console.")
    print("This system helps the company manage urgent and standard shipment orders.")
    print("Urgent orders are handled with priority.")
    print("Standard orders are handled in the order they arrive.")
    print("")
    input("Press Enter to continue to the login page")


# Login page
# This function checks the username and password
def login():
    # Admin login details stored using dictionary
    admin_details = {
        "admin": "123",
        "greentech": "2026",
        "madzoo": "0000"
    }

    home_page()

    # Login Page
    print("")
    print("LOGIN PAGE")
    print("Please enter your admin login details")
    print("")
    # Enter username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check username and password if there correct and then open menu
    if username in admin_details and admin_details[username] == password:
        print("")
        print("Login successful")
        print("Welcome", username)
        main_menu(username)
    else:
        print("")
        print("Invalid username or password")
        print("Please try again")


# Main menu
# This function shows the main options of the system
def main_menu(username):
    choice = ""

    while choice != "6":
        print("")
        print("GREEN TECH LOGISTICS - MAIN MENU")
        print("Logged in admin:", username)
        print("")
        print("System Status")
        print("Urgent Orders Available:", len(urgent_stack))
        print("Standard Orders Available:", len(standard_queue))
        print("Ready Dispatch Orders:", len(ready_dispatch_orders))
        print("")
        print("1. Manage Urgent Orders")
        print("2. Manage Standard Orders")
        print("3. Dashboard")
        print("4. Fast Track Delivery Line")
        print("5. Shipment Route Optimisation")
        print("6. Exit")
        print("")

        choice = input("Enter your choice: ")

        # Open 1. Manage Urgent Orders
        if choice == "1":
            urgent_orders_menu()

        # Open 2. Manage Standard Orders
        elif choice == "2":
            standard_orders_menu()

        # Open 3. Dashboard
        elif choice == "3":
            innovation_dashboard()

        # Open 4. Fast Track Delivery Line
        elif choice == "4":
            order_routing()

        # Open 5. Shipment Route Optimisation
        elif choice == "5":
            shipment_route_optimisation()

        elif choice == "6":
            print("")
            print("Logout successful")
            print("Thank you for using GreenTech Logistics System")

        else:
            print("")
            print("Invalid choice. Please try again")


# Level 1 urgent orders menu
# This function manages urgent orders using Stack and LIFO method
def urgent_orders_menu():
    choice = ""

    while choice != "7":
        print("")
        print("URGENT ORDER MANAGEMENT")
        print("")
        print("1. Add Urgent Order")
        print("2. View Latest Order")
        print("3. Remove Latest Order")
        print("4. View All Orders")
        print("5. Count Orders")
        print("6. Search Order")
        print("7. Back to Main Menu")
        print("")

        choice = input("Enter your choice: ")

        # Append operation
        if choice == "1":
            order_no = input("Enter urgent order number: ")
            order_name = input("Enter urgent order name: ")
            urgent_order = "U" + order_no + " - " + order_name
            urgent_stack.append(urgent_order)
            print("")
            print("Urgent order added successfully")
            print("Added order:", urgent_order)

        # Peek operation
        elif choice == "2":
            if urgent_stack:
                print("")
                print("Latest urgent order is:", urgent_stack[-1])
            else:
                print("")
                print("No urgent orders available")


        # Pop operation
        elif choice == "3":
            if urgent_stack:
                removed_order = urgent_stack.pop()
                print("")
                print("Latest urgent order removed from stack")
                print("Removed order:", removed_order)
            else:
                print("")
                print("No urgent orders to remove")

        # Display all urgent orders
        elif choice == "4":
            if urgent_stack:
                print("")
                print("All urgent orders:")
                print(urgent_stack)
            else:
                print("")
                print("No urgent orders available")

        # Count urgent orders
        elif choice == "5":
            print("")
            print("Total urgent orders:", len(urgent_stack))

        # Search urgent order
        elif choice == "6":
            search_id = input("Enter urgent order ID to search: ")
            # User enters ID like U1 or U2

            found = False
            # Used to check if order is found

            x = 0
            # Starts checking from the first order

            while x < len(urgent_stack):
                # Check each urgent order in the stack

                if search_id in urgent_stack[x]:
                    found = True
                    print("")
                    print("Urgent order found:", urgent_stack[x])

                x = x + 1
                # Move to next order

            if found == False:
                print("")
                print("Urgent order not found")

        # Back to main menu
        elif choice == "7":
            print("")
            print("Returning to main menu")


        else:
            print("")
            print("Invalid choice. Please try again")



# Level 2 standard orders menu
# This function manages standard orders using Queue and FIFO method
def standard_orders_menu():
    choice = ""

    while choice != "7":
        print("")
        print("STANDARD ORDER MANAGEMENT")
        print("")
        print("1. Add Standard Order")
        print("2. View First Order")
        print("3. Remove First Order")
        print("4. View All Orders")
        print("5. Count Orders")
        print("6. Search Order")
        print("7. Back to Main Menu")
        print("")

        choice = input("Enter your choice: ")

        # Enqueue operation
        if choice == "1":
            order_no = input("Enter standard order number: ")
            order_name = input("Enter standard order name: ")
            standard_order = "S" + order_no + " - " + order_name
            standard_queue.insert(0, standard_order)
            print("")
            print("Standard order added successfully")
            print("Added order:", standard_order)

        # Peek first order
        elif choice == "2":
            if standard_queue:
                print("")
                print("First standard order is:", standard_queue[-1])
            else:
                print("")
                print("No standard orders available")

        # Dequeue operation
        elif choice == "3":
            if standard_queue:
                removed_order = standard_queue.pop()
                print("")
                print("First standard order removed from queue")
                print("Removed order:", removed_order)
            else:
                print("")
                print("No standard orders to remove")

        # Display all standard orders
        elif choice == "4":
            if standard_queue:
                print("")
                print("All standard orders:")
                print(standard_queue)
            else:
                print("")
                print("No standard orders available")

        # Count standard orders
        elif choice == "5":
            print("")
            print("Total standard orders:", len(standard_queue))

        # Search standard order
        elif choice == "6":
            search_id = input("Enter standard order ID to search: ")
            # User enters the standard order ID, for example S1 or S2

            found = False
            # This variable checks whether the order is found or not
            # At the beginning, it is False because the order is not found yet

            x = 0
            # x is used as the index number to check each item in the standard queue

            while x < len(standard_queue):
                # This loop checks all standard orders one by one

                if search_id in standard_queue[x]:
                    # This checks whether the entered order ID is inside the current standard order

                    found = True
                    # If the order is found, found becomes True

                    print("")
                    print("Standard order found:", standard_queue[x])
                    # Display the standard order that was found

                x = x + 1
                # Move to the next standard order in the queue

            if found == False:
                # If the order was not found after checking the full queue, this message will display

                print("")
                print("Standard order not found")

        # Back to main menu
        elif choice == "7":
            print("")
            print("Returning to main menu")

        else:
            print("")
            print("Invalid choice. Please try again")


# Innovation - Dashboard
# This function shows extra system features for Level 3 or more
def innovation_dashboard():
    choice = ""

    while choice != "4":
        print("")
        print("DASHBOARD")
        print("Order Summary and Search Features")
        print("")
        print("1. View Order Summary Report")
        print("2. Search Any Order")
        print("3. View All Orders Together")
        print("4. Back to Main Menu")
        print("")

        choice = input("Enter your choice: ")

        # Summary Report
        if choice == "1":
            print("")
            print("ORDER SUMMARY REPORT")
            print("Urgent Orders:", len(urgent_stack))
            print("Standard Orders:", len(standard_queue))
            print("Ready Dispatch Orders:", len(ready_dispatch_orders))
            print("Total Active Orders:", len(urgent_stack) + len(standard_queue))

        # Search Order
        elif choice == "2":
            search_id = input("Enter order ID to search: ")
            # User enters ID like U1 or S1

            found = False
            # Used to check if order is found

            x = 0
            # Start checking urgent orders

            while x < len(urgent_stack):
                if search_id in urgent_stack[x]:
                    found = True
                    print("")
                    print("Order found in urgent orders:", urgent_stack[x])

                x = x + 1
                # Move to next urgent order

            x = 0
            # Start checking standard orders

            while x < len(standard_queue):
                if search_id in standard_queue[x]:
                    found = True
                    print("")
                    print("Order found in standard orders:", standard_queue[x])

                x = x + 1
                # Move to next standard order

            if found == False:
                print("")
                print("Order not found")

        # All Orders Display
        elif choice == "3":
            print("")
            print("ALL ORDERS IN THE SYSTEM")
            print("Urgent Orders:")
            print(urgent_stack)
            print("Standard Orders:")
            print(standard_queue)
            print("Ready Dispatch Orders:")
            print(ready_dispatch_orders)

        # Return to Main Menu
        elif choice == "4":
            print("")
            print("Returning to main menu")

        else:
            print("")
            print("Invalid choice. Please try again")


# Recursive fast track process
# This function calls itself until the urgent order is ready for dispatch
def fast_track_process(order, stage):
    if stage == 1:
        print("Stage 1: Urgent order received for fast track")
        fast_track_process(order, 2)

    elif stage == 2:
        print("Stage 2: Eco package checked")
        fast_track_process(order, 3)

    elif stage == 3:
        print("Stage 3: Priority delivery label added")
        fast_track_process(order, 4)

    elif stage == 4:
        print("Stage 4: Fast track delivery line completed")
        print("Order ready for dispatch:", order)


# Order routing
# This function sends the latest urgent order to the Fast Track Delivery Line
def order_routing():
    print("")
    print("FAST TRACK DELIVERY LINE")
    print("Urgent orders are processed using latest order first")
    print("")

    if urgent_stack:
        # Check whether urgent orders are available in the stack

        routed_order = urgent_stack.pop()
        # pop() removes the latest urgent order from the stack
        # This follows the LIFO method

        print("Selected urgent order:", routed_order)
        print("Assigned to Fast Track Delivery Line")
        print("")

        fast_track_process(routed_order, 1)
        # This sends the selected urgent order to recursive fast track processing
        # Stage 1 is passed as the starting stage

        ready_dispatch_orders.append(routed_order)
        # After fast track processing, the order is added to ready dispatch list

        print("")
        print("Order moved to ready dispatch list")

    else:

        print("No urgent orders available for fast track processing")
    print("")
    input("Press Enter to return to main menu")



# Shipment route optimisation
# This function selects route based on time and distance
def shipment_route_optimisation():
    print("")
    print("SHIPMENT ROUTE OPTIMISATION")
    print("Urgent orders are prioritised for faster delivery")
    print("")

    if ready_dispatch_orders:
        selected_order = ""
        # This variable will store the order selected for route optimisation

        selected_index = -1
        # This variable will store the position of the selected order in the list

        x = 0
        # This variable is used to check each order one by one

        # Select urgent order first if available
        while x < len(ready_dispatch_orders):
            # This loop runs until all ready dispatch orders are checked

            if ready_dispatch_orders[x][0] == "U" and selected_order == "":
                # This checks whether the current order is an urgent order
                # [0] checks the first letter of the order ID
                # If the first letter is U, it means it is an urgent order
                # selected_order == "" makes sure only the first urgent order is selected

                selected_order = ready_dispatch_orders[x]
                # Store the urgent order as the selected order

                selected_index = x
                # Store the position of the selected urgent order

            x = x + 1
            # Move to the next order in the ready dispatch list

        # If urgent order is not available, select the first ready order
        if selected_order == "":
            selected_order = ready_dispatch_orders[0]
            selected_index = 0

        print("Selected order for route optimisation:", selected_order)
        print("")

        print("Available Routes")
        print("Route A - Distance 12 km - Time 25 minutes")
        print("Route B - Distance 8 km  - Time 35 minutes")
        print("Route C - Distance 15 km - Time 20 minutes")
        print("")

        route_a_distance = 12
        route_a_time = 25

        route_b_distance = 8
        route_b_time = 35

        route_c_distance = 15
        route_c_time = 20

        # Urgent orders select the fastest route by time
        if selected_order[0] == "U":
            if route_a_time <= route_b_time and route_a_time <= route_c_time:
                print("Best route selected: Route A")
                print("Reason: Route A has the fastest delivery time")
            elif route_b_time <= route_a_time and route_b_time <= route_c_time:
                print("Best route selected: Route B")
                print("Reason: Route B has the fastest delivery time")
            else:
                print("Best route selected: Route C")
                print("Reason: Route C has the fastest delivery time")

        # Standard orders select the shortest route by distance
        elif selected_order[0] == "S":
            if route_a_distance <= route_b_distance and route_a_distance <= route_c_distance:
                print("Best route selected: Route A")
                print("Reason: Route A has the shortest distance")
            elif route_b_distance <= route_a_distance and route_b_distance <= route_c_distance:
                print("Best route selected: Route B")
                print("Reason: Route B has the shortest distance")
            else:
                print("Best route selected: Route C")
                print("Reason: Route C has the shortest distance")

        ready_dispatch_orders.pop(selected_index)
        print("")
        print("Route optimisation completed for:", selected_order)

    else:
        print("No orders available for route optimisation")

    print("")
    input("Press Enter to return to main menu")


# Program starts from here
login()