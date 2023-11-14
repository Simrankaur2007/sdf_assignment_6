# sdf_Assignment 6

## Description
This project involves the use of classes and enums to determine mortgage payment options for clients. It includes the creation of an Enum, a Class, a Unit Test Class, and updates to the client program.

## Author
Simran Kaur
## Assignment Details
This assignment, Assignment 6, focuses on defining and using classes. The key components of the project include:

1. **Created Enum:** Defined a MortgageRate enumeration class in the `pixell_lookup.py` file, inheriting from Enum. This enumeration includes options for different mortgage rates such as FIXED_5, FIXED_3, FIXED_1, VARIABLE_5, VARIABLE_3, and VARIABLE_1.

2. **Created Enum:** Defined a MortgageFrequency enumeration class in the `pixell_lookup.py` file, inheriting from Enum. This enumeration includes options for payment frequencies, including MONTHLY, BI_WEEKLY, and WEEKLY.

3. **List (Given):** Utilized a given list named `VALID_AMORTIZATION` in the `pixell_lookup.py` file, containing allowable options for the length of the mortgage in years (amortization). The list includes values such as 5, 10, 15, 20, 25, and 30 years.

4. **Defined Mortgage Class:** In the `mortgage.py` file, defined a class named Mortgage that makes use of the Enumerations and List mentioned above. Included methods for accessing and mutating attributes, as well as a method for calculating mortgage payments.

5. **Unit Test Class:** Created a unit test class, `test_mortgage.py` in the `tests` folder, to test the functionality of the Mortgage class. Covered various scenarios to ensure proper validation and behavior of the class.

6. **Client Program Updates:** Modified the provided `main.py` file to incorporate the Mortgage class, MortgageRate and MortgageFrequency enums, and the VALID_AMORTIZATION list. Enclosed the file reading block in a try-except block to catch FileNotFoundError exceptions.

## Instructions for Running the Program
1. Ensure that the required directory structure is in place.
2. Initialize a new Git repository and connect it to a remote repository on GitHub.
3. Run the `main.py` program to process batch mortgage loan data.

## Notes
- The project aims to provide accurate mortgage payment information based on client input.


