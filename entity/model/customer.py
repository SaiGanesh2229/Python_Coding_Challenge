class Customer:
    def __init__(self):
        self.customer_id = 0
        self.name = ""
        self.email = ""
        self.phone_number = ""
        self.address = ""
        self.credit_score = 0

    def __init__(self, customer_id, name, email, phone_number, address, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.credit_score = credit_score

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_credit_score(self):
        return self.credit_score

    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    def print_info(self):
        print("Customer ID:", self.customer_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)
        print("Address:", self.address)
        print("Credit Score:", self.credit_score)
