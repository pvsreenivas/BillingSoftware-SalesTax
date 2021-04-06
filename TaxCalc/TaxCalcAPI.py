# 01a, 07Apr2021, SreenivasK, Initial code

from typing import List
import math


class TaxCalcAPI:
    def __init__(self):
        pass

    def calculate_tax(self, cost: float) -> float:
        raise NotImplementedError

    def calculate_sales_tax(self, cost: float) -> float:
        raise NotImplementedError

    @staticmethod
    def round_nearest(num, nearest):
        return round(round(num / nearest) * nearest, -int(math.ceil(math.log10(nearest))))
