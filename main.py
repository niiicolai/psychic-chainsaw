from add_company import AddCompany
from add_certificate import AddCertificate
from search_companies import SearchCompanies

class Main():

    operations = {
        "add company": AddCompany.run,
        "add certificate": AddCertificate.run,
        "search companies": SearchCompanies.run,
        "exit": None
    }

    def run():
        # Loop until the user wants to quit
        while True:
            # Print some information about the program
            print("==================================================")
            print("Welcome to the energy certificate program!\nCommands:")
            # print keys in operations
            for key, value in Main.operations.items() :
                print (f"=> {key.capitalize()}")

            # Ask the user for the option
            message = input("Enter a command: ").lower()

            if message in Main.operations:
                operation = Main.operations[message]
                # None operation means the
                # user wants to quit
                if operation is None:
                    print("=> Goodbye!")
                    # Quit the program
                    break
                else:
                    # Run the operation
                    operation()
            else:
                # Print an error message
                print("=> Unknown command")
                

if __name__ == "__main__":
    Main.run()