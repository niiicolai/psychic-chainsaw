from database import Database

# An operation used to add a company.
class SearchCompanies():    
    
    # The behaviour of the operation. 
    def run():
        print("==================================================")
        print("You are currently searching for a company by name")
        print("Type 'exit' to return to the main menu")

        # Exit if there doesn't exist any companies
        if len(Database.companies) == 0:
            print("=> You have no companies to search, exiting operation")
            return

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
            SearchCompanies.run()
            # return to the method
            # to avoid duplicating
            # operations for each reverse call
            return

        # find the company
        c = None
        for company in Database.companies:
            if company.compare_to(name):
                c = company 
                break
        
        # If the company was not found
        if c is None:
            print("=> The company was not found")
            # restart the method
            SearchCompanies.run()
        else:
            # Print the information about the company
            print("==================================================")
            print("=> Company found:")
            print(f"Name: {company.get_name()}")
            print(f"Certificates (Total: {len(company.get_certificates())}):")
            i = 1
            for certificate in company.get_certificates():
                print(f"{i}. Certificate")
                print(f"Type: {type(certificate).__name__}")
                print(f"Watt: {certificate.get_watt()}")
                i += 1