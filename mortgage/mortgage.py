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

    def _validate_amortization(self):
        if self.amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")

    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        if value > 0:
            self._loan_amount = value
        else:
            raise ValueError("Loan Amount must be positive.")

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if not isinstance(value, MortgageRate):
            raise ValueError("Rate provided is invalid.")
        self._rate = value

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        if not isinstance(value, MortgageFrequency):
            raise ValueError("Frequency provided is invalid.")
        self._frequency = value

    @property
    def amortization(self):
        return self._amortization

    @amortization.setter
    def amortization(self, value):
        if value not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self._amortization = value

    def calculate_payment(self):
        # Implement the payment calculation using the provided formula
        # M = P * (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)
        i = self.rate.value / 12
        n = self.frequency.value * self.amortization
        payment = self.loan_amount * (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)
        return round(payment, 2)

    def __str__(self):
        return f"Mortgage Amount: ${self.loan_amount:,.2f}\nRate: {self.rate.value * 100:.2f}%\nAmortization: {self.amortization}\nFrequency: {self.frequency.name} -- Calculated Payment: ${self.calculate_payment():,.2f}"

    def __repr__(self):
        return f"[{self.loan_amount}, {self.rate.value:.4f}, {self.amortization}, {self.frequency.value}]"
