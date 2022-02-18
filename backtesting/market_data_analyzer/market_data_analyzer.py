from typing import Iterable

from ..candles_providers import CandlesProvider
from ..market_data_storage import MarketDataStorage


class MarketDataAnalyzer:

    def __init__(
            self,
            market_data: CandlesProvider,
            oscillators: Iterable[Callable]
    ):
        self._values = MarketDataStorage(market_data)
        # init oscillators
        oscillators = map(lambda x: x(self._values), oscillators)
        # Маппим осцилляторы к их имени для random access
        self._oscillators = {
            oscillator.get_name() : oscillator
                for oscillator in oscillators
        }

    def update(self) -> None:
        self._values.update()

    def get(self, oscillator_name: str) -> float:
        # calculate oscillator value on demand
        oscillator = self._oscillators.get(oscillator_name)

        if not oscillator:
            raise ValueError(
                f'No oscillator with provided name {oscillator_name} was found'
            )

        return oscillator()
