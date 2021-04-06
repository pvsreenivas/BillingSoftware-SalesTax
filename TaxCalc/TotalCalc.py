# 01a, 07Apr2021, SreenivasK, Initial code

from typing import List
from .TaxCalcStrings import TaxCalcStrings
from .TaxCalcGeneral import TaxCalcGeneral
from .TaxCalcExempted import TaxCalcExempted
from .TaxCalcAPI import TaxCalcAPI
from .SalesTaxCalc import SalesTaxCalc


class TotalCalc(TaxCalcAPI):

    def __init__(self, product_list: List[str]):
        super().__init__()
        self.product_list = product_list
        self.tax_calc_exempted: TaxCalcAPI = TaxCalcExempted()
        self.tax_calc_general: TaxCalcAPI = TaxCalcGeneral()
        self.tax_calc_sales: TaxCalcAPI = SalesTaxCalc()

    def get_receipt_product_list(self) -> List:
        """

        Returns: List of items in the receipt

        """
        receipt_list: List[str] = []
        total_tax: float = 0
        total_cost: float = 0
        for product in self.product_list:
            tax: float = 0
            sales_tax: float = 0
            product_tokens: List = product.split()
            try:
                item_count: float = float(product_tokens[0])
                item_cost: float = float(product_tokens[-1])
                item_total_cost: float = item_count * item_cost
            except Exception:
                print("Item not in expected format: {}".format(product))
                continue

            try:
                if TaxCalcStrings.PILLS in product or \
                        TaxCalcStrings.BOOK in product or \
                        TaxCalcStrings.CHOCOLATE in product:
                    tax = self.tax_calc_exempted.calculate_tax(item_total_cost)

                else:
                    tax = self.tax_calc_general.calculate_tax(item_total_cost)
            except Exception as ex:
                print("Exception occurred: {} for product: {}, taking tax as 0".format(ex, product))
                tax = 0

            if TaxCalcStrings.IMPORTED in product:
                sales_tax = self.tax_calc_sales.calculate_sales_tax(item_total_cost)

            item_total_cost = round((item_total_cost + tax + sales_tax), 2)
            total_tax = total_tax + tax + sales_tax
            total_cost = total_cost + item_total_cost

            product_tokens[-2] = ":"
            product_tokens[-1] = "{:.2f}".format(item_total_cost)

            taxed_product: str = " ".join(product_tokens)

            receipt_list.append(taxed_product)

        receipt_list.append("Sales Taxes: {:.2f}".format(self.round_nearest(total_tax, 0.05)))
        receipt_list.append("Total: {:.2f}".format(self.round_nearest(total_cost, 0.05)))

        return receipt_list


