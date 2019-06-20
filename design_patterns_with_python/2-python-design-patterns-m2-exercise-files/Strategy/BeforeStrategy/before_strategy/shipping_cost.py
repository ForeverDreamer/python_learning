from before_strategy import Shipper


class ShippingCost:
    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost()
        elif order.shipper == Shipper.ups:
            return self._ups_cost()
        elif order.shipper == Shipper.postal:
            return self._postal_cost()
        else:
            raise ValueError('Invalid shipper %s', order.shipper)

    @staticmethod
    def _fedex_cost():
        return 3.00

    @staticmethod
    def _ups_cost():
        return 4.00

    @staticmethod
    def _postal_cost():
        return 5.00
