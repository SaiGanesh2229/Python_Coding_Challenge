from typing import List
from entity.model.loan import Loan
from dao.ILoanRepository import ILoanRepository
from Util import DBUtil


class ILoanRepositoryImpl:

    def applyLoan(self, loan: Loan) -> None:
        print("Applying for loan...")
        try:
            # Connect to the database
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            # Execute SQL statement to insert loan details into a table
            cursor.execute(
                "INSERT INTO loans (customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (
                    loan.customer_id,
                    loan.principal_amount,
                    loan.interest_rate,
                    loan.loan_term,
                    loan.loan_type,
                    loan.loan_status,
                ),
            )

            # Commit the transaction
            connection.commit()

            print("Loan applied successfully.")
        except Exception as e:
            print(f"An error occurred while applying for the loan: {e}")
        print("Loan applied successfully.")

    def calculateInterestById(self, loan_id: int) -> float:
        print(f"Calculating interest for loan with ID: {loan_id}...")

        try:
            # Connect to the database
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            # Query the database to fetch loan details using the loan ID
            cursor.execute(
                "SELECT principal_amount, interest_rate, loan_term FROM loans WHERE loan_id = ?",
                (loan_id,),
            )
            loan_details = cursor.fetchone()  # Assuming you fetch only one row

            if loan_details:
                principal_amount, interest_rate, loan_term = loan_details
                # Perform calculations to calculate interest
                interest = (principal_amount * interest_rate * loan_term) / 12
                print(f"Interest calculated: {interest}")
            else:
                print(f"No loan found with ID: {loan_id}")

        except Exception as e:
            print(f"An error occurred while calculating interest: {e}")

        finally:
            # Close the database connection
            if connection:
                connection.close()
                print("Database connection closed.")

    def loanStatus(self, loan_id: int) -> str:
        print(f"Checking loan status for loan with ID: {loan_id}...")

        try:
            # Connect to the database
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            # Query the database to fetch credit score using the loan ID
            cursor.execute(
                "SELECT credit_score FROM customers WHERE customer_id = (SELECT customer_id FROM loans WHERE loan_id = ?)",
                (loan_id,),
            )
            credit_score = cursor.fetchone()  # Assuming you fetch only one row

            if credit_score:
                credit_score = credit_score[0]
                # Determine loan status based on credit score
                if credit_score > 650:
                    loan_status = "Approved"
                else:
                    loan_status = "Rejected"
                print(f"Loan status: {loan_status}")
                return loan_status
            else:
                print(f"No credit score found for loan with ID: {loan_id}")
            return "Unknown"

        except Exception as e:
            print(f"An error occurred while checking loan status: {e}")
        return "Error"

    def calculateEMIById(self, loan_id: int) -> float:
        print(f"Calculating EMI for loan with ID: {loan_id}...")

        try:
            # Connect to the database
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            # Query the database to fetch loan details using the loan ID
            cursor.execute(
                "SELECT principal_amount, interest_rate, loan_term FROM loans WHERE loan_id = ?",
                (loan_id,),
            )
            loan_details = cursor.fetchone()  # Assuming you fetch only one row

            if loan_details:
                principal_amount, interest_rate, loan_term = loan_details
                # Calculate Monthly Interest Rate
                monthly_interest_rate = interest_rate / 12 / 100
                # Calculate EMI
                emi = (
                    principal_amount
                    * monthly_interest_rate
                    * ((1 + monthly_interest_rate) ** loan_term)
                ) / (((1 + monthly_interest_rate) ** loan_term) - 1)
                print(f"EMI calculated: {emi}")
            else:
                print(f"No loan found with ID: {loan_id}")
            return 0.0

        except Exception as e:
            print(f"An error occurred while calculating EMI: {e}")
        return 0.0

    def loanRepayment(self, loan_id: int, amount: float) -> int:
        print(f"Processing loan repayment for loan with ID: {loan_id}...")
        try:
            # Connect to the database
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            # Query the database to fetch loan details using the loan ID
            cursor.execute(
                "SELECT principal_amount, interest_rate, loan_term FROM loans WHERE loan_id = ?",
                (loan_id,),
            )
            loan_details = cursor.fetchone()  # Assuming you fetch only one row

            if loan_details:
                principal_amount, interest_rate, loan_term = loan_details
                # Calculate Monthly Interest Rate
                monthly_interest_rate = interest_rate / 12 / 100
                # Calculate EMI
                emi = (
                    principal_amount
                    * monthly_interest_rate
                    * ((1 + monthly_interest_rate) ** loan_term)
                ) / (((1 + monthly_interest_rate) ** loan_term) - 1)
                # Determine number of EMIs that can be paid from the amount
                num_emis = int(amount / emi)
                print(f"Number of EMIs paid: {num_emis}")
            else:
                print(f"No loan found with ID: {loan_id}")

        except Exception as e:
            print(f"An error occurred while processing loan repayment: {e}")

    def getAllLoan(self) -> List[Loan]:
        print("Retrieving all loans...")
        # Here you would retrieve all loans from the database
        loans = []  # Placeholder list for demonstration
        try:
            # Connect to the database
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            # Query the database to retrieve all loan details
            cursor.execute("SELECT * FROM loans")
            loan_records = cursor.fetchall()

            for record in loan_records:
                # Assuming each record contains loan details in the same order as Loan class attributes
                loan = Loan(*record)
                loans.append(loan)

            print("Printing details of all loans:")
            for loan in loans:
                print(loan)

            return loans

        except Exception as e:
            print(f"An error occurred while retrieving all loans: {e}")
            return []

    def getLoanById(self, loan_id: int) -> Loan:
        print(f"Retrieving loan details for loan with ID: {loan_id}...")
        try:
            # Connect to the database
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            # Query the database to retrieve loan details using the loan ID
            cursor.execute("SELECT * FROM loans WHERE loan_id = ?", (loan_id,))
            loan_record = cursor.fetchone()

            if loan_record:
                # Assuming loan_record contains loan details in the same order as the attributes of the Loan class
                loan = Loan(*loan_record)
                print(f"Loan details: {loan}")
                return loan
            else:
                raise Exception(f"Loan with ID {loan_id} not found.")

        except Exception as e:
            print(f"An error occurred while retrieving loan details: {e}")
            raise
