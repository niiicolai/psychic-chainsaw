from company import Company
from certificate import Certificate

class Database():

    # A list storing all companies
    companies = []

    # Add a company to the list
    def add_company(company):
        # Raise value error if the company is not of type Company
        if not isinstance(company, Company):
            raise ValueError("The company must be of type Company")

        # Add the company to the list
        Database.companies.append(company)

