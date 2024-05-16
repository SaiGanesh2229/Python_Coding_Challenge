from ILoanRepositoryImpl import ILoanRepositoryImpl
from loan import Loan


class LoanManagement:
    def __init__(self):
        self.loan_repo = ILoanRepositoryImpl()

    def applyLoan(self):
        print("Applying for a loan...")
        customer_id = int(input("Enter customer ID: "))
        principal_amount = float(input("Enter principal amount: "))
        interest_rate = float(input("Enter interest rate: "))
        loan_term = int(input("Enter loan term (in months): "))
        loan_type = input("Enter loan type (CarLoan/HomeLoan): ")
        loan = Loan(
            loan_id=0,
            customer_id=customer_id,
            principal_amount=principal_amount,
            interest_rate=interest_rate,
            loan_term=loan_term,
            loan_type=loan_type,
            loan_status="Pending",
        )
        self.loan_repo.applyLoan(loan)
        print("Loan applied successfully.")

    def getAllLoan(self):
        print("Fetching all loans...")
        loans = self.loan_repo.getAllLoan()
        for loan in loans:
            print(loan)

    def getLoan(self):
        loan_id = int(input("Enter the loan ID: "))
        loan = self.loan_repo.getLoanById(loan_id)
        print(loan)

    def loanRepayment(self):
        loan_id = int(input("Enter the loan ID for repayment: "))
        amount = float(input("Enter the amount for repayment: "))
        num_emis_paid = self.loan_repo.loanRepayment(loan_id, amount)
        print(f"Number of EMIs paid: {num_emis_paid}")

    def exit(self):
        print("Exiting Loan Management System.")
        quit()

    def main(self):
        while True:
            print("\nLoan Management System")
            print("1. Apply for a loan")
            print("2. Get all loans")
            print("3. Get loan by ID")
            print("4. Repay a loan")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.applyLoan()
            elif choice == "2":
                self.getAllLoan()
            elif choice == "3":
                self.getLoan()
            elif choice == "4":
                self.loanRepayment()
            elif choice == "5":
                self.exit()
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    loan_management = LoanManagement()
    loan_management.main()
