

def buy_sell_stock(A:list) -> int:

    smallest = A[0]
    max_profit = 0
    curr_profit = 0

    for i in A:
        if i < smallest:
            smallest = i
        
        curr_profit = i-smallest
        if curr_profit > max_profit:
            max_profit = curr_profit

    return max_profit


def test_buy_sell_stock_returns_correct_max_profit():

    A = [7,1,2,3,6,5]

    assert 5 == buy_sell_stock(A)

def test_buy_sell_stock_returns_zero_when_no_profit():

    A = [9,8,7,6,5,4,3,2,1]

    assert 0 == buy_sell_stock(A)

def test_buy_sell_stock_returns_zero_when_no_volatility():

    A = [5,5,5,5,5,5,5]

    assert 0 == buy_sell_stock(A)


if __name__ == '__main__':
    test_buy_sell_stock_returns_correct_max_profit()
    test_buy_sell_stock_returns_zero_when_no_profit()
    test_buy_sell_stock_returns_zero_when_no_volatility()