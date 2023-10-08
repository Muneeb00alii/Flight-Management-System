# Muneeb Ali
# 261927223

# Explaining that What is this Code Supposed To Do.

'''This Python Code Let the Users 1.Book Flights, 2.Cancel Bookings, and 3.View Available Flights.


  Administrators can Also 1.Add Flight,2.Remove Flight, and 3.Modify Flight Details.


  To Use this Code, Run it and Select Login or Exit. If you Log in, You will be Prompted to Enter your Username and Password.


  Once you are Logged in, You can Access the Features of the Code Based on your Role (Guest or Administrator).


  Guests can Book, Cancel, and View Flights. To Book a Flight, Select the Booking Option and Follow the Prompts. To Cancel a Booking,


  Select the Cancel Booking Option and Choose the  Booking Details of the Flight you want to Cancel. To View Available Flights, Select the View Flights Option.


  Administrators can Add, Remove, and Modify Flight Details. To Add a New Flight, Select the Add Flight Option and Enter the Flight Details.


  To Remove an Existing Flight, Select the Remove Flight Option and Enter the Flight Details. To Modify Flight Details,


  Select the Modify Flight Option and Enter the Flight Details and the Changes you want to Make.'''


# Defining the Path to the Data File

data_file_path = "C:\\Users\\92321\\OneDrive\\Desktop\\Ticketing Data.txt"

flight_data = {}

# loading Data from the File Using Loops
try:
    with open(data_file_path, "r") as data_file:
        for line in data_file:
            key, value = line.strip().split(": ", 1)  # Split at the first ': ' to handle colons within values
            flight_data[key] = eval(value)  # Convert the string to a Python dictionary
    print("\nData Loaded Successfully")  # Add this line for debugging
except FileNotFoundError:
    print("File not Found, Initializing Flight_Data as Empty.")
    


# Function to save data to the file using loops
def save_data():
    with open(data_file_path, "w") as data_file:
        for key, value in flight_data.items():
            data_file.write(f"{key}: {value}\n")

# This Function is used to Differentiate Between User and Admin (Coder:Muneeb) 
def verification():
    global selected_flight
    userName = input("\nEnter your Username: ")
    password = input("\nEnter your Password: ")

# Guest Login

    if userName == 'Guest' and password == 'hi':
        print("\nWelcome to TG Travels.")
        print('"'*30)
        print("\nPlease Select the Function:")
        print("\n1. Book a Flight")
        print("\n2. Cancel a Flight")
        print("\n3. View Flights")
        choice = input("\nEnter your Choice (1/2/3): ")

        if choice == '1':
            booking()
        elif choice == '2':
            cancel_flight()
        elif choice == '3':
            view_flights()
        else:
            print("Invalid Choice")

# Admin Login

    elif userName == 'Muneeb' and password == 'me':
        print("\nWelcome, Muneeb!")
        print('"'*25)
        print("\nPlease Select the Function:")
        print("\n1. Add a Flight")
        print("\n2. Remove a Flight")
        print("\n3. Modify a Flight")
        choice = input("\nEnter your Choice (1/2/3): ")

        if choice == '1':
            add_flight()
        elif choice == '2':
            delete_flight()
        elif choice == '3':
            modify_flight()
        else:
            print("Invalid Choice")
    else:
        print("Verification Error: Invalid Username or Password. Please Try Again")

# This is the Function Show you All the Available Flights and Ask the User to Choose 1 Flight Option to Book a Flight

def booking():
    global selected_flight,flight_data
    print("\nPlease Select a Flight:")
    for key, value in flight_data.items():
        print(f"\nFlight No: {key}")
        print(f"\nFlight Company: {value['Flight Company']}")
        print(f"\nTotal Seats: {value['Total Seats']}")
        print(f"\nFares: {value['Fares']}")
        print(f"\nRoute: {value['Route']}")
        print(f"\nDate of Flight: {value['Date of Flight']}")
        print()
        print('"'*45)
        
        
    flight_choice = input("\nEnter the Flight No you want to book: ")
    if flight_choice in flight_data:
        selected_flight = flight_data[flight_choice]
        selecting_seat(flight_choice)  
    else:
        print("\nInvalid Flight No. Please Try Again")

# This is the Function to Select a Seat in the Selected Airline

def selecting_seat(flight_choice):
    global selected_flight,flight_data
    if selected_flight is not None:
        flight_number = flight_choice

        # Here I am Printing The Selected Flight Details for Confirmation

        print(f"\nSelected Flight Details:")
        print(f"\nFlight No: {flight_number}")
        print(f"\nFlight Company: {selected_flight['Flight Company']}")
        print(f"\nTotal Seats: {selected_flight['Total Seats']}")
        print(f"\nFares: {selected_flight['Fares']}")
        print(f"\nRoute: {selected_flight['Route']}")
        print(f"\nDate of Flight: {selected_flight['Date of Flight']}")
        print()
        print('"'*45)
        
        # Here I am Printing Grid for Seat Selection

        print("\nAvailable Seats:")
        for i, row in enumerate(selected_flight["Seats"]):
            for j, seat_status in enumerate(row):
                text = seat_status
                if seat_status == "*":
                    text = f"{i + 1}{chr(j + ord('A'))}"
                print(text, end="\t")
            print()
        print()

        # Here I am Asking About the Seat User want to Book

        row = int(input("\nEnter Row (1-4): "))
        column = input("\nEnter Column (A-E or a-e): ").upper()
        passenger_name = input("\nEnter the Passenger Name: ")

        if 1 <= row <= 4 and column in "ABCDE":
            selected_row = row - 1
            selected_column = ord(column) - ord("A")
            if selected_flight["Seats"][selected_row][selected_column] == "*":
                selected_flight["Seats"][selected_row][selected_column] = "X"
                update_grid()
                fare = selected_flight['Fares']
                print(f"\nBooking Confirmation:")
                print(f"\nYour seat {row}{column} is booked for {selected_flight['Flight Company']}.")

                # Here I am Storing the Ticket Booking Data in a txt File Ticketing Record File
                with open("Ticketing Record File.txt", "a") as f:
                    f.write("Booking Details:\n")
                    f.write(f"Flight No: {flight_choice}\n")
                    f.write(f"Flight Company: {selected_flight['Flight Company']}\n")
                    f.write(f"Passenger Name: {passenger_name}\n")
                    f.write(f"Seat Number: {row}{column}\n")
                    f.write(f"Fare: {fare}\n")
                    f.write(f"Date of Flight: {selected_flight['Date of Flight']}\n\n")

                # Here I am Storing Booking Details in the Flight Data Which will be Used for Cancellation
                selected_flight["Passengers"][f"{row}{column}"] = {
                    "Name": passenger_name,
                    "Fare": fare
                }
                save_data()
            else:
                print("\nInvalid Seat Selection or the Seat is Already Booked.. Please Try Again")
        else:
            print("\nInvalid Row or Column Selection.. Please Try Again")

# This is a that Function to Update the Grid of the Available Seats

def update_grid():
    for i, row in enumerate(selected_flight["Seats"]):
        for j, seat_status in enumerate(row):
            if seat_status == "*":
                seat_status = f"{i + 1}{chr(j + ord('A'))}"
            print(seat_status, end="\t")
        print()
    print()

# This is the Function to Cancel a Booked Seat at a Flight 

def cancel_flight():
    global flight_data

    # Here I am Showing the Booking Made For Confirmation

    print("\nList of Booked Flights:")
    for flight_no, flight_info in flight_data.items():
        if flight_info["Passengers"]:
            print(f"Flight No: {flight_no}")
            print(f"Flight Company: {flight_info['Flight Company']}")
            print(f"Date of Flight: {flight_info['Date of Flight']}")
            print()

    flight_no = input("\nEnter the Flight No to cancel a booking: ")

    if flight_no in flight_data and flight_data[flight_no]["Passengers"]:
        print("\nList of Booked Seats:")
        for seat, passenger_info in flight_data[flight_no]["Passengers"].items():
            print(f"Seat: {seat}, Passenger: {passenger_info['Name']}")

        seat_to_cancel = input("\nEnter the seat to cancel (e.g., 1A): ")

        if seat_to_cancel in flight_data[flight_no]["Passengers"]:
            passenger_name = flight_data[flight_no]["Passengers"][seat_to_cancel]["Name"]
            fare = flight_data[flight_no]["Passengers"][seat_to_cancel]["Fare"]
            
# Here I am Marking the Seat as Available Again by Changing "X" to "*"

            row = int(seat_to_cancel[0]) - 1
            column = ord(seat_to_cancel[1]) - ord("A")
            flight_data[flight_no]["Seats"][row][column] = "*"

# Here I am Removing Booking Details from the Text File

            with open("Ticketing Record File.txt", "r") as f:
                lines = f.readlines()
            with open("Ticketing Record File.txt", "w") as f:
                for line in lines:
                    if not (f"Flight No: {flight_no}" in line and f"Seat Number: {seat_to_cancel}" in line):
                        f.write(line)

            del flight_data[flight_no]["Passengers"][seat_to_cancel]
            save_data()
            print(f"\nBooking for seat {seat_to_cancel} on Flight No. {flight_no} has been canceled.")
        else:
            print("\nInvalid Seat Selection. Please Try Again")
    else:
        print("\nInvalid Flight No or no bookings found for the Selected Flight. Please Try Again")

# This is a  Function that Add a Flight (Only for Admin Use)

def add_flight():
    global flight_data
    flight_no = len(flight_data) + 1
    flight_company = input("\nEnter the Flight Company: ")
    total_seats = int(input("\nEnter the Total Seats: "))
    fares = input("\nEnter the Fare of Flight: ")
    route = input("\nEnter the Route: ")
    date_of_flight = input("\nEnter the Date: ")


    flight_data[str(flight_no)] = {
        "Flight Company": flight_company,
        "Total Seats": total_seats,
        "Fares": fares,
        "Route": route,
        "Date of Flight": date_of_flight,
        "Seats": [["*"] * 5 for _ in range(4)],
        "Passengers": {}
    }
    print(f"\nFlight No. {flight_no} has Been Added.")
    save_data()

# This is a Function to Delete a Flight 

def delete_flight():
    global flight_data
    flight_no = input("\nEnter the Flight No to Removed: ")
    if flight_no in flight_data:
        del flight_data[flight_no]
        print(f"\nFlight No. {flight_no} has been Remove .")
        save_data()
    else:
        print(f"Flight No. {flight_no} Doesn't Exist. . Please Try Again")

# This is a Function to Modify a Flight

def modify_flight():
    global flight_data
    print("\nModify Flight Details:")
    
# Here I am Displaying All the Available Flighs So the User Can Choose the Flight he wants to Modify
    
    print("\nAvailable Flights:")
    for key, value in flight_data.items():
        print(f"\nFlight No: {key}")
        print(f"\nFlight Company: {value['Flight Company']}")
        print(f"\nTotal Seats: {value['Total Seats']}")
        print(f"\nFares: {value['Fares']}")
        print(f"\nRoute: {value['Route']}")
        print(f"\nDate of Flight: {value['Date of Flight']}")
        print()
        print('"'*45)


    flight_no = input("\nEnter the Flight No to Modify: ")

# Here I am Getting the New Data for the Selected Flight
        
    if flight_no in flight_data:

        flight_company = input("\nEnter New Flight Company (Leave Empty to Keep Current): ")
        total_seats = input("\nEnter New Total Seats (Leave Empty to Keep Current): ")
        fares = input("\nEnter New Fare of Flight (Leave Empty to Keep Current): ")
        route = input("\nEnter New Route (Leave Empty to Keep Current): ")
        date_of_flight = input("\nEnter New Date (Leave Empty to Keep Current): ")

# Here I am Updating the Old Flight Data with New Details if Provided into the Text File
        
        if flight_company:
            flight_data[flight_no]['Flight Company'] = flight_company
        if total_seats:
            flight_data[flight_no]['Total Seats'] = int(total_seats)
        if fares:
            flight_data[flight_no]['Fares'] = fares
        if route:
            flight_data[flight_no]['Route'] = route
        if date_of_flight:
            flight_data[flight_no]['Date of Flight'] = date_of_flight

        print(f"Flight No. {flight_no} details have been modified.")
        save_data()
    else:
        print(f"Flight No. {flight_no} Doesn't Exist. Please Try Again")
        
# This is a Function which will Display All the Flights Available

def view_flights():
    global flight_data
    print("Available Flights:")
    for key, value in flight_data.items():
        print(f"Flight No: {key}")
        print(f"Flight Company: {value['Flight Company']}")
        print(f"Total Seats: {value['Total Seats']}")
        print(f"Fares: {value['Fares']}")
        print(f"Route: {value['Route']}")
        print(f"Date of Flight: {value['Date of Flight']}")
        print()
        print('"'*45)
    print("If you want to Book any Flight Go to Booh A Flight. Thank You For Using TG Travels! Have a great day.")    


while True: # It Should Always Be True 
    print("\nTG Travels")
    print('"'*15)
    print("\nPlease Select the Function:")
    print("\n1. Login")
    print("\n2. Exit")
    choice = input("\nEnter your Choice (1/2): ")

    if choice == '1':
        verification()
    elif choice == '2':
        print("\nThank you for using TG Travels! Have a great day.")
        break
    else:
        print("Invalid Choice, Try Again")

# Coded By Muneeb Ali. 
# Happy Checking...
