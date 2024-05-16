from abc import ABC, abstractmethod
from typing import List
from entity.model.loan import Loan


class ILoanRepository(ABC):

    @abstractmethod
    def applyLoan(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def calculateInterestById(self, loan_id: int) -> float:
        pass

    @abstractmethod
    def calculateInterest(
        self, principal_amount: float, interest_rate: float, loan_term: int
    ) -> float:
        pass

    @abstractmethod
    def loanStatus(self, loan_id: int) -> str:
        pass

    @abstractmethod
    def calculateEMIbyID(self, loan_id: int) -> float:
        pass

    @abstractmethod
    def calculateEMI(
        self, principal_amount: float, interest_rate: float, loan_term: int
    ) -> float:
        pass

    @abstractmethod
    def loanRepayment(self, loan_id: int, amount: float) -> int:
        pass

    @abstractmethod
    def getAllLoan(self) -> List[Loan]:
        pass

    @abstractmethod
    def getLoanbyID(self, loan_id: int) -> Loan:
        pass
