from certificate import Certificate

class Company():

    def __init__(self, name):
        # Raise value error if the name is not of type string
        if not isinstance(name, str):
            raise ValueError("The name must be of type string")

        # Set the name of the company
        self.name = name
        # Create a list used for storing certificates
        self.certificates = []

    def add_certificate(self, certificate):
        # Raise value error if the certificate 
        # is not of type Certificate
        if not isinstance(certificate, Certificate):
            raise ValueError("The certificate must be of type Certificate")
        
        # Add a certificate to the list
        self.certificates.append(certificate)

    def compare_to(self, name):
        # Raise value error if the name is not of type string
        if not isinstance(name, str):
            raise ValueError("The name must be of type string")
        
        # Compare the name of the company to the name of the company
        return self.name.upper() == name.upper()

    # Getter methods

    def get_certificates(self):
        # Return the list of certificates
        return self.certificates
    
    def get_name(self):
        # Return the name of the company
        return self.name
    

