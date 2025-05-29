from multiply import mul

def test_mul():
    assert mul(2, 3) == 6
def test_mul_negative():
    assert mul(-2, 3) == -6
def test_mul_zero():
    assert mul(0, 5) == 0
def test_mul_float():
    assert mul(2.5, 4) == 10.0