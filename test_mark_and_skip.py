import pytest

@pytest.mark.skip(reason="just skip")
def test_out_first_test():
    assert 1==2

@pytest.mark.skipif(5>2, reason="skipped because 5>2")
def test_skipped_if():
    assert 1==1

@pytest.mark.xfail
def test_dont_care():
    assert 1==2

