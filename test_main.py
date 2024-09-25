from main import add,sub


def test_add1n1():
    assert add(1,1) == 2

def test_add3n1():
    assert add(3,1) == 4

def test_addm3n3():
    assert add(-3,3) == 0

def test_addm3nm3():
    assert add(-3,-3) == -6

def test_subm3nm3():
    assert sub(-3,-3) == 0

def test_sub3n3():
    assert sub(3,3) == 0

def test_sub3nm3():
    assert sub(3,-3) == 6

def test_sub3nm1():
    assert sub(3,-1) == 4