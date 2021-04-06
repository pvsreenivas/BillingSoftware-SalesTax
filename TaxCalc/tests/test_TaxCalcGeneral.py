# 01a, 07Apr2021, SreenivasK

from unittest.mock import MagicMock, patch
from TaxCalc.TaxCalcGeneral import TaxCalcGeneral


def test_get_receipt_product_list():
    tot_calc = TaxCalcGeneral()

    ret_val = tot_calc.calculate_tax(5.5675)

    assert ret_val == 0.6

