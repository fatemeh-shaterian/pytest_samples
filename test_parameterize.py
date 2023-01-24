import pytest

@pytest.mark.parametrize(
    'company_id',
    ['123', '234', '345', '456'],
    ids=['Twitter', 'Instagram', 'Google', 'Facebook']
)
def test_company_name_test(company_id: str):
    print('\n test with {}'.format(company_id))

