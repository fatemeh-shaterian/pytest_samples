from employee import Employee
import pytest

@pytest.fixture
def emp1() -> Employee:
    print('in emp1 fixture')
    return Employee('fatemeh','sh', 1000)

@pytest.fixture
def emp2() -> Employee:
    print('in emp2 fixture')
    yield Employee('Ali','Alavi', 8000)
    print('\nin emp2 tearDown')


def test_email(emp1, emp2):
    assert emp1.get_email() == 'fatemeh.sh@gmail.com'
    assert emp2.get_email() == 'Ali.Alavi@gmail.com'

    emp1.first = 'ahmad'
    emp1.last = 'ahmadi'

    assert emp1.get_email() == 'ahmad.ahmadi@gmail.com'
    print('test_email')

def test_fullname(emp1,emp2):

    assert emp1.get_ful_name(), 'fatemeh sh'
    assert emp2.get_ful_name(), 'Ali Alavi'
    print('test_fullname')

def test_apply_raise(emp1,emp2):

    emp1.apply_raise()
    emp2.apply_raise()

    assert emp1.pay== 1080
    assert emp2.pay== 8640
    print('test_apply_raise')


