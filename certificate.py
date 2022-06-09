
# A certificate represents a piece of information about a company, 
# such as watt, or type of certificate. This certificate class is
# the base class for all certificates.
class Certificate():

    def __init__(self, watt, company_name):
        # Raise value error if watt 
        # is not of type float
        if not isinstance(watt, float):
            raise ValueError("The watt must be of type float")

        # Raise value error if company_name 
        # is not of type string
        if not isinstance(company_name, str):
            raise ValueError("The company_name must be of type string")

        # Set the amount of watt
        self.watt = watt

        # Set the name of the certificate's company
        self.company_name = company_name

    # Getter method

    def get_company_name(self):
        # Return the name of the company
        return self.company_name

    def get_watt(self):
        # Return the amount of watt
        return self.watt

# This certificate class represents a certificate where
# the watt were produced by sun energi. The class is a subclass of
# the Certificate base class defined in certificate.py.
class Sun(Certificate):

    def __init__(self, watt, company_name):
        # Call the __init__ method of the parent class
        super().__init__(watt, company_name)
        # Example on Sun specific property
        self.cells = 1

# This certificate class represents a certificate where
# the watt were produced by wind energi. The class is a subclass of
# the Certificate base class defined in certificate.py.
class Wind(Certificate):

    def __init__(self, watt, company_name):
        # Call the __init__ method of the parent class
        super().__init__(watt, company_name)
        # Example on Wind specific property
        self.size = 1