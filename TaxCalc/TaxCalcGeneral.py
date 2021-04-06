# 01a, 07Apr2021, SreenivasK, Initial code

from abc import ABC
from .TaxCalcAPI import TaxCalcAPI


class TaxCalcGeneral(TaxCalcAPI, ABC):
    def __init__(self):
        super().__init__()

    def calculate_tax(self, cost: float) -> float:
        """

        Args:
            cost: Cost of the item

        Returns:
            Tax

        """

        return self.round_nearest(((cost / 100) * 10), 0.05)


