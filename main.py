# Makkajai Dev Challenge

# Problem: Sales Tax
# Author: Sreenivas Kavali

from TaxCalc.ReceiptGenerate import ReceiptGenerate


def sales_tax_init():
    """
    Initiate the sales tax program

    Returns:
        None

    """

    print("************************************************************")
    print("************Welcome to Billing Software v0.1****************")
    print("************************************************************")
    receipt_gen = ReceiptGenerate()
    while True:
        receipt_gen.receipt_generate()


if __name__ == '__main__':
    sales_tax_init()

