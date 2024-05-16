from loan import Loan


class CarLoan(Loan):
    def __init__(self):
        super().__init__()
        self.car_model = ""
        self.car_value = 0

    def __init__(
        self,
        loan_id,
        customer,
        principal_amount,
        interest_rate,
        loan_term,
        loan_status,
        car_model,
        car_value,
    ):
        super().__init__(
            loan_id,
            customer,
            principal_amount,
            interest_rate,
            loan_term,
            "CarLoan",
            loan_status,
        )
        self.car_model = car_model
        self.car_value = car_value

    def get_car_model(self):
        return self.car_model

    def set_car_model(self, car_model):
        self.car_model = car_model

    def get_car_value(self):
        return self.car_value

    def set_car_value(self, car_value):
        self.car_value = car_value

    def print_info(self):
        super().print_info()
        print("Car Model:", self.car_model)
        print("Car Value:", self.car_value)
