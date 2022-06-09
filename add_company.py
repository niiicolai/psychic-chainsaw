from company import Company
from database import Database

# An operation used to add a company.
class AddCompany():    
    
    # The behaviour of the operation. 
    def run():
        print("==================================================")
        print("You are currently adding a new company")
        print("Type 'exit' to return to the main menu")
        # Ask the user for the name of the company
        name = input("Enter the name of the company: ")
        # Quit if the user types 'exit'
        if name.upper() == "EXIT":
            print("=> Exiting operation")
            return
        # Ensure the name is longer than 0 characters
        if len(name) == 0:
            print("=> The name must be longer than 0 characters")
            # restart the method
            AddCompany.run()
            # return to the method
            # to avoid duplicating
            # operations for each reverse call
            return
        # Ensure the company does not already exist
        for company in Database.companies:
            if company.compare_to(name):
                print("=> The company already exists")
                # restart the method
                AddCompany.run()
                # return to the method
                # to avoid duplicating
                # operations for each reverse call
                return

        # Create a company with the name
        company = Company(name)

        # Add the company to the database
        Database.add_company(company)

        # Let the user know the company was added
        print("=> The company was added")