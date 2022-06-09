from certificate import Sun
from certificate import Wind
from database import Database

# An operation used to add a company.
class AddCertificate():    
    
    # The behaviour of the operation. 
    def run():
        print("==================================================")
        print("You are currently adding a new certificate")
        print("Type 'exit' to return to the main menu")

        # Exit if there doesn't exist any companies
        if len(Database.companies) == 0:
            print("=> Please add a company before adding a certificate, exiting operation")
            return

        # Ask the user for the name of the company
        name = input("Enter the name of the company: ")

        # Quit if the user types 'exit'
        if name.upper() == "EXIT":
            print("=> Exiting operation")
            return

        # Find the company
        c = None
        for company in Database.companies:
            if company.compare_to(name):
                c = company 
                break
        
        # If the company was not found
        if c is None:
            print("=> The company was not found")
            # restart the method
            AddCertificate.run()
        else:
            try:
                # Ask the user for the watt
                watt = float(input("Enter the watt: "))
            except ValueError:
                print("=> The watt must be a number")
                # restart the method
                AddCertificate.run()
                # return to the method
                # to avoid duplicating
                # operations for each reverse call
                return

            # Ask to select the type of certificate
            print("=> Select the type of certificate")
            print("1. Sun certificate")
            print("2. Wind certificate")

            # Ask the user for the option
            option = input("Enter the option: ")

            # Quit if the user types 'exit'
            if option.upper() == "EXIT":
                print("=> Exiting operation")
                return

            certificate = None
            # Create a certificate with the watt
            if option == "1" or option ==  "sun certificate" or option == "sun":
                # Create certificate
                certificate = Sun(watt, c.get_name())
            elif option == "2" or option == "wind certificate" or option == "wind":
                # Create certificate
                certificate = Wind(watt, c.get_name())
            else:
                print("=> Invalid option")
                # restart the method
                AddCertificate.run()
                # return to the method
                # to avoid duplicating
                # operations for each reverse call
                return

            if certificate is not None:
                # Add the certificate to the company
                c.add_certificate(certificate)
                # Let the user know the certificate was added
                print(f"=> The certificate was added to the company")
                print(f"Type: {type(certificate).__name__}")
                print(f"Watt: {certificate.get_watt()}")
                print(f"Company: {certificate.get_company_name()}")