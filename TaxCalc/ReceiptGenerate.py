# 01a, 07Apr2021, SreenivasK, Initial code

from typing import List, Dict
from .TotalCalc import TotalCalc


class ReceiptGenerate:
    def __init__(self):
        self.product_list: List[str] = []

    def receipt_generate(self):
        """

        Returns:
            None

        """
        print("Ready to bill the cart.")
        print("Please enter the products in the format: [QUANTITY] [PRODUCT NAME] at [COST PER PRODUCT]")
        print("Example: 1 book at 12.49\n")
        self.product_list = []
        cont: int = True
        print("Enter the sale details: \n")
        while cont:
            prod: str = input()
            if prod:
                self.product_list.append(prod.strip(" "))
            else:
                cont = False

        total_calc: TotalCalc = TotalCalc(self.product_list)
        taxed_product_list: List = total_calc.get_receipt_product_list()

        print("***********Receipt***********")
        for taxed_product in taxed_product_list:
            print("{}".format(taxed_product))
        print("**********Thank You**********")
        print("*********Visit Again*********\n")



