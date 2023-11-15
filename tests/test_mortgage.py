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

    def test_init_invalid_amount(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(-500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)

    def test_init_invalid_rate(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(500000, 0.05, MortgageFrequency.MONTHLY, 30)

    def test_init_invalid_frequency(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(500000, MortgageRate.FIXED_5, "INVALID_FREQUENCY", 30)

    def test_init_invalid_amortization(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, -30)
    
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

    def test_loan_amount_mutator_negative_value(self):
        mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        
        with self.assertRaises(ValueError):
            mortgage.loan_amount = -100000

    def test_loan_amount_mutator_zero_value(self):
        mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        
        with self.assertRaises(ValueError):
            mortgage.loan_amount = 0

    def test_loan_amount_mutator_positive_value(self):
        mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        
        mortgage.loan_amount = 600000
        self.assertEqual(mortgage.loan_amount, 600000)

    def test_rate_mutator_valid_enum_value(self):
        mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        
        mortgage.rate = MortgageRate.VARIABLE_3
        self.assertEqual(mortgage.rate, MortgageRate.VARIABLE_3)

    def test_rate_mutator_invalid_enum_value(self):
        mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        
        with self.assertRaises(ValueError):
            mortgage.rate = 0.05
            
    def test_frequency_mutator_valid_enum_value(self):
        mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        
        mortgage.frequency = MortgageFrequency.BI_WEEKLY
        self.assertEqual(mortgage.frequency, MortgageFrequency.BI_WEEKLY)

    def test_frequency_mutator_invalid_enum_value(self):
        mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        
        with self.assertRaises(ValueError):
            mortgage.frequency = 15

    def test_amortization_mutator_valid_value(self):
        mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        
        mortgage.amortization = 20
        self.assertEqual(mortgage.amortization, 20)

    def test_amortization_mutator_invalid_value(self):
        mortgage = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        
        with self.assertRaises(ValueError):
            mortgage.amortization = 40


    def test_calculate_payment_monthly(self):
        mortgage_monthly = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        expected_monthly_payment = 2684.11
        self.assertAlmostEqual(mortgage_monthly.calculate_payment(), expected_monthly_payment, places=2)

    def test_calculate_payment_biweekly(self):
        mortgage_biweekly = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.BI_WEEKLY, 30)
        expected_biweekly_payment = 2167.96
        self.assertAlmostEqual(mortgage_biweekly.calculate_payment(), expected_biweekly_payment, places=2)

    def test_calculate_payment_weekly(self):
        mortgage_weekly = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.WEEKLY, 30)
        expected_weekly_payment = 2086.51
        self.assertAlmostEqual(mortgage_weekly.calculate_payment(), expected_weekly_payment, places=2)

    def test_str_representation_monthly(self):
        mortgage_monthly = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        expected_str_monthly = "Mortgage Amount: $500,000.00\nRate: 5.00%\nAmortization: 30\nFrequency: MONTHLY -- Calculated Payment: $2,684.11"
        self.assertEqual(str(mortgage_monthly), expected_str_monthly)

    def test_str_representation_biweekly(self):
        mortgage_biweekly = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.BI_WEEKLY, 30)
        expected_str_biweekly = "Mortgage Amount: $500,000.00\nRate: 5.00%\nAmortization: 30\nFrequency: BI_WEEKLY -- Calculated Payment: $2,167.96"
        self.assertEqual(str(mortgage_biweekly), expected_str_biweekly)

    def test_str_representation_weekly(self):
        mortgage_weekly = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.WEEKLY, 30)
        expected_str_weekly = "Mortgage Amount: $500,000.00\nRate: 5.00%\nAmortization: 30\nFrequency: WEEKLY -- Calculated Payment: $2,086.51"
        self.assertEqual(str(mortgage_weekly), expected_str_weekly)

    def test_repr_representation_monthly(self):
        mortgage_monthly = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        expected_repr_monthly = "[500000, 0.0500, 30, 12]"
        self.assertEqual(repr(mortgage_monthly), expected_repr_monthly)

    def test_repr_representation_biweekly(self):
        mortgage_biweekly = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.BI_WEEKLY, 30)
        expected_repr_biweekly = "[500000, 0.0500, 30, 26]"
        self.assertEqual(repr(mortgage_biweekly), expected_repr_biweekly)

    def test_repr_representation_weekly(self):
        mortgage_weekly = Mortgage(500000, MortgageRate.FIXED_5, MortgageFrequency.WEEKLY, 30)
        expected_repr_weekly = "[500000, 0.0500, 30, 52]"
        self.assertEqual(repr(mortgage_weekly), expected_repr_weekly)

if __name__ == '__main__':
    unittest.main()
