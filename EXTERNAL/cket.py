def calculate_total(prices, discount_threshold=100, discount_rate=0.1):
    total = sum(prices)
    if total > discount_threshold:
        total -= total * discount_rate
    return total


def test_no_discount():
    prices = [20, 30, 40]
    assert calculate_total(prices) == 90


def test_with_discount():
    prices = [50, 60, 70]
    assert calculate_total(prices) == 162  # 180 - 10% discount


def test_edge_case():
    prices = [50, 50]
    assert calculate_total(prices) == 100  # exactly at the threshold

# Running pytest automatically discovers and runs these tests.
