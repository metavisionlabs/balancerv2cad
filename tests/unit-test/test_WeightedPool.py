from decimal import *
from BalancerV2cad.WeightedPool import WeightedPool

class TestWeightedPool:

    def test_join_pool(weightedpool_test):
        wp = WeightedPool()
        wp.join_pool({'btc':2,'eth':20},{'btc':0.2,'eth':0.8})

    def test_exit_pool(weightedpool_test):
        wp = WeightedPool()
        wp.join_pool({'btc':2,'eth':20},{'btc':0.2,'eth':0.8})
        wp.exit_pool({'btc':1})
        assert wp._balances['btc'] == 1

    def test_set_swap_fee(weightedpool_test):
        wp = WeightedPool()
        wp.set_swap_fee(4)
        assert wp._swap_fee == 4

    def test_set_weights(weightedpool_test):
        wp = WeightedPool()
        wp.join_pool({'btc':2,'eth':20},{'btc':0.2,'eth':0.8})
        wp.set_weights({'btc':0.1,'eth':0.3})
        assert wp._weights == {'btc':0.1,'eth':0.3}

    def test_swap(weightedpool_test):
        wp = WeightedPool()
        wp.join_pool({'btc':2,'eth':20},{'btc':0.2,'eth':0.8})
        wp.swap('btc','eth',0.2)
        #assert()