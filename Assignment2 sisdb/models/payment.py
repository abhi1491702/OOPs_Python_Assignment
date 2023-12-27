from student import Student
from datetime import datetime

class Payment:
    def __init__(self, PaymentID, StudentID, Amount, PaymentDate):
        self._PaymentID = PaymentID
        self._StudentID = StudentID
        self._Amount = Amount
        self._PaymentDate = PaymentDate

    @property
    def PaymentID(self):
        return self._PaymentID

    @PaymentID.setter
    def PaymentID(self, new_PaymentID):
        if isinstance(new_PaymentID, int) and new_PaymentID > 0:
            self._PaymentID = new_PaymentID
        else:
            raise ValueError("Payment ID must be a positive integer.")

    @property
    def StudentID(self):
        return self._Student

    @StudentID.setter
    def StudentID(self, new_Student):
        if isinstance(new_Student,int):
            self._Student = new_Student
        else:
            raise ValueError("Invalid Student reference.")

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, new_Amount):
        if isinstance(new_Amount, (int, float)) and new_Amount >= 0:
            self._Amount = new_Amount
        else:
            raise ValueError("Amount must be a non-negative number.")

    @property
    def PaymentDate(self):
        return self._PaymentDate

    @PaymentDate.setter
    def PaymentDate(self, new_PaymentDate):
        if isinstance(new_PaymentDate, str) and len(new_PaymentDate) == 10:
            self._PaymentDate = new_PaymentDate
        else:
            raise ValueError("Invalid payment date format.")

    def GetStudent(self):
       pass

    def GetPaymentAmount(self):
        return self.Amount

    def GetPaymentDate(self):
        return self.PaymentDate

payment = Payment(101, 1, Amount=50, PaymentDate="2023-12-12")

    # Retrieve payment amount and date
payment_amount = payment.GetPaymentAmount()
payment_date = payment.GetPaymentDate()

    # Display payment information
print(f"Payment Amount: {payment_amount}")
print(f"Payment Date: {payment_date}")