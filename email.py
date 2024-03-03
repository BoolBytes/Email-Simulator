# Import 'os' module to allow us to define a variable to clear the terminal, so it does not become too crowded
import os


# Defining the 'clear_terminal' function to clear terminal 
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# The following program is an email simulator made using OOP, functions, lists, and conditional statements
# To start, we create a class named 'Email', and assign it two class variables; 'inbox', an empty string to hold email values, and 'has_been_read' a boolean variable to mark whether an email has been read
class Email:
    inbox = []
    has_been_read = False


    # We then initialise a constructor that takes three areguments, then we define said arguments using 'self'
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content


    # After this we create a class method, that changes the value of the class variable 'has_been_read'
    # We using 'self' to modify the instance of the class attribute, not the attribute itself 
    def mark_as_read(self):
        self.has_been_read = True
        print(f"\nEmail from {self.email_address} marked as read.")


    # Then we create a function that takes the arguments of 'self', to create an email object with all the arguments of our constructor and store it in the inbox list 
    def populate_inbox(self):
        Email.inbox.append(self)


    # After we create another function that takes the arguments of 'self', loop through the inbox, and print the subject line along with the corresponding number
    def list_emails(self):
        for index, sub_line in enumerate(Email.inbox):
            print(f"{index} {sub_line.subject_line}")


    # Following this we create another function, taking 'self', and 'index' as an argument
    # This will read an email selected by the user, and mark it as read, the 'index' argument is based on user input
    def read_email(self, index):
            if 0 <= index <= len(Email.inbox):
                email = Email.inbox[index]
                print(f"\nFrom: {email.email_address}\nSubject: {email.subject_line}\n{email.email_content}")
                email.mark_as_read()
            else:
                print("\nInvalid index. Please select a valid email.")


# These are the sample emails, used to populate the inbox
email1 = Email("sender1@example.com", "Welcome to your new inbox!", "This is the content of the first email.")
email2 = Email("sender2@example.com", "Great work on the task!", "Congratulations on your progress.")
email3 = Email("sender3@example.com", "Your excellent attitude!", "Your attitude thus far has been amazing.")


# This is how we populate the inbox via invoking the corresponding function
email1.populate_inbox()
email2.populate_inbox()
email3.populate_inbox()


# This is a custom ASCII title for the 'email simulator'
print("""
███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
█████╗░░██╔████╔██║███████║██║██║░░░░░  ╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
███████╗██║░╚═╝░██║██║░░██║██║███████╗  ██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝ 
    """)


# Variable used to break out of the while-loop
user_choice = 0


# While-loop to allow user to remain in the inbox and continuously select what they want to do whilst in there 
# Condition set so that whilst the variable is not equal to the quit application option, continue looping
while user_choice != 3:


    # Input statement casted into an integer, used to take the value of the user option
    user_choice = int(input(f"\nYou have {len(Email.inbox)} emails\n\nPick one of the three options:\n1. Read an email\n2. View unread emails\n3. Quit application\n= "))


    # Invoking clear terminal function 
    clear_terminal()


    # conditional statements for each of the user's choices
    # First if-statement, lists subject line with corresponding number, and input statement to allow user to select what email they would like to read
    if user_choice == 1:
        print("Email Inbox")
        email1.list_emails()
        email_position = int(input(f"\nChoose which numerical position email you would like to read:\n'0' = 1st email\n'1' = 2nd email, and so on...\nEmail Number =  "))
        email_to_read = Email.inbox[email_position]
        email_to_read.read_email(email_position)
        

    # Elif-statement, with additional if/else statement, allows user to view which emails have be read/unread, and shows the subject line 
    elif user_choice == 2:
        for index, email in enumerate(Email.inbox):
            if not email.has_been_read:
                print(f"Unread Email - From: {email.email_address}, Subject: {email.subject_line}")
            else:
                print(f"Read Email - From: {email.email_address}, Subject: {email.subject_line}")


    # Another elif-statement if user selects 3, meeting the parameter to exit the loop and printing the 'Goodbye' message
    elif user_choice == 3:
        print("Goodbye! ")
    


    # Else-statement used to prompt user to enter a number within the range
    else:
        print("Please choose option 1, 2, or 3")