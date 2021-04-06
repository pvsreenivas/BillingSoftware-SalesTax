# 01a, 07Apr2021, SreenivasK, Initial code

from unittest.mock import MagicMock, patch
from TaxCalc.TotalCalc import TotalCalc


def test_get_receipt_product_list():
    tot_calc = TotalCalc(["1 imported bottle of perfume at 27.99", "1 bottle of perfume at 18.99",
                          "1 packet of headache pills at 9.75", "1 box of imported chocolates at 11.25"])

    ret_val = tot_calc.get_receipt_product_list()

    assert ret_val == ['1 imported bottle of perfume : 32.19',
                       '1 bottle of perfume : 20.89',
                       '1 packet of headache pills : 9.75',
                       '1 box of imported chocolates : 11.85',
                       'Sales Taxes: 6.70',
                       'Total: 74.70']

