import numpy as np

from pandas import DataFrame
from typing import Tuple
from typing import List
from typing import Union
from typing import Optional


from pyrobot.stock_frame import StockFrame
from td.client import TDClient

class Portfolio:

    def __init__(self, account_number: Optional[str]):
        
        self.positions = {}
        self.positions_count = 0
        self.market_value = 0.0
        self.profit_loss = 0.0
        self.risk_tolerance = 0.0
        self.account_number = account_number

    def add_position(self, symbol: str, asset_type: str, purchase_date: Optional[str], quantity: int = 0, purchase_price: float = 0.0) -> dict:

        self.positions[symbol] = {}
        self.positions[symbol]['symbol'] = symbol
        self.positions[symbol]['quantity'] = quantity
        self.positions[symbol]['purchase_price'] = purchase_price
        self.positions[symbol]['purchase_date'] = purchase_date
        self.positions[symbol]['asset_type'] = asset_type

        return self.positions
    
    def add_positions(self, positions: List[dict]) -> dict:

        if not isinstance(positions, list):
            raise TypeError("Must be a list of dictionaries!")
        
        for position in positions:
            self.add_position(
                symbol=position['symbol'],
                asset_type = position['asset_type'],
                purchase_date = position.get('purchase_date', None),
                purchase_price = position.get('purchase_price', 0.0),
                quantity = position.get('quantity', 0)
            )
            
            return self.positions
        

    def remove_position(self, symbol: str) -> Tuple[bool, str]:
        
        if symbol in self.positions:
            del self.positions[symbol]
            return (True, f"Symbol: {symbol} was succefully removed")
        else:
            return (False, f"Symbol: {symbol} does not exist in portfolio")

    def in_portforlio(self, symbol:str) -> bool:
        if symbol in self.position:
            return True
        else:
            False

    def is_profitable(self, symbol:str, current_price:float) -> bool:
        #Grab the purchase price
        purchase_price = self.positions[symbol]['purchase_price']

        if (purchase_price < current_price):
            return True 
        else:
            return False


      
    def total_allocation(self):
        ...

    def risk_exposure(self):
        ...

    def total_market_value(self):
        ...






 