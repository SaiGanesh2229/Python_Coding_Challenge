from loan import Loan


class HomeLoan(Loan):
    def __init__(self):
        super().__init__()
        self.property_address = ""
        self.property_value = 0

    def __init__(
        self,
        loan_id,
        customer,
        principal_amount,
        interest_rate,
        loan_term,
        loan_status,
        property_address,
        property_value,
    ):
        super().__init__(
            loan_id,
            customer,
            principal_amount,
            interest_rate,
            loan_term,
            "HomeLoan",
            loan_status,
        )
        self.property_address = property_address
        self.property_value = property_value

    def get_property_address(self):
        return self.property_address

    def set_property_address(self, property_address):
        self.property_address = property_address

    def get_property_value(self):
        return self.property_value

    def set_property_value(self, property_value):
        self.property_value = property_value

    def print_info(self):
        super().print_info()
        print("Property Address:", self.property_address)
        print("Property Value:", self.property_value)
