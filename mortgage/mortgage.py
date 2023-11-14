"""
Description: A class meant to manage Mortgage options.
Author: Simran Kaur
Date: 13/11/2023
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

# mortgage.py

from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class Mortgage:
    def __init__(self, loan_amount, rate, frequency, amortization):
        self.loan_amount = loan_amount
        self.rate = rate
        self.frequency = frequency
        self.amortization = amortization

        # Validate inputs
        self._validate_loan_amount()
        self._validate_rate()
        self._validate_frequency()
        self._validate_amortization()

    def _validate_loan_amount(self):
        if self.loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")

    

 def _validate_rate(self):
        if not isinstance(self.rate, MortgageRate):
            raise ValueError("Rate provided is invalid.")
 def _validate_frequency(self):
        if not isinstance(self.frequency, MortgageFrequency):
            raise ValueError("Frequency provided is invalid.")