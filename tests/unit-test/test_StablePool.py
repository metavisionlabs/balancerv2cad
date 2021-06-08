from decimal import Decimal
from src.BalancerV2cad.StablePool import StablePool
import unittest
from src.BalancerV2cad.BalancerConstants import *

class TestStablePool(unittest.TestCase):

    def test_balancerpool(stablepool_test):
        ...
    
    def test_swap_given_in(stablepool_test):
        POOL_SWAP_FEE_PERCENTAGE = Decimal(0.01)
        sp = StablePool()
        sp.set_swap_fee(POOL_SWAP_FEE_PERCENTAGE)
        balances = {'uni': Decimal(1), 'weth': Decimal(0.9)}
        print('swap-givne-in, balances', balances)
        sp.join_pool(balances)
        amount = Decimal(0.1)
        expected = Decimal(100986343323831144)/Decimal(1e18)
        result  = sp.swap(token_in='uni', token_out='weth',amount=amount, given_in=True)
        print('fee', sp._swap_fee)
        print('result', result)
        print('expected',expected)
        print('uni', sp._balances['uni'])
        print('weth', sp._balances['weth'])

        assert sp._balances['uni'] == expected




    