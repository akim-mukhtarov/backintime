import heapq
from .order import Order, OrderTypes


class OrdersRepository:
    '''
    Use priority queue for limit orders,
    and list/queue for market ones
    '''
    def __init__(self):
        # map order to item in priority queue
        self._entry_finder = {}
        self._orders = {
            OrderTypes.Market: [],
            OrderTypes.Limit: []
        }

    def append(self, order):
        order_t = order.type
        collection = self._orders[order_t]

        if order_t is OrderTypes.Limit:
            entry = (order.price, order)
            self._entry_finder[order] = entry
            heapq.heappush(collection, entry)
        else:
            self._orders[order_t].append(order)

    def remove(self, order):
        order_t = order.type
        collection = self._orders[order_t]
        entry = order
        if order_t is OrderTypes.Limit:
            entry = self._entry_finder[order]
        collection.remove(entry)

    def items(self):
        return self._orders.items()

    def __len__(self):
        return sum(map(lambda orders: len(orders), self._orders.values()))
