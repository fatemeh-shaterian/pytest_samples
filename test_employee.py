from employee import Employee
import pytest

@pytest.mark.email
def test_email():
    emp1 = Employee('fatemeh', 'sh', 1000)
    emp2 = Employee('Ali', 'Alavi', 8000)

    assert emp1.get_email() == 'fatemeh.sh@gmail.com' , "this is not right"
    assert emp2.get_email() == 'Ali.Alavi@gmail.com'

    emp1.first = 'ahmad'
    emp1.last = 'ahmadi'

    assert emp1.get_email() == 'ahmad.ahmadi@gmail.com'

def test_fullname():
    emp1 = Employee('fatemeh', 'sh', 1000)
    emp2 = Employee('Ali', 'Alavi', 8000)

    assert emp1.get_ful_name() == 'fatemeh sh'
    assert emp2.get_ful_name() == 'Ali Alavi'

@pytest.mark.slow
def test_apply_raise():
    emp1 = Employee('fatemeh', 'sh', 1000)
    emp2 = Employee('Ali', 'Alavi', 8000)

    emp1.apply_raise()
    emp2.apply_raise()

    assert emp1.pay == 1080
    assert emp2.pay == 8640


