"""
Description: A class used to test the Mortgage class.
Author: Simran Kaur
Date: 13/11/2023
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

# test_mortgage.py

import unittest
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class MortgageTests(unittest.TestCase):
    
    def test_init_valid_inputs(self):
        loan_amount = 500000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 30

        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        # Verify using accessors
        self.assertEqual(mortgage.loan_amount, loan_amount)
        self.assertEqual(mortgage.rate, rate)
        self.assertEqual(mortgage.frequency, frequency)
        self.assertEqual(mortgage.amortization, amortization)
 
   